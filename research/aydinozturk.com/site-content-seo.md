# İçerik ve SEO Analizi: aydinozturk.com

**Görev:** #262 · **Analiz tarihi:** 2026-11-05 · **Yazar:** agent-4

## Yöntem

Site içeriği 2026-11-05 tarihinde doğrudan HTTP istekleriyle (curl, tarayıcı User-Agent) çekildi; analiz, elde edilen HTML üzerinde yapıldı. Erişilen kaynaklar:

| Kaynak | Durum |
|---|---|
| `https://aydinozturk.com/` (ana sayfa, ~23,7 KB) | 200 |
| `https://aydinozturk.com/tr/` (Türkçe ana sayfa, ~24,8 KB) | 200 |
| 6 vaka çalışması: `/case-studies/{shipyard-erp-turnaround, camera-based-production-tracking, llm-agents-on-a-legacy-erp, rebuild-or-integrate, talking-to-an-erp, vessel-telemetry-platform}/` | 200 |
| 1 Türkçe vaka: `/tr/projeler/llm-agentlari-ve-eski-kod/` | 200 |
| `https://aydinozturk.com/robots.txt` | 200 |
| `https://aydinozturk.com/sitemap-index.xml` → `sitemap-0.xml` | 200 |
| `https://aydinozturk.com/sitemap.xml` | **404** (gerçek sitemap `sitemap-index.xml`) |
| `https://aydinozturk.com/og.png` (HEAD) | 200, `image/png` |
| Yetim sayfalar: `/driveinsight/privacy/`, `/zapp/privacy/`, `/tr/zapp/gizlilik/` | 200 |

> Not: `robots.txt` "Content-Signal: search=yes, ai-train=no" ile yalnızca aramaya izin veriyor ve AI eğitim botlarını engelliyor. Bu analiz, site yöneticisinin doğrudan talebiyle yapılan tekil erişim üzerinden derlenmiştir; içerik toplanması/treni amacıyla kullanılmamıştır.

---

## 1. Sitenin amacı ve hedef kitlesi

Sait, **kişisel profesyonel (personal-brand) sitesi**dir: "Aydın Öztürk — Systems Architect for Shipyards & Fleets". H1 ("Systems that hold up where ships are built") ve About bölümü, sahibinin **yazılım geliştirme müdürü ve sistem mimarı** olduğunu; gemi inşa ERP platformu, filo telemetrisi ve endüstriyel AI sistemleri üzerinde 10+ yıl deneyimle, 10 kişilik bir ekip yönettiğini anlatıyor. *(Kaynak: ana sayfa `<h1>`, "About" bölümü, `JSON-LD @type: Person`)*

**Hedef kitle:** tersaneler, filo operatörleri, proje bazlı imalat firmaları; ERP/endüstriyel IoT/uygulamalı AI konusunda teknik karar veren kişiler. Sayfa sonu "Open to: Selected consulting conversations" — yani site asıl olarak **seçici danışmanlık** ve profesyonel ağ (LinkedIn bağlantılı) amaçlıdır. *(Kaynak: ana sayfa About tablosu ve Contact bölümü)*

Ek olarak, henüz "In development" aşamasında bir girişim tanıtılıyor: **DriveInsight** — kamera + CAD + ERP verisinden denetlenebilir üretim ilerleme ölçümü. *(Kaynak: ana sayfa "Venture · In development" bölümü)*

## 2. Sayfa ve içerik haritası

Sitemap (`sitemap-0.xml`) toplam **17 URL** içeriyor:

- EN ana sayfa + TR ana sayfa (`/`, `/tr/`) — karşılıklı hreflang'lı
- 6 EN vaka çalışması (`/case-studies/…`) + 6 TR karşılığı (`/tr/projeler/…`)
- 4 gizlilik sayfası: `/driveinsight/privacy/`, `/tr/driveinsight/gizlilik/`, `/zapp/privacy/`, `/tr/zapp/gizlilik/` — **sitenin hiçbir yerinden linklenmiyor** (bkz. §8.1)

