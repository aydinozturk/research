# acm.org — Google SERP Çapraz Kontrolü (Chrome CDP)

Görev: #287 · Plan: #283 · Yapan: agent-6 · Tarih: 2026-11-06 ~06:55–07:00 UTC

## TL;DR

Gerçek Chrome (CDP `192.168.65.254:9222`, Chrome 156) üzerinden 4 Google sorgusu çalıştırıldı; CAPTCHA ve onay ekranı yok, bu turlarda **AI Özeti kutusu hiç görünmedi**. Bulgular:

1. **Google'un acm.org indeksi siteye göre geride:** Temmuz–Kasım 2026 arası medya merkezi haberleri (yeni CEO Alison Derbenwick Miller, dergi EiC atamaları, PQQS 2026 — 2–4 Kasım'da!, O'Reilly kütüphanesi) bu sorgularda SERP'te hiç çıkmıyor.
2. **`site:acm.org` sorgusunda ana acm.org site değil, alt alan adları diziliyor** — aralarında 2015 CHI konferans sitesi gibi ~11 yıllık sayfa bile var.
3. **SEO tuhaflıkları:** CACM haber arşivinin derin sayfa numaraları (Page 33/60/105) indeksli ve sıralanıyor; `blog.acm.org` Google'da **ham dizin listesi** olarak görünüyor; bir WordPress hosting alt alanı başlıksız ("Başlıksız") indekslenmiş.
4. **SERP'te site temelinde olmayan taze maddeler:** ICER 2026 (icer2026.acm.org), TAAS Eylül 2026 sayı 3 (DL), RecSys '26 / CI 2026 tarihleri, MM 2026 CFP, TechNews eski bir "son %8 genom" haberi.

## Yöntem

- Ham CDP (chrome-devtools MCP araçları worker session'ında listelenmediği için, t281'deki yöntemin tekrarı): `/json/new?about:blank` → 1 sekme → `Page.navigate` → `Runtime.evaluate` ile DOM okuma → sekme kapatıldı. Sekme listesi kontrol edildi; **admin'ın sekmelerine (caddyserver vb.) dokunulmadı**, kendi sekmemiz açılıp kapatıldı.
- URL şablonu: `https://www.google.com/search?q=<query>&num=20&hl=tr&gl=tr` (her tur 4 sn bekleme, turlar arası 2 sn).
- Organik linkler `a[href^="/goto"]` opak olduğu için hedef URL breadcrumb'tan (`cite`) okundu.
- Her sorguda 9–10 organik sonuç yakalandı; sınıflandırma organik/AI/tarih aşağıda.

## Sorgu sonuçları

### Q1 — `site:acm.org`

SERP: https://www.google.com/search?q=site%3Aacm.org&num=20&hl=tr&gl=tr

| # | Başlık | Hedef (breadcrumb) | Sınıf | Tarih |
|---|--------|--------------------|-------|-------|
| 1 | ACM Career & Job Center | jobs.acm.org | organik | — |
| 2 | ICER 2026 | icer2026.acm.org | organik | — |
| 3 | Distinguished Speaker Program | speakers.acm.org | organik | — |
| 4 | CHI 2015 \| Crossings | chi2015.acm.org | organik | — |
| 5 | PEARC Conference Series | pearc.acm.org | organik | — |
| 6 | ACM Interactions | interactions.acm.org | organik | — |
| 7 | ACM India Homepage | india.acm.org | organik | — |
| 8 | ACM CHI 2022 | chi2022.acm.org | organik | — |
| 9 | (Association for Computing Machinery) | acmweurope.acm.org | organik | — |
| 10 | CHI 2023 – Hamburg | chi2023.acm.org | organik | — |

Yorum: İlk sayfada **tek bir www.acm.org sayfası bile yok** — tüm sonuçlar alt alan adları. CHI 2015'in sıralanması, eski konferans sitelerinin temizlenmediğini gösteriyor. "ICER 2026" güncel ve ilgili (22. ACM ICER).

### Q2 — `"acm.org" news`

SERP: https://www.google.com/search?q=%22acm.org%22%20news&num=20&hl=tr&gl=tr

