# Konsolide Araştırma Raporu: aydinozturk.com

- **Görev:** #264 (Plan #260 — aydinozturk.com kapsamlı araştırması)
- **Hazırlayan:** agent-6 · **Tarih:** 2026-11-05
- **Kapsam:** Bu rapor, aynı günün içinde üç ayrı alt görevle üretilen raporun bulgularını tek Türkçe belge halinde konsolide eder:
  1. **Teknik site analizi** (#261, agent-3) → `research/aydinozturk.com/site-technical.md`
  2. **İçerik ve SEO analizi** (#262, agent-4) → `research/aydinozturk.com/site-content-seo.md`
  3. **Alan adı geçmişi ve çevrimiçi varlık** (#263, agent-5) → `research/aydinozturk.com/domain-history.md` (main, merge 582dcd5)

Alt raporlar değiştirilmemiştir; bu dosya yalnızca onları çelişkisiz biçimde özetler. Her bölümde bulguların geldiği alt rapor (ve oradaki dış kaynak) referans olarak gösterilir.

---

## 1. Özet (5 madde)

1. **Site, tek bir kişinin net ve tutarlı kişisel markasıdır.** "Aydın Öztürk — Systems Architect for Shipyards & Fleets" başlıklı, EN/TR çift dilli bir portföy/danışmanlık sitesidir; GitHub (ad, konum: Kocaeli, firma: Uzmar Technologies, `blog` alanı aydinozturk.com) ve site kimlik bilgileri güçlü biçimde tek kişiye işaret eder. [Kaynak: #262 §1, #263 §1/§5]
2. **Teknik olarak sağlam ve çok hızlı; güvenlik başlıklarında belirgin boşluk var.** Statik Astro site Cloudflare arkasında, HTTP/2 aktif, TTFB ~160–190 ms, ana sayfa ~78 KB. HSTS, CSP, X-Frame-Options gibi güvenlik başlıkları yok ve `http://` isteği 301 yerine 200 dönüyor (Always Use HTTPS kapalı). [Kaynak: #261 §1, §5, §6]
3. **SEO temelleri örnek düzeyde; içerik kalitesi yüksek.** 17 URL'lik sitemapta tümü 200; karşılıklı (mutual) canonical + `en/tr/x-default` hreflang tüm sayfalarda doğrulandı; somut, sayısal ve abartısız içerik ("200+ vessel projects" vb.); Türkçe çeviri doğal ve terminolojik olarak tutarlı. Küçük düzeltmeler (meta description uzunluğu, Article şeması, `lastmod`, yetim gizlilik sayfaları) bekleniyor. [Kaynak: #262 §3, §8.1, §10–11]
4. **Alan adı bugünkü kayıttan çok daha eski ve geçmişte başka sahibin içeriğini barındırmış.** RDAP'ta NameCheap kaydı 2026-02-13 (expiry 2027-02-13, tek yıllık döngü) görünse de Wayback izleri 2005'e (robots.txt) ve kök sayfada 2010'a (başlığı "Cuneyt SARIKAYA" — farklı kişi) dayanır. 2026 tarihi ilk tescil değil, mevcut registrar kaydının/transferinin tarihidir. [Kaynak: #263 §1, §2, §4]
5. **Bilinen en kritik iyileştirme alanları üçlüktür:** (a) HTTP→HTTPS yönlendirmesi + HSTS, (b) güvenlik başlıkları, (c) dört yetim gizlilik sayfasının (eski DriveInsight/Zapp ürünleri) iç ağa bağlanması veya temizlenmesi. Bunların tamamı düşük maliyetli, düşük riskli düzeltmelerdir. [Kaynak: #261 §6, #262 §8.1/§11]

---

## 2. Site ve amaç

aydinozturk.com bir **kişisel profesyonel (personal-brand) sitesidir**; kurumsal ürün sitesi değildir. [Kaynak: #262 §1]

- **Kimlik:** Site sahibi kendini "yazılım geliştirme müdürü ve sistem mimarı" olarak tanımlar; uzmanlık alanları gemi inşa ERP platformu, filo telemetrisi ve endüstriyel AI'dır (10+ yıl, 10 kişilik ekip yönetimi). JSON-LD `Person` şemasında `knowsAbout`: Maritime ERP, Industrial IoT, Applied AI, Shipbuilding software. [Kaynak: #262 §1, §8.2]
- **Hedef kitle ve niyet:** Tersaneler, filo operatörleri ve proje bazlı imalat firmalarındaki teknik karar vericiler; sayfa sonunda "Open to: Selected consulting conversations" — site **seçici danışmanlık** ve profesyonel ağ (LinkedIn bağlantılı) amaçlıdır. [Kaynak: #262 §1]
- **İçerik evreni:** 17 sayfalık bir yapı: EN + TR ana sayfa, 6 vaka çalışması ve TR karşılıkları (`/case-studies/…` ↔ `/tr/projeler/…`), ayrıca 4 gizlilik sayfası. Ana sayfa tek sayfa (one-page) düzeninde (`/#work`, `/#expertise`, `/#about`, `/#contact`). [Kaynak: #261 §3, #262 §2]
- **Girişim tanıtımı:** "In development" aşamasında bir girişim — **DriveInsight** — kamera + CAD + ERP verisinden denetlenebilir üretim ilerleme ölçümü. [Kaynak: #262 §1]
- **Doğrulanan kimlik zinciri (dış varlık):** GitHub hesabı `aydinozturk` (kuruluş 2016-08-14, "Aydın Öztürk", Kocaeli, Uzmar Technologies, bio "Software Development Manager", `blog` alanı doğrudan aydinozturk.com); repo listesi alanla tutarlı (S1000D, VDMS, uzmar.modbus, orkestra-integration-provider, elm327-tcp-simulator). Site'den bağlı tek dış profil LinkedIn (`linkedin.com/in/aydinozturk`) ve e-posta (`hello@aydinozturk.com`); LinkedIn bot korumalı olduğundan bağımsız doğrulanamamıştır. [Kaynak: #263 §5, #261 §3]

---

## 3. Teknik bulgular

Kaynak: #261 (curl + openssl çıktılarının tamamı alt raporda referanslıdır).

### 3.1 Altyapı

| Bulgu | Durum |
|---|---|
| CDN/edge | Cloudflare (`server: cloudflare`, `cf-cache-status: HIT`) |
| Protokol | HTTP/2 aktif; HTTP/3 yalnızca `alt-svc` ile reklam ediliyor — ortamın libcurl sürümü QUIC desteklemediğinden gerçek h3 yanıtı **doğrulanamadı** |
| TLS | Google Trust Services (CN=WE1) yayıncılı, `aydinozturk.com` + wildcard SAN, geçerlilik 2026-10-13 → 2027-01-11 |
| Teknoloji | Statik **Astro** site (hash'li `/_astro/` asset imzası); tek harici JS modülü 2,1 KB; CSS tek dosya 9,7 KB; framework runtime'ı yok |
| DNS | A/AAAA edge, NS, MX (Cloudflare e-posta), TXT (`google-site-verification`, SPF) — tamamı Cloudflare altyapısı [ayrıca #263 §3] |

### 3.2 Performans

Çok hafif bir statik site: TTFB 3 numunede 0,190 s / 0,165 s / 0,157 s; ana sayfa HTML 23,7 KB ham / **6,7 KB brotli**; brotli sıkıştırması aktif; sayfa toplamı ~78 KB. Tek belirgin "ağırlık" 65 KB'lık `og.png` (yalnızca sosyal paylaşım önizlemesinde kullanılır, gezinmede etkisi yok). Vaka sayfaları ~2,5 KB brotli. **Sınır:** bunlar sunucu tarafı (curl) sinyalleridir; LCP/CLS/TBT gibi tarayıcı metrikleri bu analizde ölçülmemiştir. [Kaynak: #261 §5, §8.2]

### 3.3 Erişilebilirlik ve mobil

Sitemap'teki **17 URL'in tamamı 200** döndürüyor; olmayan sayfalarda özel 404 sayfası (`<title>404 — Aydın Öztürk</title>`). `viewport` meta tüm sayfalarda, `<html lang>` doğru (en/tr), CSS'te sınırlı ama mevcut `@media` kırılımı. [Kaynak: #261 §3, §7]

### 3.4 Güvenlik — dikkat çeken bulgular

`GET https://aydinozturk.com/` başlık taraması sonucunda **hiçbir** modern güvenlik başlığı yoktur: HSTS, CSP, X-Frame-Options/frame-ancestors, X-Content-Type-Options, Referrer-Policy, Permissions-Policy yok; `.well-known/security.txt` 404. [Kaynak: #261 §6]

En önemli tekil bulgu: **`curl http://aydinozturk.com/` → `200 OK`, yönlendirme yok.** Cloudflare "Always Use HTTPS" kapalı olduğu için ilk ziyareti HTTP yapan bir istemci içeriği şifresiz alır; HSTS de olmamışken bu pencere kalıcıdır. İkincil not: `www.aydinozturk.com` da 200 dönüyor (apex'e 301 yok) — canonical apex'e işaret ettiği için SEO çifte içerik riski düşük, tek kanonik hosta yönlendirme iyi uygulamadır. [Kaynak: #261 §6, §8.5]

Pozitif güvenlik izleri: çerez yok (`Set-Cookie` yok), hata sayfalarında sunucu/sürüm sızıntısı yok, ve `robots.txt` bilinçli bir **AI-eğitim blok politikası** taşıyor (`Content-Signal: search=yes,ai-train=no,use=reference` + GPTBot, ClaudeBot, CCBot, Amazonbot vb. ~30 bot `Disallow: /`). [Kaynak: #261 §6]

---

## 4. SEO / içerik bulguları

Kaynak: #262 (tüm sayfa HTML'leri aynı gün çekilip analiz edilmiştir).

### 4.1 Güçlü yönler

- **Canonical + hreflang örnek düzeyde:** her sayfada kendine referanslı `rel="canonical"` ve tam `en/tr/x-default` üçlüsü; ana sayfa ve 6 vakanın tamamında karşılıklı (mutual) eşleşme doğrulandı. Çoğu kurumsal siteden iyi yapılandırılmış.
- **İçerik kalitesi yüksek ve somut:** jenerik şablon dilinden uzak, ölçülebilir iddialar ("200+ vessel projects", "26+ vessels streaming telemetry", "12+ ERP modules"); vakalar `CS-01`…`CS-06` numaralı, etiketli (durum: "Proof of concept" / "In daily use" / "In production") ve sabit **Context → Problem → Approach → Outcome** şablonuyla yazılmış; teknik olarak tutarlı, abartısız ton.
- **Türkçe çeviri sadık ve doğal:** makine çevirisi izi yok; terminoloji tutarlı ("inceleme isteği" = pull request, "belirteç" = token); başlık yapısı EN ile birebir eşleşiyor.
- **Temiz URL mimarisi:** anlamlı ASCII slug'lar (TR karakterler doğru biçimde çevrilmiş), tutarlı trailing slash, sitemap uyumu.
- **Meta etiketler eksiksiz:** her sayfada benzersiz `<title>` (ana sayfa 55 karakter, isim + uzmanlık + niş) ve benzersiz meta description; tam OG seti (`og:image` dahil); `Person` JSON-LD.
- **Erişilebilirlik hijyeni:** doğru `lang`, her sayfada "Skip to content" atlama bağlantısı, gövdede `<img>` olmadığı için alt metin sorunu yok.
- **Şeffaflık:** footer'da vaka bilgilerinin anonimleştirildiği açıkça bildiriliyor.

### 4.2 Zayıf yönler (detaylı liste alt raporda)

| # | Zayıf yön |
|---|---|
| 1 | **4 yetim gizlilik sayfası** (`/driveinsight/privacy/`, `/zapp/privacy/` + TR karşılıkları): hiçbir menüden/footerdan linklenmiyor, canonical/hreflang içermiyor; muhtemelen eski DriveInsight/Zapp ürünlerinin artığı — hem SEO hem içerik sahipliği sorunu |
| 2 | Ana sayfa meta description **161 (EN) / 167 (TR) karakter** — SERP'te ~155–160 karakterde kırpılma riski |
| 3 | Sitemap URL'lerinde **`lastmod` yok** (Astro varsayılanı) — güncellik sinyali vermiyor |
| 4 | Vakalarda **`Article` JSON-LD yok**; `WebSite`/`ProfessionalService` şeması da yok |
| 5 | **`twitter:image` eksik**; sitenin tamamında tek ve genel `og.png` (vakaya özgü görsel yok) |
| 6 | `/sitemap.xml` **404** — gerçek adres `sitemap-index.xml` (robots'ta doğru bildirilmiş, indeksleme sorunu yok; yalnızca keşif araçları 404'e takılır) |
| 7 | İçerik hacmi düşük: toplam 17 URL, blog/güncel akış yok (B2B kişisel marka için doğal; arama görünürlüğü istenirse stratejik konu) |
| 8 | Ana sayfadaki interaktif kamera tarama demosunun ekran okuyucu davranışı statik analizde ölçülmemiş |

[Kaynak: #262 §7–§11]

---

## 5. Alan adı geçmişi ve çevrimiçi varlık

Kaynak: #263 (RDAP, DoH, Wayback CDX, GitHub API — erişim 2026-11-05).

### 5.1 Kayıt durumu

| Alan | Değer |
|---|---|
| Registrar | NameCheap, Inc. (IANA #1068) |
| RDAP "registration" | 2026-02-13 → **ilk tescil değil**, NameCheap'a kayıt/transfer tarihidir (aşağıdaki arşiv kanıtları) |
| Expiry | 2027-02-13 (≈1 yıllık döngü; last-changed 2026-08-15) |
| Durum | `client transfer prohibited` (transfer kilitli) |
| DNSSEC | İmzalı değil |
| Nameserver'lar | `sid.ns.cloudflare.com`, `teagan.ns.cloudflare.com` |

### 5.2 Tarihçe (Wayback Machine)

- **En eski iz:** `robots.txt` 2005-09-05; kök sayfa **2010-03-23** — alan adı bugünkü 2026 kaydından **15–21 yıl önce aktif**.
- **2010 görüntüsünde farklı kişi:** kök sayfa başlığı "Cuneyt SARIKAYA" → alan adı geçmişte başka bir sahiplik/içerik barındırmış; bugünkü "Aydın Öztürk" markası sonraki bir dönemdedir.
- **2011 ve 2015** görüntüleri ~2,4 KB neredeyse boş gövde (o dönemlerde site boş bırakılmış görünüyor).
- Toplam ~82 arşiv görüntüsü; 2019→2021 ve 2021→2025 arasında kök sayfada boşluk; en yakın görüntü 2025-07-10.
- Arşiv yalnızca kök/robots/favicon gibi sığ yolları içeriyor; derin sayfa taraması yapılmamış.

### 5.3 Çevrimiçi varlık ve doğrulanamayanlar

- **Doğrulanan:** GitHub `aydinozturk` (güçlü kimlik eşleşmesi — ad, konum, firma, blog alanı; hesap 2016'dan beri, 17 repo, 24 takipçi; repo içeriği gemi/savunma/sanayi yazılımı alanıyla tutarlı), Google Search Console doğrulaması (DNS TXT kaydı), Cloudflare e-posta altyapısı (MX kayıtları).
- **Referans olarak alınan ama bağımsız doğrulanamayan:** LinkedIn profili (bot/giriş korumalı).
- **Yöntemsel sınırlamalar (negatif bulgu DEĞİL):** bu ortamda web arama aracı çalışmadığından X/Twitter, Google Scholar, Facebook, Instagram profilleri ve dış backlink/mention listesi **derlenemedi**; trafik tahmini için SimilarWeb halka açık verisi bot koruması nedeniyle alınamadı. [Kaynak: #263 §5–§8]

---

## 6. Riskler ve zayıf noktalar (konsolide)

Üç rapordan bir araya getirilen, öncelik sırasına göre:

| # | Risk / zayıf nokta | Köken | Etki |
|---|---|---|---|
| R1 | **HTTP → HTTPS yönlendirmesi yok** (`http://` 200) + HSTS yok → ilk ziyaret HTTP ise içerik şifresiz aktarılabilir | #261 §6 | Yüksek |
| R2 | **Güvenlik başlıkları eksik** (CSP, X-Frame-Options, nosniff, Referrer-Policy…) → clickjacking/ MIME sniffing için teknik pencere | #261 §6 | Orta-Yüksek |
| R3 | **4 yetim gizlilik sayfası** (eski DriveInsight/Zapp ürünleri) — iç link ağından kopuk, canonical/hreflang'sız; içerik sahipliği belirsiz | #261 §8.4, #262 §8.1 | Orta |
| R4 | `www.` host 301'siz (200) → iki kanonik host var; düşük SEO riski, iyi uygulama sapması | #261 §8.5 | Düşük |
| R5 | **Alan adı geçmişi:** önceki sahiplik (2010, farklı kişi) — eski dönemden kalan gizli backlink/reputasyon mirası bu araştırmada incelenemedi | #263 §4, §7.2 | Bilinmeyen (not) |
| R6 | Alan adı **tek yıllık döngüde** yenileniyor (expiry 2027-02-13), DNSSEC imzası yok — süre yenileme disiplinine bağımlı (transfer kilidi pozitif) | #263 §2 | Düşük |
| R7 | SEO detayları: meta description aşırı uzun, `lastmod` yok, `Article` şeması yok, tek `og.png`, `/sitemap.xml` 404 | #262 §11 | Düşük |
| R8 | **Doğrulama boşlukları:** HTTP/3, tarayıcı performans metrikleri (LCP/CLS/TBT), interaktif demo erişilebilirliği, LinkedIn ve diğer sosyal profiller, trafik — bu ortamda ölçülemeyen noktalar şeffaflık için açıkça notlu; sonuçların kesinliği bunlara bağlıdır | #261 §8, #262 §9, #263 §8 | Bilgi eksikliği |

Çelişki notu: üç rapor birbiriyle tutarlıdır; tek "görünür" fark (RDAP'ta 2026 kayıt tarihi) #263'te arşiv kanıtlarıyla açıklanmıştır (ilk tescil değil, mevcut registrar kaydı) ve bu raporda aynı yorumla aktarılmıştır.

---

## 7. Öneriler (öncelikli)

### P1 — Güvenlik (yüksek öncelik, düşük maliyet)
1. Cloudflare'de **Always Use HTTPS**'i etkinleştir (`http://` → 301) ve **HSTS** başlığı ekleyin; önce düşük `max-age` ile başlayıp kademeli artırın. [Kaynak: #261 §6]
2. Güvenlik başlıklarını tamamlayın: CSP, `X-Frame-Options`/`frame-ancestors`, `X-Content-Type-Options: nosniff`, `Referrer-Policy`, isteğe bağlı `Permissions-Policy`; `security.txt` ekleyin. [Kaynak: #261 §6]

### P2 — İçerik/SEO düzeltmeleri (orta öncelik)
3. **`www.aydinozturk.com` → apex'e 301** yönlendirmesi. [Kaynak: #261 §8.5]
4. **Yetim gizlilik sayfalarını çözümlen:** ilgili ürün bölümlerinden/footerdan linkleyin + canonical/hreflang ekleyin; DriveInsight/Zapp artık aktif değilse sayfaları ve sitemap girdilerini kaldırın. [Kaynak: #262 §11.1]
5. Ana sayfa meta description'ını **150–155 karaktere** kısaltın (değer önermesini sona bırakmayın). [Kaynak: #262 §11.3]
6. Vaka şablonuna **`Article` JSON-LD** (headline, author→Person, datePublished) ve sitemap'e **`lastmod`** ekleyin. [Kaynak: #262 §11.2, §11.5]
7. Vakaya özgü **OG görselleri** üretin ve `twitter:image` ekleyin. [Kaynak: #262 §11.4]
8. `/sitemap.xml` → `sitemap-index.xml` yönlendirmesi (keşif araçları için). [Kaynak: #262 §11.6]

### P3 — Stratejik / düşük öncelik
9. **DNSSEC imzalama** (Cloudflare üzerinden basit) ve alan adını çok yıllıya yenileme (veya en azından yenileme hatırlatıcısı; expiry 2027-02-13). [Kaynak: #263 §2, §7.4]
10. Arama görünürlüğü hedeflenirse niş, taze içerik (ör. "shipyard ERP integration" temalı makaleler) — 17 URL'lik sabit yapıyı tamamlar. [Kaynak: #262 §11.7]
11. **Ölçüm boşluklarını kapatın:** PageSpeed Insights/Lighthouse koşularıyla tarayıcı metriklerini (LCP, CLS, TBT) alın; HTTP/3'ü QUIC destekli istemciyle doğrulayın; interaktif demo için ekran okuyucu testi yapın. [Kaynak: #261 §8.1–8.3, #262 §11.8]

---

## 8. Kaynaklar

### 8.1 Bu rapora girdi olan alt raporlar (depo içinde)
- `research/aydinozturk.com/site-technical.md` — #261, agent-3 (main, merge 08b6053)
- `research/aydinozturk.com/site-content-seo.md` — #262, agent-4 (main, merge d831c44)
- `research/aydinozturk.com/domain-history.md` — #263, agent-5 (main, merge 582dcd5)

### 8.2 Alt raporlarda referanslı birincil kaynaklar (erişim 2026-11-05)
1. `https://aydinozturk.com/` ve tüm 17 sitemap URL'i — `curl` (başlık/gövde/boyut/TTFB), HTTP/2 doğrulaması
2. `openssl s_client -connect aydinozturk.com:443` — TLS sertifikası (issuer, SAN, geçerlilik)
3. `https://aydinozturk.com/sitemap-index.xml` → `sitemap-0.xml` — sayfa haritası (17 URL)
4. `https://aydinozturk.com/robots.txt` — AI-eğitim blok politikası (2.751 B)
5. `http://aydinozturk.com/` — HTTP davranışı (200, yönlendirme yok)
6. Verisign RDAP: `https://rdap.org/domain/AYDINOZTURK.COM` → `https://rdap.verisign.com/com/v1/domain/aydinozturk.com` — registrar, tarihler, durum, NS, DNSSEC
7. Cloudflare DoH: `https://1.1.1.1/dns-query` (A, AAAA, MX, NS, TXT, SOA; apex + www) — DNS kayıtları
8. Wayback Machine CDX: `http://web.archive.org/cdx/search/cdx?url=aydinozturk.com*` — ~82 arşiv görüntüsü; örnek görüntüler 2005/2010/2011/2015/2025
9. GitHub API: `https://api.github.com/users/aydinozturk` (+ `/repos`, repository search) — profil ve repo listesi
10. `https://www.similarweb.com/website/aydinozturk.com/` — trafik verisi (bot korumalı, alınamadı; sınırlılık olarak raporlandı)

### 8.3 Yöntem notları
- Tüm bulgular 2026-11-05 UTC aynı gününde, ağ üzerinden canlı erişimle elde edilmiştir; dış servisler (LinkedIn, SimilarWeb, bazı arşiv görüntüleri) bot/giriş korumalı olduğundan doğrulanamayan her nokta ilgili alt raporda açıkça "sınırlama" olarak işaretlenmiştir.
- `whois`/`dig` istemcileri ortamda bulunmadığından RDAP JSON ve DNS-over-HTTPS kullanılmıştır (eşdeğer sonuç). [Kaynak: #263 §2, §8]
- Tekrarlanabilirlik için tam kaynak komut listesi #261'in §9 bölümündedir.
