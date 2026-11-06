# Konsolide Rapor — acm.org'da ne yenisi var? (son ~2 hafta: 2026-10-23 → 2026-11-06)

- **Görev:** #288 (Plan #283 — admin [3877]: "acm.org a bak bakalım yeni ne var?")
- **Hazırlayan:** agent-6 · **Tarih:** 2026-11-06
- **Girdiler (değiştirilmedi, yalnızca konsolide edildi):**
  - `research/acm-org-update/news.md` — #284, agent-3 (haberler/duyurular; main'de, commit 54b0a12)
  - `research/acm-org-update/publications.md` — #285, agent-4 (yayınlar: CACM + dergiler; main'de, commit b28a0e6)
  - `research/acm-org-update/events-programs.md` — #286, agent-5 (etkinlikler/programlar/ödüller; commit 45d711a)
  - `research/acm-org-update/serp-crosscheck.md` — #287, agent-6 (Google SERP çapraz kontrolü; main'de, commit 707ea2a)
- **Dürüstlük çerçevesi:** Bu rapor **yeni gezinme/arama içermez**. Dört alt raporda ne yazıyorsa onu özetler; tüm alt bulgular 2026-11-06 06:45–07:00 UTC arasında **gerçek Chrome 156** (Windows host, CDP ucu `http://192.168.65.254:9222`) üzerinden alınmıştır. Alt raporlar arası tek tarih farkı (§3.3, TAAI) olduğu gibi işaretlenmiştir.

---

## 1. TL;DR — admin'in sorusuna 5 maddede cevap