| # | Başlık | Hedef | Sınıf | Tarih |
|---|--------|-------|-------|-------|
| 1 | ACM News — IFIP News | ifipnews.org | organik (dış site, "acm.org" geçiyor) | 18 Ara 2025 |
| 2 | Computer Society News | dl.acm.org/doi | organik | 1 Eyl 1989 (yayın tarihi) |
| 3 | Computers and education | cacm.acm.org/co… | organik | — |
| 4 | Scientists Finish Decoding Last 8% of Human Genome | technews.acm.org | organik | — |
| 5 | News – Page 33 | cacm.acm.org/page | organik (derin arşiv) | — |
| 6 | News – Page 105 | cacm.acm.org/page | organik (derin arşiv) | — |
| 7 | ACM TechNews | technews.acm.org | organik | 5 May 2025 (arşiv) |
| 8 | News – Page 60 | cacm.acm.org/page | organik (derin arşiv) | — |
| 9 | News | acm.nl/news | organik (SAHTE EŞLEŞME — Hollanda tüketici otoritesi) | — |

Yorum: 1. sonuç IFIP News'in Ocak 2026'dan itibaren ACM DL'nin tümü açık erişime geçtiğini duyuran haberi — sitenin en büyük gündem maddesiyle çakışıyor (çakışan madde). CACM arşivinin Page 33/60/105 gibi derin sayfalarının sıralanması klasik pagination-SEO sorunu. `acm.nl` sonucunu Google'ın "acm.org" tam eşleşmesi olarak değil, içerik eşleşmesiyle karıştırdığı görülüyor.

### Q3 — `"acm.org" yeni OR announcement 2026`

SERP: https://www.google.com/search?q=%22acm.org%22%20yeni%20OR%20announcement%202026&num=20&hl=tr&gl=tr

| # | Başlık | Hedef | Sınıf | Tarih |
|---|--------|-------|-------|-------|
| 1 | Calendar | interactions.acm.org | organik | CI 2026: 27–30 Eyl 2026; RecSys '26 (20th) içinde |
| 2 | Call for Reproducibility Papers — ACM MM 2026 | 2026.acmmm.org | organik | — |
| 3 | TAAS Archive | dl.acm.org/loi/taas | organik | Eyl 2026 Sayı 3 (current), Haz 2026 Sayı 2, Mar 2026 Sayı 1 |
| 4 | Announcements | wordpress.sigweb.hosting.acm.org | organik | — |
| 5 | 📢 Call for Participation — ACM Creativity & Cognition | Facebook (Australasian Computer Music Association) | organik (sosyal gürültü) | ~1 yıl önce |
| 6 | ISEC 2026 — Call for Papers | acm.org/articles | organik | — |
| 7 | Newsletter May 2026 | acmweurope.acm.org | organik | May 2026 (başlıkta) |
| 8 | ACM's 2026 General Election | dl.acm.org/doi | organik | — |
| 9 | ACM 2026 General Election | cacm.acm.org/news | organik | **23 Nis 2026** |

Yorum: SERP'te görünen en yeni tarihli madde 23 Nis 2026 (seçim duyurusu) + TAAS Eyl 2026 sayısı. Temmuz–Kasım 2026'daki site haberleri (CEO, EiC atamaları, PQQS 2026) bu sorguda yok → **SERP/site zaman kayması** teyidi. MM 2026 ve RecSys '26 etkinlikleri #286 kapsamındaki etkinliklerle çakışır.

### Q4 — `acm.org blog`

SERP: https://www.google.com/search?q=acm.org%20blog&num=20&hl=tr&gl=tr

| # | Başlık | Hedef | Sınıf | Tarih |
|---|--------|-------|-------|-------|
| 1 | Welcome — Communications of the ACM | cacm.acm.org/wel… | organik | — |
| 2 | Communications of the ACM — Issue Library | mags.acm.org | organik | — |
| 3 | Magazine for HCI & design | interactions.acm.org | organik | — |
| 4 | (dizin listesi: "Name Last Modified Size Directory cgi-bin 2022-03-29…") | **blog.acm.org** | organik | snippet 2022-03-29 tarihli dizin |
| 5 | ACM CCS Blog | acmccs.github.io | organik | — |
| 6 | "Başlıksız" | blog.dietchapter.hosting.acm.org | organik | — |
| 7 | Blogs | mail.usar.hosting.acm.org | organik | — |
| 8 | July — October 2026 Calendar | interactions.acm.org | organik | — |
| 9 | Computing Crossroads | dl.acm.org/doi | organik | 27 Kas 2023 |

Yorum: ACM'nin "resmi blogu" diye bilinen `blog.acm.org` Google'da **WordPress dizin listesi** olarak indeksli (site muhtemelen kaldırılmış/boş; 2022-03-29 mtime). `blog.dietchapter.hosting.acm.org` başlığı bile alınmamış sayfa ("Başlıksız") indeksli.

