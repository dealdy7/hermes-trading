# Backup Hermes System — 2026-10-07

Backup konfigurasi Hermes autonomous trading + WhatsApp gateway.
**TANPA secrets, API keys, atau credentials.**

## Isi

- `SOUL.md` — Persona + prinsip kepatuhan Hermes
- `cron/jobs-backup.json` — 9 cron jobs (jadwal, prompt, model)
- `screener/magang-screener.py` — 5 presets screener
- `whatsapp/FORMAT_WA.md` — Format pesan WA
- `docs/JADWAL_DETAIL.md` — Jadwal detail harian

## Cron Jobs (9)

1. Laporan pipeline reanalysis
2. Magang Watchlist Pagi (08:50 WIB)
3. Magang Laporan Sore (15:30 WIB)
4. Magang Scan Kontinu (tiap 30 mnt)
5. Magang Momentum Hunter (tiap 2 mnt)
6. Stockbit Keep-Alive (tiap 2 jam)
7. BSJP Daily Buy (14:55 WIB)
8. Hermes Monitor (tiap 30 mnt)
9. WA News Summary (8x sehari)

## Presets Screener (5)

- momentum, oversold_bounce, bandar_accum (Hermes)
- bsjp_aldy (Aldy)
- terbang_komunitas (komunitas, standby)

## Restore

1. Copy `jobs-backup.json` ke `~/.hermes/cron/jobs.json`
2. Copy `SOUL.md` ke `~/.hermes/SOUL.md`
3. Copy `magang-screener.py` ke `~/.hermes/bin/`
4. Restart gateway: `hermes gateway restart`
