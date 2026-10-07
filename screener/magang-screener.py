#!/opt/saham/.venv/bin/python
"""Stockbit Screener Automation v2 — alur UI yang benar.
1. Edit Screener -> hapus rules -> Add a Rule -> Basic Ratio
2. Set metric via modal, operator, value
3. Klik Screen (TANPA Save) -> extract tabel
"""
import json, sys, argparse, time, os
from playwright.sync_api import sync_playwright

CHROME = "/home/hermes/.agent-browser/browsers/chrome-154.0.8037.92/chrome"
PROFILE = "/home/hermes/.hermes/browser-profile/stockbit"
LOCKF = "/home/hermes/.hermes/browser.lock"

PRESETS = {
    # Original Hermes: professional momentum
    'momentum': [
        {"metric": "1 Day Price Returns", "op": ">=", "val": 2},
        {"metric": "1 Day Price Returns", "op": "<=", "val": 15},
        {"metric": "Price", "op": ">=", "val": 60},
        {"metric": "Price", "op": "<=", "val": 2500},
        {"metric": "Bandar Accum/Dist", "op": ">=", "val": 0},
    ],
    # Filter "akan terbang" dari komunitas (Aldy 2026-10-06)
    'terbang_komunitas': [
        {"metric": "Price MA 5", "op": ">", "val": 0},
        {"metric": "Price", "op": ">", "val": 50},
        {"metric": "Bandar Accum/Dist", "op": ">", "val": 0},
        {"metric": "Market Cap", "op": ">", "val": 0},
        {"metric": "Price", "op": "<", "val": 2000},
        {"metric": "Value", "op": ">", "val": 0},
        {"metric": "Value MA 5", "op": ">", "val": 0},
        {"metric": "1 Day Price Returns", "op": ">", "val": 18},
        {"metric": "1 Day Price Returns", "op": "<=", "val": 30},
    ],
    'oversold_bounce': [
        {"metric": "RSI(14)", "op": "<=", "val": 35},
        {"metric": "Price", "op": "<=", "val": 2500},
        {"metric": "Price", "op": ">=", "val": 60},
    ],
    # Original Hermes: bandar accumulation
    'bandar_accum': [
        {"metric": "Bandar Accum/Dist", "op": ">=", "val": 10},
        {"metric": "1 Day Price Returns", "op": ">=", "val": 1},
        {"metric": "Price", "op": "<=", "val": 2500},
    ],
    # Filter BSJP dari Aldy (2026-10-06)
    'bsjp_aldy': [
        {"metric": "Value", "op": ">=", "val": 1000000},
        {"metric": "Price", "op": ">", "val": 60},
        {"metric": "1 Day Price Returns", "op": ">=", "val": 2},
        {"metric": "Bandar Accum/Dist", "op": ">=", "val": 10},
        {"metric": "Price", "op": "<=", "val": 2500},
        {"metric": "Price MA 20", "op": ">=", "val": 2},
        {"metric": "1 Day Price Returns", "op": "<=", "val": 15},
    ],
}

def lock():
    for _ in range(60):
        try:
            fd = os.open(LOCKF, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, str(os.getpid()).encode()); os.close(fd)
            return True
        except FileExistsError:
            time.sleep(2)
    return False

def unlock():
    try: os.unlink(LOCKF)
    except: pass

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--preset', default='momentum', choices=list(PRESETS.keys()))
    ap.add_argument('--limit', type=int, default=15)
    a = ap.parse_args()
    rules = PRESETS[a.preset]

    if not lock():
        print(json.dumps({'error': 'lock timeout'})); sys.exit(1)
    try:
        with sync_playwright() as pw:
            ctx = pw.chromium.launch_persistent_context(
                PROFILE, executable_path=CHROME, headless=False,
                args=['--no-sandbox', '--disable-dev-shm-usage'])
            pg = ctx.pages[0] if ctx.pages else ctx.new_page()
            pg.goto("https://stockbit.com/screener", timeout=30000)
            pg.wait_for_timeout(6000)

            # 1. Klik Edit Screener
            try:
                pg.click('button:has-text("Edit Screener")', timeout=45000)
            except:
                # Fallback: coba selector lain
                pg.click('button:text-is("Edit Screener")', timeout=45000)
            pg.wait_for_timeout(4000)

            # 2. Hapus semua rules lama
            for _ in range(20):
                b = pg.query_selector('[data-cy="screener-delete-rules-button"]')
                if not b: break
                b.click(); pg.wait_for_timeout(400)

            # 3. Tambah rules baru
            for r in rules:
                pg.click('button:has-text("Add a Rule")')
                pg.wait_for_timeout(1500)
                # Klik Basic Ratio dari dropdown
                pg.click('.ant-dropdown:not(.ant-dropdown-hidden) >> text=Basic Ratio')
                pg.wait_for_timeout(2000)
                # Klik input combobox via JS (placeholder text tidak bisa diklik langsung)
                pg.evaluate("""() => {
                    const sels = document.querySelectorAll('div.ant-select');
                    if (sels.length > 0) {
                        const last = sels[sels.length - 1];
                        const inp = last.querySelector('input[role=combobox]');
                        if (inp) inp.click(); else last.click();
                    }
                }""")
                pg.wait_for_timeout(1800)
                # Search di modal
                search = pg.query_selector('.ant-modal input')
                if search:
                    search.fill(r['metric'])
                    pg.wait_for_timeout(1200)
                    # Klik hasil yang cocok
                    opts = pg.query_selector_all('.ant-modal-body div')
                    for o in opts:
                        try:
                            if r['metric'].lower() in o.inner_text().lower():
                                o.click(); break
                        except: continue
                    pg.wait_for_timeout(800)
                # Operator
                sels = pg.query_selector_all('select')
                if sels:
                    try: sels[-1].select_option(r['op'])
                    except: pass
                # Value
                inp = pg.query_selector_all('input[name="value"]')
                if inp:
                    inp[-1].fill(str(r['val']))
                pg.wait_for_timeout(500)

            # 4. Klik Screen (hijau, tanpa Save)
            pg.click('button:has-text("Screen")')
            pg.wait_for_timeout(7000)

            # 5. Extract tabel
            rows = pg.query_selector_all('table tbody tr')
            out = []
            for row in rows[:a.limit]:
                try:
                    c = row.query_selector_all('td')
                    if len(c) >= 4:
                        out.append({
                            'symbol': c[0].inner_text().strip(),
                            'price': c[2].inner_text().strip(),
                            'change_1d': c[3].inner_text().strip(),
                        })
                except: continue
            ctx.close()
            print(json.dumps({'preset': a.preset, 'count': len(out),
                              'results': out}, indent=1))
    finally:
        unlock()

if __name__ == '__main__':
    main()
