# İndekslenme ve Görünürlük Sinyalleri — aydinozturk.com

- **Görev:** #267 (Plan #265 — "Bu kişinin Google'da arama sonuçlarıyla ilgili bir şey var mı?")
- **Tarih:** 2026-11-05 (tüm istekler bu tarihte, bu ortamdan gönderildi)
- **Kapsam:** Site arama motorlarında indekslenmeye ne kadar açık/uygun görünüyor? Nesnel sinyaller: robots.txt + Content-Signals, sitemap, CommonCrawl, Wayback Machine, sosyal profiller.
- **Metot:** `curl` (tarayıcı UA ile) + CommonCrawl index API + Wayback CDX API. Google/Bing indeksine bu ortamdan doğrudan erişim yok (bkz. #265, #266).

## 0. Sinyal özeti

| # | Sinyal | Değer | Kaynak (URL + metot) |
|---|--------|-------|----------------------|
| 1 | robots.txt — normal arama botlarına izin | **Açık** (`User-agent: * → Allow: /`, `Content-Signal: search=yes,ai-train=no,use=reference`) | `https://aydinozturk.com/robots.txt` (curl, HTTP 200) |
| 2 | robots.txt — AI eğitim botları | **Engelli** (31 bot `Disallow: /`, aralarında CCBot, GPTBot, ClaudeBot, Google-Extended) | aynı URL |
| 3 | Sitemap | **Yayında** — 1 alt sitemap, **18 URL**, `<lastmod>` yok | `https://aydinozturk.com/sitemap-index.xml` → `sitemap-0.xml` (curl, HTTP 200) |
| 4 | CommonCrawl varlığı (Eki 2019 → Eki 2026, 13 crawl) | **YOK** — "No Captures found" (kesin, HTTP 404 + JSON mesajı) | `https://index.commoncrawl.org/<ID>-index?url=aydinozturk.com*&output=json` (curl) |
| 5 | Wayback Machine capture geçmişi | **106 capture**, 2005 → 2021; 2022-2024 ve 2026'da **sıfır** yeni capture; 2025'te 1 `warc/revisit` (eski içerik işaretçisi) | `http://web.archive.org/cdx/search/cdx?url=aydinozturk.com&matchType=domain&output=json&fl=timestamp,original,statuscode,mimetype&limit=10000` (curl) |
| 6 | Sosyal profil: LinkedIn | **Erişilebilir, gerçek profil** — HTTP 200, başlık "Aydın Öztürk - UZMAR Technology \| LinkedIn" | `https://www.linkedin.com/in/aydinozturk` (curl, tarayıcı UA) |
| 7 | Diğer sosyal profiller (X, GitHub, Facebook, Instagram, YouTube, Medium) | **Sitede link yok** | ana sayfa HTML'i `https://aydinozturk.com/` (curl, HTTP 200) |

> **⚠️ Ayrık not (yorumlamada kritik):** *"CommonCrawl'de yok" ≠ "Google'da indeksli değil."* CommonCrawl'ın botu (CCBot) robots.txt ile **bilinçli olarak engellenmiş** (`User-agent: CCBot → Disallow: /`, Cloudflare yönetilen bölüm); bu yüzden siteden CC'ye hiç veri akışı olmaması beklenen bir durum ve indeks sinyali olarak yorumlanmamalı. Öte yandan `Content-Signal: search=yes` + `Allow: /` sitenin **Google/Bing normal arama crawler'larına açık** olduğunu, 18 URL'lik yayın sitemap'inin de indekslenmeyi kolaylaştırdığını gösteriyor. Yani site, indekslenmeye karşı **tamamen izin verici** bir yapıya sahip; "indeksli mi?" sorusunun kendisi ise ancak arama motorunun kendi indeksinden (bkz. #266: Bing `site:aydinozturk.com` → 0 sayfa) yanıtlanabilir.

## 1. robots.txt ve Content-Signals

Kaynak: `https://aydinozturk.com/robots.txt` — 2026-11-05, curl + tarayıcı UA, **HTTP 200**, ~3 KB.

Yapı: **Cloudflare yönetilen (managed) robots.txt** (dosyanın içinde "BEGIN/END Cloudflare Managed content" işaretleri var).

| Blok | Kural | Anlam |
|------|-------|-------|
| `User-agent: *` | `Content-Signal: search=yes,ai-train=no,use=reference` + `Allow: /` | **Arama indekslemeye açık** (arama sonuçları için içerik toplanabilir); **AI eğitimine kapalı** (içerik model eğitimi/fine-tuning için kullanılamaz); kullanım tipi "reference". EU 2019/790 m.4 hak saklaması notu içerir. |
| 31 özel bot | `Disallow: /` | Engellenenler: Amazonbot, Applebot-Extended, Bytespider, **CCBot**, ClaudeBot, Diffbot, **Google-Extended**, **GPTBot**, omgili, anthropic-ai, Claude-Web, cohere-ai, MistralAI-Training, meta-externalagent, GoogleOther, Baiduspider, PetalBot, AwarioSmartBot, AwarioRssBot, Google-CloudVertexBot, QualifiedBot, Cotoyogi, ICC-Crawler, atlassian-bot, FishBot, BorderxBot, NavuBot, SemrushBot-SWA, WARDBot, magpie-crawler, KimiBot, CitibotSiteCrawler |
| Son `User-agent: *` | `Allow: /` + `Sitemap: https://aydinozturk.com/sitemap-index.xml` | Genel izin tekrar; sitemap adresi resmi olarak duyurulmuş. |

**Yorum:** Googlebot ve Bingbot gibi *normal arama* crawler'larına kısıtlama yok (liste yalnızca AI eğitim/RAG botlarını kapsar). `Google-Extended` (AI arama/RAG) ve `GoogleOther` engellidir; `google.com`'ın ana indeks crawler'ı (Googlebot) izinlidir. Yorum: site sahibi "aramada görün, ama AI'a eğitme" seçeneğini bilinçli olarak seçmiş. *(Kaynak: robots.txt içeriği, yukarıdaki URL)*

## 2. Sitemap

- `https://aydinozturk.com/sitemap-index.xml` — curl, **HTTP 200**: `<sitemapindex>` içinde **1** alt sitemap: `https://aydinozturk.com/sitemap-0.xml`
- `https://aydinozturk.com/sitemap-0.xml` — curl, **HTTP 200**: **18 `<url>`, `<lastmod>` alanı yok.**

18 URL (tam liste):

```
https://aydinozturk.com/
https://aydinozturk.com/case-studies/camera-based-production-tracking/
https://aydinozturk.com/case-studies/llm-agents-on-a-legacy-erp/
https://aydinozturk.com/case-studies/rebuild-or-integrate/
https://aydinozturk.com/case-studies/shipyard-erp-turnaround/
https://aydinozturk.com/case-studies/talking-to-an-erp/
https://aydinozturk.com/case-studies/vessel-telemetry-platform/
https://aydinozturk.com/driveinsight/privacy/
https://aydinozturk.com/tr/
https://aydinozturk.com/tr/driveinsight/gizlilik/
https://aydinozturk.com/tr/projeler/erp-ile-konusmak/
https://aydinozturk.com/tr/projeler/gemi-telemetri-platformu/
https://aydinozturk.com/tr/projeler/kamera-tabanli-uretim-takibi/
https://aydinozturk.com/tr/projeler/llm-agentlari-ve-eski-kod/
https://aydinozturk.com/tr/projeler/tersane-erp-donusumu/
https://aydinozturk.com/tr/projeler/yeniden-yazmak-mi-entegre-olmak-mi/
https://aydinozturk.com/tr/zapp/gizlilik/
https://aydinozturk.com/zapp/privacy/
```

Yapı: 2 dil (EN kök + `/tr/`), 6 İngilizce vaka + 5 Türkçe vaka, 4 gizlilik sayfası, 2 dil kökü. Sitemap, ana sayfada da `href="/sitemap-index.xml"` olarak linklenmiş. *(Kaynak: ana sayfa HTML'i + sitemap XML'leri, yukarıdaki URL'ler)*

## 3. CommonCrawl

**Soru:** Site CommonCrawl indeksinde hiç yakalandı mı?
**Metot:** `https://index.commoncrawl.org/<ID>-index?url=aydinozturk.com*&output=json` (curl; 504/502 gelenler 3-4 kez tekrar denendi; indeks kimlikleri `collinfo.json`'dan).

**Sonuç: 13 crawl'da kesin "No Captures found"** (API yanıtı HTTP 404 + `{"message": "No Captures found for: aydinozturk.com"}`):

| Crawl (ID) | Crawl aralığı | Sonuç |
|---|---|---|
| CC-MAIN-2019-43 | 2019-10-13 → 24 | YOK |
| CC-MAIN-2020-40 | 2020-09-18 → 10-02 | YOK |
| CC-MAIN-2021-43 | 2021-10-15 → 28 | YOK |
| CC-MAIN-2022-40 | 2022-09-24 → 10-08 | YOK |
| CC-MAIN-2023-40 | 2023-09-21 → 10-05 | YOK |
| CC-MAIN-2024-46 | 2024-11-01 → 15 | YOK |
| CC-MAIN-2025-51 | 2025-12-04 → 17 | YOK |
| CC-MAIN-2026-04 | 2026-01-12 → 25 | YOK |
| CC-MAIN-2026-12 | 2026-03-05 → 17 | YOK |
| CC-MAIN-2026-17 | 2026-04-10 → 23 | YOK |
| CC-MAIN-2026-21 | 2026-05-08 → 21 | YOK |
| CC-MAIN-2026-39 | 2026-09-04 → 17 | YOK |
| CC-MAIN-2026-43 (en güncel) | 2026-10-05 → 18 | YOK |

Belirsiz kalan (504 Gateway Timeout, tekrarlı): CC-MAIN-2026-25 (Haz 2026), 2026-30 (Tem 2026), 2026-34 (Ağu 2026) — bu üçü için hüküm verilemez; ancak ayda 2 crawl sıklığıyla, 2026'nın geri kalan tüm crawl'ları + Aralık 2025 + 2019-2024 yıllarının tamamında yokluk, güçlü ve tutarlı bir örüntü.

**Yorum:** Bu yokluk, robots.txt'teki `CCBot → Disallow: /` kuralının sonucu — CCBot robots'a uyduğu için siteyi hiç crawl'lamıyor. Dolayısıyla CC verisi **olumsuz indeks sinyali taşımaz** (bkz. §0 ayrık not). *(Kaynak: CommonCrawl index API yanıtları + robots.txt §1)*

## 4. Wayback Machine (Internet Archive)

**Metot:** CDX API — `http://web.archive.org/cdx/search/cdx?url=aydinozturk.com&matchType=domain&output=json&fl=timestamp,original,statuscode,mimetype&limit=10000` (curl, 2026-11-05). Alan adı tüm alt yollarıyla sorgulandı.

**Toplam: 106 ham capture. Yıl bazında:**

| Yıl | Capture | Not |
|---|---|---|
| 2005 | 5 | **Yalnız `/robots.txt`** (2005-09-05 → 2005-11-07, mimetype "unk", 200). Ana sayfa capture'ı yok. |
| 2010 | 1 | Ana sayfa 200 (2010-03-23, `www.aydinozturk.com`) — ilk sayfa capture'ı. |
| 2011 | 6 | Ana sayfa ×3 (200) + robots.txt 404 ×2 + favicon 404 |
| 2012 | 13 | |
| 2013 | 5 | |
| 2014 | 11 | |
| 2015 | 10 | |
| 2016 | 11 | Bir capture `warc/revisit` |
| 2017 | 6 | |
| 2018 | 21 | En yoğun yıl; 3'ü `warc/revisit` |
| 2019 | 12 | |
| 2020 | **0** | Boşluk |
| 2021 | 4 | Sonuncusu 2021-11-25 (ana sayfa, 200) |
| 2022 | **0** | Boşluk |
| 2023 | **0** | Boşluk |
| 2024 | **0** | Boşluk |
| 2025 | 1 | **`warc/revisit`** (2025-07-10, status "-") — yeni içerik değil, eski bir payload'a işaretçi |
| 2026 | **0** | (sorgu tarihi itibarıyla) |

**Yorum:**
- Alan adının Web arşivindeki izi 2005'e (robots.txt) ve 2010'a (ilk ana sayfa) dayanıyor — `domain-history.md` (#263) ile tutarlı.
- 2010-2021 arası düzenli (küçük/kişisel site ölçeğinde) capture var; 2022'den itibaren **yeni hiçbir capture yok**. 2025 tek kaydı bir revisit işaretçisi, gerçek içerik snapshot'ı değil.
- Wayback Machine robots.txt'e kısmen uyan bir crawler ağıdır (SPN kaynaklı capture'lar dahil) — 2022-2026 sıfırı, sitenin IA tarafından "crawl edilemeye değer" bulunmadığına (ya da erişiminin engellendiğine) işaret eder, **Google indeks sinyali değildir**.
- Pratik sonuç: Wayback'te güncel sitenin (vaka sayfalı hâli) arşivlenmiş bir görüntüsü bulunmuyor; en son gerçek ana sayfa capture'ı 2021-11-25. *(Kaynak: CDX API, yukarıdaki URL)*

## 5. Sosyal profiller

Siteden çıkan **tek dış sosyal link** LinkedIn; ana sayfanın `Person` şemasındaki `sameAs` listesi de aynı URL'i içeriyor. *(Kaynak: `https://aydinozturk.com/` ana sayfa HTML'i — `<a href="https://www.linkedin.com/in/aydinozturk">` ve `<script type="application/ld+json">` `sameAs` alanı, 2026-11-05 curl)*

| Profil | URL | Kontrol | Sonuç |
|---|---|---|---|
| LinkedIn | `https://www.linkedin.com/in/aydinozturk` | curl + tarayıcı UA, `-L`, 2026-11-05 | **HTTP 200**, 746 KB tam sayfa; `<title>Aydın Öztürk - UZMAR Technology \| LinkedIn` → **gerçek, açık (public) profil**, bot'a kapalı değil. İsim eşleşiyor; "UZMAR Technology" unvanı sitenin About bölümündeki danışmanlık kimliğiyle uyumlu. |
| X/Twitter, GitHub, Facebook, Instagram, YouTube, Medium | — | Ana sayfa HTML taraması (tüm `href`'ler listelendi) | **Hiçbiri sitede linklenmemiş.** |

E-posta: `mailto:hello@aydinozturk.com` (sosyal profil değil; erişim kanalı). *(Kaynak: ana sayfa HTML'i)*

## 6. Sınırlılıklar

1. Google indeksinin kendisine bu ortamdan erişim yok (JS challenge); "indeksli mi?" sorusuna yanıt #266 (Bing best-effort: `site:aydinozturk.com` → 0 sayfa) ve bu rapordaki *izin* sinyalleriyle birlikte değerlendirilmeli.
2. CommonCrawl'da 3 crawl (2026-25/30/34) 504 ile belirsiz kaldı (tekrarlı denemeye rağmen); hüküm 13 kesin crawl'a dayanıyor.
3. Wayback `warc/revisit` kayıtları yeni içerik sayılmadı; 2005 kayıtları yalnız robots.txt (mimetype "unk").
4. LinkedIn sayfası yalnız HTTP durumu + başlık düzeyinde doğrulandı (profil içeriğinin tamamı analiz edilmedi; gerek de olmadı).
5. Tüm HTTP kontrolleri 2026-11-05, tek oturumda yapıldı.

## 7. Kaynaklar ve yöntemler (özet)

| Kaynak | URL | Metot |
|---|---|---|
| robots.txt | `https://aydinozturk.com/robots.txt` | curl (tarayıcı UA), HTTP 200 |
| Sitemap index / alt | `https://aydinozturk.com/sitemap-index.xml`, `.../sitemap-0.xml` | curl, HTTP 200, XML parse |
| CommonCrawl index API | `https://index.commoncrawl.org/<ID>-index?url=aydinozturk.com*&output=json` | curl; indeks listesi `https://index.commoncrawl.org/collinfo.json` |
| Wayback CDX | `http://web.archive.org/cdx/search/cdx?url=aydinozturk.com&matchType=domain&output=json&fl=timestamp,original,statuscode,mimetype&limit=10000` | curl (ilk deneme 503, ikinci 200) |
| Ana sayfa | `https://aydinozturk.com/` | curl (tarayıcı UA), HTTP 200, link/şema taraması |
| LinkedIn | `https://www.linkedin.com/in/aydinozturk` | curl (tarayıcı UA, `-L`), HTTP 200 |