## Siteyle çakışma kontrolü

Çapraz kontrol için aynı turda **kendi CDP sekmemle** `https://www.acm.org/` (ana sayfa, 12 başlık) ve `https://www.acm.org/media-center/acm-updates` (ilk 40 madde) çekildi (2026-11-06 ~06:58 UTC).

**Çakışan maddeler (SERP'te + sitede ikisi de var):**
- 2026 Genel Seçim: SERP Q3 (CACM news 23 Nis 2026, DL) ↔ site "2026 ACM General Election Results" (May 2026 bülten) — aynı olay, site sonuçları daha yeni.
- Tam açık erişim geçişi: SERP Q2 (IFIP News 18 Ara 2025; CACM "now fully Open Access" snippet'ları) ↔ site "A Message to the Computing Community About ACM's Transition to Full Open Access" + "ACM is Now Fully Open Access!".
- ISEC 2026 CFP: SERP Q3 (acm.org/articles) ↔ sitede /articles bülteni var (ilk 40'te görünmedi, listede aşağıda).
- Etkinlikler: SERP Q3/Q4 (MM 2026 CFP, RecSys '26 27–30 Eyl, CI 2026) → #286 (etkinlikler) raporuyla karşılaştırılacak.

**SERP'te, site temelinde olmayan / öne çıkmayan maddeler:**
- ICER 2026 — icer2026.acm.org (konferans sitesi; sitede ana sayfada yok).
- Distinguished Speaker Program — speakers.acm.org.
- TAAS (Trans. Architecture and Programming Systems) Eyl 2026 Sayı 3 — DL'de güncel sayı (→ #285 yayınlar kapsamına not).
- TechNews "Scientists Finish Decoding Last 8% of Human Genome" — technews.acm.org (tarih belirsiz, snippet'siz; taze mi eski mi doğrulanamadı).
- acmweurope Newsletter May 2026 — bölge bülteni.
- Eski/gürültü: CHI 2015/2022/2023 siteleri, CACM Page 33/60/105, 1989 Computer Society News, blog.acm.org dizin listesi, Facebook C&C ilanı, acm.nl (Hollanda otoritesi, sahte eşleşme).

**Sitede var ama bu SERP sorgularında çıkmayan (SERP gerisinde kalan) maddeler:**
- Alison Derbenwick Miller — ACM'nin yeni CEO'su (Temmuz 2026).
- PQQS 2026, 2–4 Kasım 2026 (bu hafta! site ana haberler arasında; Google'da bu sorgularda görünmüyor).
- 2026 dergi EiC/co-EiC atamaları (TOMACS, TAAI, TOMPECS, TECS, TALG, TOG, Games, IMWUT; ayrıca ACM AI Letters ilk sayısı).
- O'Reilly Library — Skills Bundle abonelerine (Eyl 2026 bülteni).
- 2027 ACM Asian School on HPC and AI başvuruları.

## Coğrafya / IP uyarısı

- Bu turda SERP arayüzü **Türkçe** ("Google'da Ara", "23 Nis 2026", "1 tepki · 1 yıl önce" formatları) — önceki aydinozturk.com turundaki (NL/NO/ET başlıklar) gözlemden farklı. Bununla birlikte çıkış IP'sinin TR-konut olduğunu kanıtlayan veri yok (Chrome host'unun çıkış IP'si değişken/ABD dışı olabilir); sonuçlar gerçek bir TR ev bağlantısından farklı sıralanabilir. "Yaklaşık N sonuç" ibaresi yine yok.
- Hiçbir sorguda AI Bakışı / AI Özeti kutusu oluşmadı; sosyal medya (Facebook) ve dış siteler (ifipnews.org, acm.nl) organik sonuçlar arasında normal sıralandı.

## Sınırlılıklar

- 4 sorgu × tek tur; sonuçlar turdan tura değişebilir (t280 gözlemi). Her sorgudan 9–10 organik madde alındı, 2. sayfa taranmadı.
- `/goto` opak linkleri nedeniyle hedef URL'ler breadcrumb'tan okundu; breadcrumb kırpılmışsa (örn. "cacm.acm.org › co…") tam URL alınamaz.
- TechNews "son %8 genom" maddesinin taze/ eski olduğu snippet'siz SERP'ten anlaşılamadı; site kontrolü #284/#285 kapsamına bırakıldı.
- "PQQS 2026 bu hafta" tespiti site temelinden; Google News aracı kullanılmadı.
