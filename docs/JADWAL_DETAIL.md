# Jadwal Detail Hermes — Program Magang Trader

**Berlaku:** Hari bursa (Senin-Jumat)
**Zona waktu:** WIB (server CST - 1 jam)
**Budget:** 3.2jt/hari (2jt sesi pagi/siang + 1.2jt BSJP)

---

## Pagi

| Jam (WIB) | Kegiatan | Screener | Eksekusi | Keterangan |
|-----------|----------|----------|----------|------------|
| 08:50 | Watchlist Pagi | ❌ Belum bisa (market tutup) | ❌ | Analisis sentimen chat Stockbit, pre-market positioning |
| 09:00 | Market buka sesi 1 | ✅ momentum | ✅ | Mulai scan + eksekusi |
| 09:20, 09:50 | Scan kontinu | ✅ momentum | ✅ | Tiap :20 dan :50 |
| 10:20, 10:50 | Scan kontinu | ✅ momentum | ✅ | |
| 11:20, 11:50 | Scan kontinu | ✅ momentum | ✅ | |

## Istirahat Siang

| Jam (WIB) | Kegiatan | Screener | Eksekusi | Keterangan |
|-----------|----------|----------|----------|------------|
| 12:00-13:30 | Market istirahat | ✅ Bisa dipake | ❌ | Screener jalan buat persiapan/analisa, tapi TIDAK ada buy/sell. Monitor posisi hold tetap jalan. |

## Siang

| Jam (WIB) | Kegiatan | Screener | Eksekusi | Keterangan |
|-----------|----------|----------|----------|------------|
| 13:30 | Market buka sesi 2 | ✅ oversold_bounce | ✅ | Strategi reversal |
| 13:50 | Scan kontinu | ✅ oversold_bounce | ✅ | |
| 14:20 | Scan kontinu | ✅ oversold_bounce | ✅ | |
| 14:30 | Ganti preset | ✅ bandar_accum | ✅ | Strategi overnight |
| 14:50 | Scan kontinu | ✅ bandar_accum | ✅ | |
| **14:55** | **BSJP Daily Buy** | ✅ bandar_accum | ✅ | **Cron khusus**: beli 3 saham (terbaik/mid/terjelek) @400rb each. Full-otomatis. |
| 15:20, 15:50 | Scan kontinu | ✅ bandar_accum | ✅ | |
| 16:00 | Market tutup | — | ❌ | Tidak ada eksekusi lagi |

## Sore/Malam

| Jam (WIB) | Kegiatan | Keterangan |
|-----------|----------|------------|
| 16:30 | Laporan Sore | Rekap trading hari ini + jurnal |
| 18:00 | News summary | Ringkasan berita (via WA gateway, Fase 1) |

## Momentum Hunter

| Jadwal | Keterangan |
|--------|------------|
| Tiap 2 menit, 09:00-16:00 | Monitor cepat, model murah (unik/GLM-5.2). Skip jam istirahat 12:00-13:30. |

## Keep-Alive

| Jadwal | Keterangan |
|--------|------------|
| Tiap 2 jam | Cek session Stockbit, alert Telegram jika logout |

---

## Catatan

- **08:50**: screener BELUM bisa (market tutup), cuma analisis sentimen
- **12:00-13:30**: screener BISA dipake (data masih ada), tapi TIDAK ada eksekusi buy/sell
- **BSJP 14:55**: cron terpisah, tidak numpang scan kontinu
- Semua notifikasi ke Telegram Aldy