**İçerik hacmi (görünür metin, kelime):** ana sayfa EN ≈ 1.090, TR ≈ 1.020; vaka çalışmaları 315–509 kelime arası (en uzun: shipyard-erp-turnaround ≈ 509). *(Kaynak: çekilen HTML'lerin script/style hariç metin sayımı, 2026-11-05)*

## 3. İçerik kalitesi ve Türkçe kullanımı

**Kalite yüksek.** İçerik jenerik "web sitesi şablonu" dilinden uzak, somut ve ölçülebilir: "200+ vessel projects", "26+ vessels streaming telemetry", "12+ ERP modules", "10 engineers". Vakalar `CS-01`…`CS-06` numaralı, etiketli (alan + durum: "Proof of concept", "In daily use", "In production") ve **Context → Problem → Approach → Outcome** şablonuyla yazılmış. Örnek (CS-02, LLM agent on legacy ERP): "Committing, pushing, and opening the pull request are handled deterministically by the server, on an isolated per-task branch in its own git worktree" — teknik olarak tutarlı, abartısız. *(Kaynak: çekilen vaka sayfası HTML'leri)*

**Türkçe çeviri sadık ve doğal** — makine çevirisi kokusu yok; terminoloji tutarlı ("inceleme isteği" = pull request, "belirteç" = token, "çalışma alanı" = worktree). Başlık yapısı ve içerik EN ile birebir eşleşiyor. *(Kaynak: `cs-llm.html` ↔ `tr-projeler.html` karşılaştırması)*

**Anonimleştirme şeffaf:** footer'da "case information is anonymized with organizational confidentiality in mind" açıkça bildiriliyor. *(Kaynak: her sayfanın footer metni)*

## 4. `<title>` ve meta etiketler

| Sayfa | `<title>` (karakter) | Değerlendirme |
|---|---|---|
| Ana sayfa EN | "Aydın Öztürk — Systems Architect for Shipyards & Fleets" (55) | İsim + uzmanlık + niş; ideal uzunlukta |
| Ana sayfa TR | "Aydın Öztürk — Tersaneler ve Filolar için Sistem Mimarı" | Doğal TR karşılığı |
| Vakalar (6) | "<Vaka başlığı> — Aydın Öztürk" (ör. 72 k.) | Her biri benzersiz; marka ismi sonda |

**Meta description:** her sayfada var ve benzersiz. EN ana sayfa description'ı **161 karakter** (TR: **167**) — SERP'te ~155–160 karakterde kırpılma riski taşıyor; son kelimeler ("…case studies and consulting.") Google'da kesilebilir. *(Kaynak: `home.html`, `tr.html` `<meta name="description">`)*

**Open Graph / Twitter:** `og:type, og:title, og:description, og:url, og:image, og:locale` tam set (vakalarda da var); `twitter:card=summary_large_image` mevcut ama **`twitter:image` yok** (çoğu platform og:image'den otomatik beslenir, dolayısıyla düşük risk). `og:image` sitenin tamamında tek ve genel bir görsel (`/og.png`, 200 OK — her vakaya özgü görsel yok). *(Kaynak: `home.html`, `cs-shipyard.html` meta etiketleri; `og.png` HEAD isteği)*

## 5. Heading yapısı

Her sayfada **tek `<h1>`**, ardından `<h2>` bölüm başlıkları ("What I work on", "Selected work", "About", "Contact"), kartlarda `<h3>` — hiyerarşi atlamasız ve tutarlı. Vakalarda h1 = vaka başlığı, h2 = Context/Problem/Approach/Outcome. TR sayfalarda aynı yapı korunuyor. *(Kaynak: çekilen tüm sayfaların heading sayımı)*

## 6. URL yapısı

- Alt küçük harf, tire ayraçlı, anlamlı slug'lar: `/case-studies/shipyard-erp-turnaround/` ✓
- TR karşılıkları da anlamlı: `/tr/projeler/tersane-erp-donusumu/` ✓ (diğer 5'i: `kamera-tabanli-uretim-takibi`, `llm-agentlari-ve-eski-kod`, `gemi-telemetri-platformu`, `yeniden-yazmak-mi-entegre-olmak-mi`, `erp-ile-konusmak`)
- Trailing slash tutarlı; sitemap'deki URL'lerle birebir uyumlu
- Teknik olarak not: slug'larda **TR karakterler ASCII'ye çevrilmiş** (`donusumu`, `kamera-tabanli-uretim-takibi` — "dönüşümü", "üretim"); tutarlı ve DNS-dostu, bu tercih doğru.

*(Kaynak: `sitemap-0.xml` + sayfalar arası link analizi)*

## 7. robots.txt ve sitemap

**robots.txt** (Cloudflare Managed content):
- `Content-Signal: search=yes, ai-train=no, use=reference` — arama indekslemesine izin, **AI eğitimine açık izin yok** (AB DSM Direktifi 2019/790 art. 4'e atıfla hak saklı tutulmuş)
- ~30 AI eğitim botu `Disallow: /` ile engelli (Amazonbot, GPTBot, ClaudeBot, CCBot, Google-Extended, meta-externalagent, MistralAI-Training vb.)
- Genel crawler'lar için `Allow: /`
- `Sitemap: https://aydinozturk.com/sitemap-index.xml` bildirimi var

**Sitemap:** `sitemap-index.xml` → `sitemap-0.xml` (17 URL, geçerli XML). Dikkat: yaygın varsayım olan `/sitemap.xml` **404** veriyor — doğru adres `sitemap-index.xml` ve robots'ta doğru bildirilmiş, yani indeksleme açısından sorun yok; sadece keşif sırasında 404'e takılma riski.

**Eksikler:**
- URL'lerde **`<lastmod>` yok** (Astro varsayılanı) — güncellik sinyali vermiyor
- Sitemap'teki hreflang `xhtml:link`'leri yalnızca ana sayfa çiftinde var (vakalarda yok); fakat vakaların sayfaları kendi `<link rel="alternate">` etiketleri ile tamamlıyor (bkz. §9) — dolayısıyla indeksleme açısından eksik değil.

*(Kaynak: `robots.txt`, `sitemap-index.xml`, `sitemap-0.xml`, `/sitemap.xml` 404 yanıtı)*

## 8. Teknik SEO işaretleri (canonical, hreflang, yapılandırılmış veri)

### 8.1 Canonical ve hreflang — **örnek seviyede**
Her sayfada kendine referanslı `rel="canonical"` ve tam `en / tr / x-default` üçlüsü:

```html
<!-- cs-shipyard.html -->
<link rel="canonical" href="https://aydinozturk.com/case-studies/shipyard-erp-turnaround/">
<link rel="alternate" hreflang="en" href="…/case-studies/shipyard-erp-turnaround/">
<link rel="alternate" hreflang="tr" href="…/tr/projeler/tersane-erp-donusumu/">
<link rel="alternate" hreflang="x-default" href="…/case-studies/shipyard-erp-turnaround/">
```

Ana sayfa ve 6 vakanın tamamında karşılıklı (mutual) hreflang doğrulandı. `<html lang="en">` / `<html lang="tr">` doğru. *(Kaynak: `home.html`, `tr.html`, `cs-*.html` link etiketleri)*

**Tek önemli içerme hatası:** 4 gizlilik sayfası (DriveInsight ve Zapp'ın EN+TR) **hiçbir menüden/footerdan linklenmiyor**; yalnızca sitemap üzerinden keşfedilebilir. Bu sayfalar `hreflang`/canonical içermiyor ve sitenin iç link ağıyla kopuk. *(Kaynak: ana sayfa link listesi vs. `sitemap-0.xml` karşılaştırması; `orphan-*.html`)*

### 8.2 Yapılandırılmış veri (JSON-LD)
Ana sayfa ve vakalarda `@type: Person` şeması: `name, jobTitle, url, sameAs (LinkedIn), knowsAbout: [Maritime ERP, Industrial IoT, Applied AI, Shipbuilding software]`. **Eksikler:** vakalar için `Article` şeması yok (başlık + tarih olmasa da `Article` eklemek zengin sonuç şansını artırır); `WebSite`/`ProfessionalService` şeması yok. *(Kaynak: `home.html`, `cs-shipyard.html` `<script type="application/ld+json">`)*

### 8.3 Anahtar kelime konumu
Niş bir kişisel marka sitesi olduğu için klasik hacim tabanlı SEO beklentisi düşük; yapı buna rağmen doğru:
- H1'de ana konum: "Systems that hold up where ships are built" — "ships/shipbuilding" anahtar kavramı
- Description'da: "ERP, industrial IoT, applied AI, shipbuilding, maritime" hepsi
- Vaka başlıkları (H1 + title) aramada bulunabilecek cümleler: "camera-based production tracking", "vessel telemetry", "LLM agent", "legacy ERP" — bunlar gerçek teknik arama sorgularıyla örtüşüyor
- Türkçe karşılıkları da H1/title'da ("gemi telemetrisi", "kamera tabanlı üretim takibi", "tersane ERP dönüşümü")

*(Kaynak: sayfa title/H1/description içerikleri)*

## 9. Erişilebilirlik işaretleri

- `<html lang>` doğru (en/tr) — ekran okuyucu dili ✓
- "Skip to content" / "İçeriğe atla" atlama bağlantısı var ✓ (her sayfanın ilk linki)
- Sayfalarda **`<img>` etiketi hiç yok** → eksik alt metin sorunu yok; og:image yalnızca paylaşım kartlarında
- Heading hiyerarşisi mantıklı (§5), link metinleri açık ("LinkedIn ↗", vaka başlıkları)
- Ana sayfada interaktif bir demo (kamera tarama simülasyonu) var — SVG/CSS tabanlı, `alt` yükü doğurmuyor; ancak butonların (`Run the scan`, `Reset`) ekran okuyucu erişimi HTML'de teyit edilemedi (statik çekimde interaktif davranış ölçülmez) — **ölçülmemiş**, teknik analiz görevinin (#261) kapsamına girer

*(Kaynak: `home.html` gövde ve heading/link analizi)*

---

## 10. Güçlü yönler

1. **Çift dil + tam hreflang/canonical:** EN-TR her sayfa eşleşmeli, karşılıklı hreflang ve doğru lang attribute — çoğu kurumsal siteden daha iyi yapılandırılmış.
2. **Somut, tutarlı içerik:** sayısal kanıtlar (200+ gemi, 26+ telemetri akışı), numaralı vaka kaydı, tek tip Context/Problem/Approach/Outcome şablonu; abartısız, teknik olarak güvenilir ton.
3. **Yüksek kalite Türkçe çeviri:** terminoloji tutarlı, doğal akış.
4. **Temiz URL mimarisi:** anlamlı, ASCII slug'lar, tutarlı trailing slash, sitemap uyumu.
5. **SEO temel etiketleri eksiksiz:** her sayfada benzersiz title/description, OG set, Person JSON-LD.
6. **Bilinçli AI politikası:** robots.txt'te Content-Signal ve bot bazlı kurallar — telif duruşu açıkça tanımlı.
7. **Erişilebilirlik hijyeni:** skip link, doğru lang, img/alt sorunu yok.

## 11. Zayıf yönler ve somut öneriler

| # | Zayıf yön | Öneri | Etki |
|---|---|---|---|
| 1 | 4 gizlilik sayfası (DriveInsight/Zapp) **yetim** — hiçbir yerden link yok, hreflang/canonical de içermiyor | Footer'a "Gizlilik" linki ekleyin; mümkünse ilgili vaka/ürün bölümlerinden de linkleyin; sayfalara canonical + hreflang ekleyin | Sitenin keşfedilebilirliği ve ürün tanıtımı |
| 2 | Sitemap URL'lerinde `lastmod` yok | Astro sitemap ayarında `lastmod` (dosya mtime veya deploy tarihi) etkinleştirin | Tazelik sinyali |
| 3 | Ana sayfa meta description 161 (EN) / 167 (TR) karakter — SERP kırpma riski | 150–155 karaktere kısaltın; öne çıkan değeri (10+ yıl, 200+ gemi, ERP/IoT/AI) sonuna bırakmayın | Tıklama oranı |
| 4 | `twitter:image` eksik; tüm sitede tek `og.png` | `twitter:image` ekleyin; her vakaya özgü OG görseli (ör. CS-01 kamera demosu) üretin | Sosyal paylaşım etkisi |
| 5 | Vakalarda `Article` JSON-LD yok | Vaka şablonuna `@type: Article` (headline, author→Person, datePublished) ekleyin | Zengin arama sonuçları |
| 6 | `/sitemap.xml` 404 (gerçek adres `sitemap-index.xml`) | İsteğe bağlı: `/sitemap.xml`'i `sitemap-index.xml`'e yönlendirin; keşif araçları 404 ile karşılaşmasın | Küçük |
| 7 | Sadece 17 URL, blog/güncel içerik akışı yok | B2B kişisel marka için doğal; ancak arama görünürlüğü istenirse niş makaleler (ör. "shipyard ERP integration") taze içerik sağlar | Orta (stratejik) |
| 8 | Interaktif demo (kamera tarama) erişilebilirlik davranışı statik analizde doğrulanamadı | #261 (teknik analiz) kapsamında e2e/ekran okuyucu testi önerilir | Açık |

## 12. Sonuç

aydinozturk.com, SEO temelleri (title, description, canonical, hreflang, sitemap, yapılandırılmış veri) **örnek düzeyde** kurulu, içerik kalitesi ve Türkçe kullanımı yüksek, nişine (maritime ERP / endüstriyel AI / filo telemetrisi) çok iyi konumlanmış bir kişisel profesyonel sitedir. Anahtar iyileştirme alanları: **yetim gizlilik sayfalarının iç ağa bağlanması, `lastmod` eklenmesi, meta description uzunlukları, vaka bazlı OG görselleri ve Article şeması**. Bu düzeltmelerin tamamı küçük çaplıdır ve sitenin mevcut Astro şablon yapısına uygun düşer.

*Bu rapor #260 planının #262 alt görevi kapsamındadır; teknik (performans/güvenlik) ve alan adı geçmişi bulguları #261 ve #263 raporlarındadır.*