1. **Pencerede (23 Eki–6 Kas) resmi duyuru akışı sakin: 1 net tarihli + 1 tarihsiz madde.** Net tarihli tek duyuru **5 Kasım 2026 ETPC webinar'ı** ("European Social Media Ban", webinar 4 Aralık'ta); tarihsiz madde **PQQS 2026** — SIGSAC'ın ilk post-kuantum güvenliği konferansı, **2–4 Kasım'da bu hafta San Jose'de**. En taze "medyada ACM" haberi 25 Eylül 2026 (pencere dışı). [Kaynak: #284 §TL;DR, §✅]
2. **Yayın tarafında en büyük yenilik: CACM Kasım 2026 sayısı (Vol. 69 No. 11).** 18 Features makalesi, ağırlıklı **yapay zeka** (The Techlash Is Back, AI'ın insan-bağımsızlık eşiği, rekürsif öz-iyileştirme, vibe coding, AI ekonomisi ajandası). Pencerede 8 yeni CACM makalesi çıktı; ayrıca **TQC'nin yeni EiC'si** (28 Eki) ve **TAAI** (yeni Agentic AI dergisi) atamaları. [Kaynak: #285 §1, §2]
3. **Etkinlik takvimi yoğun — en büyük dalga 15–20 Kasım 2026:** SC '26 (Supercomputing), SIGOPS ATC, CCS '26, ICAIF '26, HAI '26, VRST '26, HotNets '26 aynı haftaya yığılmış; Aralık'ta SIGGRAPH Asia, UCC, MUM, BDCAT ve ACM'nin **yeni "Compute '26" konferans serisi**. Ödül tarafında pencerede tarihli resmi duyuru yok; en taze **15 Ekim 2026 Ken Kennedy Award → Daniel Reed**. [Kaynak: #286 §1, §4]
4. **Yılın en büyük kurumsal haberi (bağlam): yeni CEO Alison Derbenwick Miller** (28 Tem 2026 ataması) + **tam açık erişim geçişi** (1 Oca 2026'dan itibaren tüm ACM dergileri/magazinleri OA) + başkan Elisa Bertino'nun DL-LLM eğitim tartışması (23 Tem 2026, anket hâlâ açık, karar yok). [Kaynak: #286 §5, #285 §2]
5. **Google'ın indeksi acm.org'un sitesine göre belirgin şekilde geride:** Temmuz–Kasım 2026 haberleri (yeni CEO, EiC atamaları, **bu hafta olan PQQS 2026**) SERP'te hiç çıkmıyor; `site:acm.org` ilk sayfasında **tek bir www.acm.org sayfası bile yok** (tümü alt alan adları, aralarında 11 yıllık CHI 2015 sitesi). Uyarı: Chrome çıkış IP'si **TR-konut değil** → Türkiye'deki bir kullanıcının SERP'i farklı sıralanabilir. [Kaynak: #287 §TL;DR, §Coğrafya]

---

## 2. Haberler / Duyurular özeti (#284, agent-3)

**Yapısal bulgu:** `acm.org/news` adresi artık **`acm.org/media-center`**'a (Medya Merkezi) yönlendiriyor. Tarihli duyurular **ACM Updates** (`/media-center/acm-updates`) alt sayfasında; medya haberleri **ACM in the News** (`/media-center/acm-in-the-news`) sayfasında.

**Pencere içinde (2026-10-23 → 2026-11-06):**

| Madde | Tarih | Özet |
|---|---|---|
| **ETPC Webinar: "European Social Media Ban"** | 5 Kas 2026 (sitede "Novmber 5" yazım hatası) | Avrupa'da çocukların sosyal medya erişim kısıtlamaları + DSA çerçevesi; sivil toplum ve çocuk hakları panelleri. Webinar'ın kendisi **4 Aralık 2026** (15:00 CET). [Kaynak: #284 §✅.1] |
| **PQQS 2026 — ilk Post-Quantum & Quantum-based Security Konferansı** | listede açık tarih satırı YOK (5 Kas ile 9 Eki maddeleri arasında) | SIGSAC'ın yeni yıllık platformu; kuantum/post-kuantum kriptografi + güvenli altyapı. Konuşmacılar: Turing ödüllüsü **Charles H. Bennett (IBM)**, Renato Renner (ETH), Dan Boneh (Stanford), Ryan Babbush (Google Quantum AI). **San Jose, 2–4 Kasım 2026** (konferans bu hafta). [Kaynak: #284 §✅.2] |

Bu iki madde dışında pencereye düşen net tarihli duyuru yok — **acm.org duyuru akışı bu 2 haftada gerçekten sınırlı içerik üretmiş** (#284'ün dürüst notu).

**Bağlam (pencere dışı, erken–orta Ekim):** 9 Eki "Global Technology Policy at ACM" webinar'ı (4 Kas'ta yapıldı) · 1 Eki TOMACS yeni Co-EiC'ler · 30 Eyl African Union AI Yönetişimi Açık Danışması yanıtı · 25 Eyl TAAI yeni Co-EiC'ler · (19 Eyl 2027 Asian School on HPC&AI başvuruları, 13 Eyl Heidelberg Laureate Forum özeti). [Kaynak: #284 §📅]

**Medyada ACM:** en taze madde **25 Eyl 2026** — "AI's Open Source Surge Recasts IT Services" (*Channel Dive*); pencere dışı. [Kaynak: #284 §📰]

---

## 3. Yayınlar — CACM ve dergi güncellemeleri (#285, agent-4)

### 3.1 CACM en son sayı: **Kasım 2026, Vol. 69 No. 11**

- Sayfa: <https://cacm.acm.org/issue/november-2026/>; ana sayfadaki "Latest Issue" bağlantısı bu sayıya işaret ediyor (1 Kasım dolaylarında yayımlandı).
- **18 Features makalesi**; sayının genel damgası **yapay zeka**: AI insan-bağımsızlık eşiği, rekürsif öz-iyileştirme, AI güvenliği ("Inside Risks" yeni dönemi), AI politikası (Senato), **vibe coding** ("Can VIBE Drive Development?"), AI'ın işgücü/ekonomi etkisi ("A Research Agenda for the Economics of Transformative AI" — Brynjolfsson/Korinek/Agrawal), "The Techlash Is Back" (Vardi). Tam tablo ve linkler #285 §1'de.
- Not: CACM'in gerçek alan adı `cacm.acm.org`; eski `communica.acm.org` DNS'te **NXDOMAIN** (çözüm yok). [Kaynak: #285 §1]

### 3.2 Pencerede (23 Eki → 6 Kas) çıkan yeni CACM makaleleri (8)

"AI Abundance or Luddite Revolution?" (Denning/Lewis/Gelenbe, 5 Kas, Opinion) · 4 BLOG@CACM yazısı (5–3 Kas) · "The Septuagint Effect" (Baquero, 3 Kas) · "The Techlash Is Back" (Vardi, 30 Eki) · "Can VIBE Drive Development?" (Mukhopadhyay, 30 Eki). [Kaynak: #285 §1.2]

### 3.3 Dergi tarafı (yeni atamalar ve dergiler)

- **28 Eki 2026 — TQC (Trans. on Quantum Computing) yeni EiC:** Min-Hsiu Hsieh (Hon Hai/Foxconn Quantum RC, Taipei); görev 1 Kas 2026 → 31 Eki 2029. Penceredeki tek yeni atama ilanı. [Kaynak: #285 §2]
- Bağlam: 1 Eki TOMACS (Liu/Strassburger/Szabo) · **TAAI (Trans. on Agentic AI) — yeni onaylanan dergi, ilk Co-EiC'leri Bang Liu & Yan Liu** (görev 1 Eki 2026 → 30 Eyl 2029). ⚠️ **Tarih farkı:** #285 ve #284 bu duyuruyu **25 Eylül** tarihli sayıyor, #286'nın program tablosu **25 Ekim** yazıyor; içerik (isimler, görev süresi) birebir aynı. Konsolide rapor bu çelişkiyi çözmeye çalışmaz — kaynak tarafı okunmamıştır. [Kaynak: #285 §2; #284 §📅; #286 §5]
- **Yeni dergiler:** en taze "ilk sayı" kaydı ACM AI Letters (27 Mar 2026); pencereye doğrudan giren yeni bir "ilk sayı" ilanı yok. [Kaynak: #285 §2]
- **Queue:** pencerede tek Queue makalesi Maria De-Arteaga, "How Does Generative AI Change the Algorithmic Fairness Problem?" (19 Eki — pencerenin hemen öncesinde). [Kaynak: #285 §2]

### 3.4 Yayın politikası (taze bağlam)

- **1 Oca 2026'dan itibaren tüm ACM dergileri ve magazinleri Open Access** (Bertino'nun OA mesajı 11 Kas 2025).
- **DL–LLM tartışması:** Başkan Elisa Bertino, Dijital Kütüphanenin LLM eğitimine açılması olasılığı için topluluk anketi topluyor (mesaj 23 Tem 2026, publications ana sayfasında hâlâ öne çıkarılmış; **karar verilmiş değil**). [Kaynak: #285 §2]

---

## 4. Etkinlikler, programlar, ödüller (#286, agent-5)

> Yapısal not: `acm.org/events` **404** — etkinlikler `/conferences/conference-events` (aylık takvim) ve `/chapters/local-activities` (bölüm etkinlikleri) altında; CFP deadline'ları `/conferences/upcoming-submission-deadlines`'ta.

### 4.1 Konferans takvimi (6 Kas → 5 Ara 2026)

- **Bu hafta (8 büyük etkinlik):** Koli Calling '26 (5–8), **CIKM '26** (7–11, Roma), ICCAD '26 (8–12), MM '26 (10–14), SIGCITE '26 (12–14), SIGCSE Virtual 2026 (12–15), ICAIF '26 (14–17), **SC '26** (15–20) başlangıcı.
- **En yoğun dalga 15–20 Kasım:** SC '26 (Supercomputing), SIGOPS ATC, **CCS '26** (SIGSAC güvenlik), ICAIF '26, HAI '26, VRST '26, HotNets '26, SoCC '26 aynı haftaya yığılmış.
- **Aralık:** **SIGGRAPH Asia 2026**, UCC '26, MUM '26, BDCAT '26 ve ACM'nin yeni serisi **Compute '26** (3–5 Ara).
- **Az önce kapananlar (1–5 Kas):** MICRO '26, **PQQS '26 (2–4 Kas, San Jose — SIGSAC'ın ilk yeni yıllık konferansı)**, CHI PLAY/UIST '26, SIGSPATIAL '26, EAAMO '26. Tam tablo #286 §1'de.
- Yerel/bölgesel (örnek, 6–8 Kas): GreekCHI-CYCHI Symposium (Kıbrıs/Yunanistan), CCF ChinaSoft etkinlikleri, Princeton CS Contest, WISE 2026 (Venedik), Fall 2026 ACM Banquet (Cleveland). [Kaynak: #286 §1–§2]

### 4.2 CFP / başvuru deadline'ları (seçili)

- **Kasım 2026:** PLDI '27 (15 Kas), WSDM '27 + DAC '27 (17 Kas), ISCA '27 (26 Kas), STOC '27 (2 Kas, site henüz yok).
- **Aralık 2026:** CODASPY '27 (1 Ara), Middleware '27 (3 Ara), MobiSys '27 (5 Ara), WebSci '27 (15 Ara).
- **Ocak 2027 (yıl sonu yoğunluğu):** 14+ konferansın CFP'si 1 Ocak'ta; FAccT '27 (14 Oca), **SIGGRAPH '27** (28 Oca), **SIGCOMM '27** (31 Oca), CSCW '27 (24 Oca), SPLASH '27 (4 Oca). Bazı linkler ACM'nin kendi listesinde "not available yet / under construction". [Kaynak: #286 §3]

### 4.3 Ödüller

- **Pencerede (23 Eki–6 Kas) tarihli resmi ödül duyurusu YOK.** En taze: **15 Ekim 2026 — 2026 ACM-IEEE CS Ken Kennedy Award → Daniel Reed** (Univ. of Utah; paralel/HPC öncülüğü; basın bülteni `media-center/2026/october/kennedy-award-2026`).
- 9 Eyl: 2026 George Michael Memorial HPC Fellowship kazananları (Jie Ren, Amit Samanta, Xuan Wu + mansiyon Yankai Jiang) — tören **SC26**'da (15–20 Kas).
- 2026 döngüsü (duyuru tarihleri birebir sayfalarda görünmüyor, tarihsiz): Eckert-Mauchly → Srinivas Devadas (MIT); Doctoral Dissertation → Allen Liu (MIT); Athena → Monika Henzinger; **Kanellakis → Erdal Arıkan (Bilkent, polar kodlar)**; Newell → Kevin Leyton-Brown; **Grace Hopper → Ben Mildenhall & Pratul Srinivasan (NeRF)**; Karlstrom → Yasmin Kafai & Mitchel Resnick; Policy → Ed Felten. 2025 büyük ödülleri liste üstte: **Turing 2025 → Bennett & Brassard**; **Prize in Computing 2025 → Matei Zaharia**. [Kaynak: #286 §4]

### 4.4 Program / üyelik haberleri

- **2027 ACM Asian School on HPC and AI** — 1–5 Mar 2027 Singapur (SupercomputingAsia ile birlikte); başvuru deadline'ı **31 Eki 2026 AoE'de yeni kapandı**.
- **Yeni CEO (bağlam):** 28 Tem 2026 — Alison Derbenwick Miller, CEO & Executive Director (basın bülteni `2026/july/acm-names-new-ceo-2026`).
- 30 Ağu: Inaugural ACM AI Leadership Summit duyurusu (LeCun, Barto konuşmacılar arasında).
- Üyelik: **1 Eyl 2026**'dan Skills Bundle abonelerine tam O'Reilly kütüphanesi; Student Research Competition (src.acm.org); Call for Proposals: ACM Books. [Kaynak: #286 §5]

---

## 5. Google SERP çapraz kontrolü + coğrafya uyarısı (#287, agent-6)

4 Google sorgusu (`site:acm.org` · `"acm.org" news` · `"acm.org" yeni OR announcement 2026` · `acm.org blog`), `hl=tr&gl=tr`, her tur 9–10 organik sonuç; aynı turda kendi CDP sekmesiyle site basline'ı (ana sayfa + media-center/acm-updates) çekilip çakışma kontrolü yapıldı. CAPTCHA/consent yok; bu turlarda **AI Özeti kutusu hiç oluşmadı**. Tam tablolar #287 §Sorgu sonuçları'nda.

**Ana bulgular:**

1. **Google indeksi siteye göre geride (zaman kayması).** SERP'te görünen en yeni tarihli madde 23 Nis 2026 (Genel Seçim). Temmuz–Kasım 2026'daki site haberleri — yeni CEO, dergi EiC atamaları, O'Reilly bülteni ve **bu hafta (2–4 Kas) olan PQQS 2026** — hiçbir sorguda çıkmıyor.
2. **`site:acm.org` ilk sayfasında www.acm.org sayfası YOK.** 10/10 sonuç alt alan adı (jobs, icer2026, speakers, pearc, interactions, india, chi2015/2022/2023, acmweurope) — en eskisi ~11 yıllık CHI 2015.
3. **SEO tuhaflıkları:** CACM haber arşivinin derin sayfa numaraları (Page 33/60/105) sıralanıyor (pagination sorunu); `blog.acm.org` Google'da **ham dizin listesi** olarak indeksli (2022 mtime; site muhtemelen kaldırılmış); bir WordPress hosting alt alanı ("Başlıksız") başlıksız indeksli; `acm.nl` (Hollanda tüketici otoritesi) "acm.org" tam eşleşmesiyle karışmış.
4. **SERP'te site ana yüzeyinde olmayan maddeler:** ICER 2026 (icer2026.acm.org), TAAS Eyl 2026 Sayı 3 (DL), MM '26 CFP / RecSys '26 / CI 2026 tarihleri (#286 ile çakışıyor), TechNews "son %8 genom" haberi (taze/esi doğrulanamadı).

**🌍 Çıkış IP coğrafya uyarısı:** Bu turda SERP arayüzü **Türkçe** görünmüştü (önceki aydinozturk.com turunda NL/NO/ET başlıkları vardı) — yani Chrome'un çıkış IP'si **değişken**; ama çıkış IP'sinin TR-konut olduğunu kanıtlayan veri hâlâ yok. Türkiye'deki gerçek bir ev bağlantısından farklı sıralama/sonuç **mümkün**. "Yaklaşık N sonuç" ibaresi de yok.

---

## 6. Sınırlılıklar (toplu)

- **Cloudflare 403:** acm.org'a doğrudan `curl`/istemci 403 döndürdüğü için tüm dört alt rapor **gerçek Chrome 156 üzerinden ham CDP** (`http://192.168.65.254:9222`, Windows host) ile gezildi; her agent kendi sekmesini açıp kapattı, admin sekmelerine (caddyserver) dokunulmadı. CAPTCHA'ya takılan sayfa yok; cookie banner'ları içeriği engellemedi.
- **Çıkış IP'si TR-konut değil:** Chrome host'u değişken/ABD dışı bir çıkış IP'sinden gidiyor. acm.org coğrafi kişiselleştirme yapmadığından **site içeriğini etkilemez** (#286 notu); ancak **Google SERP sıralamasını etkileyebilir** (§5 uyarısı). TR kullanıcısı için kesin kanal hâlâ site sahibinin kendi GSC/SERP kontrolüdür.
- **Tarih belirsizlikleri:** (a) PQQS 2026 maddesi media-center listesinde açık tarih satırı taşımıyor — tarih listenin en-yeni-ilk sıralamasından çıkarıldı (5 Kas ile 9 Eki arası); konferans tarihi (2–4 Kas) konferans sitesinden net. (b) Sitede "Novmber 5, 2026" yazım hatası (ETPC). (c) TAAI Co-EiC duyuru tarihi alt raporlar arasında farklı: 25 Eyl (#284/#285) vs. 25 Eki (#286) — içerik aynı, çelişki olduğu gibi aktarıldı. (d) 2026 döngüsü ödül duyuru tarihleri awards.acm.org birebir sayfalarda görünmüyor (tarihsiz listelendi). (e) TechNews "son %8 genom" maddesi snippet'siz SERP'te — taze/esi doğrulanamadı.
- **Kapsam:** bu rapor yeni gezinme/arama yapmaz; yalnızca 4 alt raporun konsolidasyonudur. Google tarafı 4 sorgu × tek tur (sonuçlar turdan tura değişebilir; 2. sayfa taranmadı). `/blogs` ve `/podcasts` sayfaları #284'te incelenmedi (içerik Media Center'da toplu). Yerel etkinlik takvimi yüzlerce madde içeriyor; #286'da yalnızca 6–8 Kas diliminden örnek verildi.
- **Pencere darlığı:** acm.org'un resmi duyuru akışı 23 Eki–6 Kas arasında az içerik ürettiği için her alt rapor, "ne yenisi var?" sorusunu tam cevaplamak amacıyla erken/orta Ekim bağlam maddelerini **ayrı sınıflandırarak** ekledi (pencere içi ↔ bağlam ayrımı korunmuştur).

---

## 7. Kaynaklar

### 7.1 Gezilen URL'ler (alt raporlara göre)

**#284 — Haberler/duyurular (agent-3):**
1. `https://www.acm.org/news` → 301 → `https://www.acm.org/media-center` (Medya Merkezi)
2. `https://www.acm.org/media-center` (ana sayfa)
3. `https://www.acm.org/media-center/acm-updates` (ana haber kaynağı, tarihli liste)
4. `https://www.acm.org/media-center/acm-in-the-news` (medya haberleri)
5. İçerik linkleri: `https://acm-pqqs.github.io/pqqs2026/`, `https://dl.acm.org/journal/tomacs`, `https://dl.acm.org/journal/taai`, `https://www.acm.org/public-policy/er-tpc/african-open-consultation-ai-governance-regulation-10052026`, 2 Zoom webinar linki (events.zoom.us)

**#285 — Yayınlar (agent-4):**
6. `https://www.acm.org/publications` (hub + "ACM Welcomes New EICs" + LLM/OA blokları)
7. `https://www.acm.org/publications/journals` · `https://www.acm.org/publications/magazines` · `https://www.acm.org/publications/new-journals`
8. `https://www.acm.org/publications/message-to-the-community` (OA mesajı, 11 Kas 2025)
9. `https://www.acm.org/about-acm/acm-pres-on-llms-and-the-dl` (LLM/DL mesajı, 23 Tem 2026)
10. `https://cacm.acm.org/` · `https://cacm.acm.org/issue/november-2026/` (Kasım 2026 TOC) · `https://queue.acm.org/`
11. `https://www.communica.acm.org` / `https://communica.acm.org` — DNS NXDOMAIN (eski alan adı)
12. `https://www.acm.org/cacm` (CACM kısayolu)

**#286 — Etkinlikler/programlar/ödüller (agent-5):**
13. `https://www.acm.org/events` → **404** · `https://www.acm.org/` (ana sayfa)
14. `https://www.acm.org/conferences/conference-events` (aylık etkinlik takvimi, 1 Kas–5 Ara görünümü)
15. `https://www.acm.org/conferences/upcoming-submission-deadlines` (+ `?startDate0=20261201`, `?startDate0=20270101`)
16. `https://www.acm.org/chapters/local-activities` (bölüm etkinlikleri)
17. `https://awards.acm.org/` + birebir ödül sayfaları: `/kennedy`, `/about/2025-turing`, `/about/2025-acm-prize`, `/hpc-fellows`, `/eckert-mauchly`, `/doctoral-dissertation`, `/athena`, `/kanellakis`
18. `https://www.acm.org/membership` (üyelik + program duyuruları)
19. CFP/etkinlik dış linkleri: `https://pldi27.sigplan.org/`, `https://wsdm-conference.org/2027/`, `https://idc.acm.org/2027`, `https://iscaconf.org/isca2027/`, `https://s2027.siggraph.org/`, `https://www.sigcomm.org/events/sigcomm-conference` vb.; `https://europe.acm.org/seasonal-schools/asean/2027` (Asian School 2027), `http://src.acm.org/` (Student Research Competition)

**#287 — SERP çakışma kontrolü için site basline'ı (agent-6):**
20. `https://www.acm.org/` (ana sayfa, 12 başlık) + `https://www.acm.org/media-center/acm-updates` (ilk 40 madde), 2026-11-06 ~06:58 UTC

### 7.2 Google SERP URL'leri (#287, 4 sorgu)

- `https://www.google.com/search?q=site%3Aacm.org&num=20&hl=tr&gl=tr`
- `https://www.google.com/search?q=%22acm.org%22%20news&num=20&hl=tr&gl=tr`
- `https://www.google.com/search?q=%22acm.org%22%20yeni%20OR%20announcement%202026&num=20&hl=tr&gl=tr`
- `https://www.google.com/search?q=acm.org%20blog&num=20&hl=tr&gl=tr`

### 7.3 Alt raporlar

- `research/acm-org-update/news.md` (#284) · `research/acm-org-update/publications.md` (#285) · `research/acm-org-update/events-programs.md` (#286) · `research/acm-org-update/serp-crosscheck.md` (#287)
