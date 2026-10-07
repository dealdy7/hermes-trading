# Format Pesan WhatsApp — Berita & Rekomendasi Saham

## /tnews — Berita Bullish
```
📈 BERITA BULLISH — [tanggal] [jam] WIB

1. [TICKER] (+X%)
   📰 [Judul berita]
   📝 [Ringkasan 1-2 kalimat]
   🔗 [Sumber]

2. [TICKER] (+X%)
   📰 [Judul berita]
   📝 [Ringkasan 1-2 kalimat]
   🔗 [Sumber]

... (maks 15)

📊 [N] berita dianalisa | Sentimen IHSG: [bullish]
```

## /bnews — Berita Bearish
```
📉 BERITA BEARISH — [tanggal] [jam] WIB

1. [TICKER] (-X%)
   📰 [Judul berita]
   📝 [Ringkasan 1-2 kalimat]
   🔗 [Sumber]

2. [TICKER] (-X%)
   📰 [Judul berita]
   📝 [Ringkasan 1-2 kalimat]
   🔗 [Sumber]

... (maks 15)

📊 [N] berita dianalisa | Sentimen IHSG: [bearish]
```

## /req — Rekomendasi Saham Sesi Pagi/Siang
```
🎯 REKOMENDASI SAHAM — [tanggal]

Berdasarkan: screener + sentimen berita + sentimen chat

1. [TICKER] @ [harga]
   💡 Thesis: [1 kalimat]
   📰 Berita pendukung:
      • [judul berita 1]
      • [judul berita 2]
   💬 Chat: [bull/bear ratio]
   📊 Conviction: [skor]/100
   🛡️ SL: [harga] | 🎯 TP: [harga]

2. [TICKER] @ [harga]
   ...

📝 Catatan:
• [catatan 1, misal: big-cap di-skip karena 1 lot > 250rb]
• [catatan 2, misal: IHSG flat, tunggu konfirmasi arah]
• [catatan 3]

⚠️ Bukan rekomendasi beli, hanya data untuk analisa
```

## /reqbs — Rekomendasi Saham BSJP
```
🌙 REKOMENDASI BSJP — [tanggal]

Berdasarkan: screener bandar_accum

TERBAIK:
📌 [TICKER] @ [harga] (rank [N])
   💡 [thesis 1 kalimat]
   📰 [berita pendukung jika ada]

MID:
📌 [TICKER] @ [harga] (rank [N])
   💡 [thesis 1 kalimat]
   📰 [berita pendukung jika ada]

TERJELEK:
📌 [TICKER] @ [harga] (rank [N])
   💡 [thesis 1 kalimat]
   📰 [berita pendukung jika ada]

📝 Catatan:
• [catatan relevan]

📊 Data untuk training ML, bukan rekomendasi beli
```

## Auto News Summary
```
📰 RINGKASAN BERITA — [jam] WIB

🔴 BERDAMPAK BESAR:
• [Judul] → [TICKER/sektor terdampak]

🟡 PERLU DIPANTAU:
• [Judul]
  [Ringkasan 1 kalimat]

📊 Sentimen IHSG: [bullish/bearish/netral]
```

## Aturan
- Bahasa Indonesia
- Timestamp WIB selalu
- Berita: maks 15 per command
- Rekomendasi: bukan ajakan beli, hanya data analisa
- Skip auto-summary jika tidak ada berita signifikan
