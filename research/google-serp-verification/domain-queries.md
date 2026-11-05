# Gerçek Google SERP doğrulaması — alan adı/marka sorguları

> Görev: [#280] (Plan #279 — admin [3854]: "Google dan arayabilirsin") · Çalışan: agent-3
> Çekim tarihi: **2026-11-05, ~20:07–20:10 UTC** (3 tam tur; her sorgu ≥2 kez, biri ~20:05 UTC)
> Önceki durum: `reports/google-search-results.md` (#268) "Google'a erişilemedi" demişti; bu rapor o eksikliği **gerçek Google SERP'inden** kapatır.
> Sınıflandırma kuralları: `research/aydinozturk.com/search-serp.md` §2, §4, §5 (kişi / site / başka kişi / şehir / filler).

---

## 1. Özet bulgular

1. **Site Google'da indeksli ve görünüyor — Bing'deki "0 sonuç" tablosu motor bazlıymış.** `site:aydinozturk.com` sorgusu **10 aydinozturk.com sayfası** döndürdü (ana sayfa EN+TR, DriveInsight/Zapp gizlilik sayfaları EN+TR, 4 blog yazısı) (Bölüm 4.2). Karşılaştırma: aynı sorgu Bing'de alan adından 0 sayfa döndürmüştü (#266 §4.7).
2. **Google'ın AI Özeti (AI Bakışı) alan adını doğru kişiyi tanıyarak özetliyor:** "aydinozturk.com adresi, Aydın Öztürk adlı Yazılım Geliştirme Müdürü ve Sistem Mimarının kişisel web sitesidir" + siteden "öne çıkan bilgiler" (Bölüm 4.1).
3. **Kişinin LinkedIn profili, `"aydinozturk linkedin"` sorgusunda Google AI Özeti'nin ÖNE ÇIKAN 1. profili:** "Aydın Öztürk: Software Development Manager / Architect (UZMAR Technology)" (Bölüm 4.4). Klasik organik listede `linkedin.com/in/aydinozturk` URL'si ilk ~12 sonuçta görünmedi; dizin sayfaları ve başka Aydın Öztürk profilleri sıralandı.
4. **İsim çakışması Google'da da gerçek:** `"aydinozturk"` ve `"aydinozturk.com"` sorgularının organik sonuçlarının tamamı **başka** Aydın Öztürk'lere ait (yayıncı, müzisyen, gazeteci, Instagram/X/Pinterest hesapları, avukat, şair) (Bölüm 4.1, 4.3). Google, token'ı `aydin ozturk` olarak çözüp "Müzisyen" varlık panosu gösteriyor.
5. **Kontrol sorgusu başarılı:** `"uzmar technology"` UZMAR Gemi İnşa grubunun sayfalarını (uzmar.com, uzmar.com.tr, **uzmar.tech** = teknoloji birimi) ilk 2 pozisyonda döndürdü → pipeline doğru çalışıyor (Bölüm 4.6).

---

## 2. Metot

- **Tarayıcı:** Windows host'taki gerçek Chrome 156.0.8078.80; CDP ucu `http://192.168.65.254:9222` (#274'te doğrulanmış uç).
- **Çalıştırma:** chrome-devtools MCP `claude mcp list`'e göre "✔ Connected" idi ancak bu oturumda MCP araçları enumeration'da görünmedi; görev tanımındaki fallback izlendi (chair'e DM'de bildirildi). Arama, aynı CDP ucuna WebSocket ile doğrudan bağlanarak yapıldı: **sadece kendine ait yeni sekme** açıldı (`/json/new?about:blank`), `Page.navigate` ile sorguya gidildi, `Runtime.evaluate` ile DOM çekildi, sekmeler kullanımdan sonra kapatıldı. Mevcut sekmelere dokunulmadı* (yıldız: Bölüm 8'de şeffaflık notu).
- **URL:** her sorgu için `https://www.google.com/search?q=<sorgu>&hl=tr&gl=tr`. Giriş yapılmadı, arama sonucuna tıklanmadı, hiçbir form doldurulmadı.
- **CAPTCHA/JS challenge:** 3 turda **hiçbir sorguda** challenge/consent sayfası görülmedi (eski raporun "Google'a erişilemedi" durumu, sade HTTP istemcisi içindi; gerçek tarayıcı sorunsuz geçti).
- **Çekilen alanlar:** SERP'in tam URL'si, sayfa başlığı, organik sonuçlar (başlık, görünen URL, snippet), AI Bakışı (AI Overview) metni, Knowledge Panel / People-also-ask varlığı, "Bunu mu demek istediniz?" önerileri.
- **Chrome 156 SERP düzeni notu:** organik sonuç bağlantıları `a[href^="/goto"]` (opak hedef) olarak render ediliyor; gerçek hedef URL SERP'te **görünen** breadcrumb (örn. `https://uzmar.tech › c...`) olarak raporlandı — tıklanmadan okundu.
- **A/B varyasyonu:** aynı sorgunun farklı çekimlerinde AI Bakışı kutusu içeriği ve ilk organik sonuç değişti (örn. Q1: 3 varyasyon gözlemledik). Aşağıda her sorgunun **son tur** (20:10 UTC) kaydı ana tablo olarak verildi; fark olan yerlerde varyasyonlar not düştü. Sonuç sayıları ("Yaklaşık N sonuç") bu SERP varyantında metin olarak görünmüyordu.

---

## 3. Sorgu listesi ve çekim zamanları (UTC)

| # | Sorgu | Tur 1 | Tur 2 | Tur 3 (ana) |
|---|---|---|---|---|
| 1 | `aydinozturk.com` | 20:07:33 | 20:08:50 | 20:10:07 |
| 2 | `site:aydinozturk.com` | 20:07:39 | 20:08:55 | 20:10:12 |
| 3 | `aydinozturk` | 20:07:45 | 20:09:01 | 20:10:18 |
| 4 | `aydinozturk linkedin` | 20:07:50 | 20:09:07 | 20:10:24 |
| 5 | `aydinozturk twitter` | 20:07:56 | 20:09:12 | 20:10:29 |
| 6 | `uzmar technology` | 20:08:01 | 20:09:18 | 20:10:35 |

---

## 4. Sorgu başına sonuçlar (Google TR, 2026-11-05)

İlinti değerleri: **kişi** = Aydın Öztürk (UZMAR, bu kişi) · **site** = aydinozturk.com · **başka kişi** = farklı kişi · **şehir** = Aydın ili · **filler** = alakasız.

### 4.1 `aydinozturk.com` — SERP: https://www.google.com/search?q=aydinozturk.com&hl=tr&gl=tr

Sayfa başlığı: `aydinozturk.com - Google'da Ara`. Öneri: **"Bunu mu demek istediniz? aydinozturk.com.tr"**. Knowledge Panel yok; PAA yok; **AI Bakışı VAR**.

**AI Bakışı (20:10 turu, birebir):** "Aydın Öztürk adına sahip farklı alanlarda bilinen birden fazla kişi ve web sitesi bulunmaktadır: **Sistem Mimarı / Yazılım Geliştirici: Gemi inşa ve denizcilik operasyonları için kurumsal yazılım, endüstriyel IoT ve yapay zeka alanında çözümler geliştiren, Aydın Öztürk Resmi Web Sitesi sahibidir. — aydinozturk.com** · Dijital Pazarlama Uzmanı: Boğaziçi Üniversitesi mezunu olup, Google Ads, Analytics ve Tag Manager gibi konularda Udemy Eğitimleri hazırlayan…".
*(20:08 turu varyasyonu: "aydinozturk.com adresi, Aydın Öztürk adlı Yazılım Geliştirme Müdürü ve Sistem Mimarının kişisel web sitesidir" + "Sitede öne çıkan bilgiler: Meslek/Rol: … ERP platformları" — siteden üretilmiş yapılandırılmış özet.)*

| # | Başlık | Görünen URL | Snippet (kısa) | İlinti |
|---|---|---|---|---|
| AI | aydinozturk.com (AI Kutusu) | — | yukarıdaki AI Özeti | **site + kişi** |
| 1 | Aydın Öztürk (YouTube, 20+ takipçi) | youtube | "Merhaba arkadaşlar adım Aydın Öztürk ve 20 yaşındayım… streamer…" | başka kişi |
| 2 | Aydin Öztürk (@aydinozturk58) Instagram (150+ takipçi) | instagram | 153 followers · 2018 araba ile TR… | başka kişi |
| 3 | Aydın Öztürk (@aydinsozturk) Instagram (1,8 B+ takipçi) | instagram | CHP Bursa İl Başkanlığı'ndaki görevine son verildi… | başka kişi |
| 4 | Aydın Öztürk (@aydnztrk) Instagram (520+ takipçi) | instagram | — | başka kişi |
| 5 | Aydin Öztürk (@aydinozturk2635) Instagram (550+ takipçi) | instagram | DEVREK ZONGULDAK… | başka kişi |
| 6 | Aydın Öztürk (@aydinztrkzh) Instagram (170+ takipçi) | instagram | "Books Runner Stock&portfolio" | başka kişi |
| 7 | Aydın ÖZTÜRK kitabı — Nadir Kitap | https://www.nadirkitap.com › kitapara_ai | (e-ticaret şablon snippet'i) | başka kişi |
| 8 | AYDIN ÖZTÜRK (@AvAydinOZTURK) X (80+ takipçi) | x | Marmara Üniv. Hukuk mezunu, İstanbul… | başka kişi |
| 9 | Photo by Aydın Öztürk (@aydinozturk61) Instagram | instagram | 1 beğeni, 1 ay önce | başka kişi |

**Okuma:** Alan adının kendisi için **organik web sonuçlarında site sayfası çıkmadı** (3 turda da); site yalnızca AI Kutusu'nda (ve bir erken gözlemde — Bölüm 4.1 notu) göründü. Organik liste 9/9 **başka kişi**. A/B notu: ilk turda (~20:05 UTC, tur dışı manuel gözlem) aynı sorguda ana sayfa "Aydın Öztürk — Systems Architect for Shipyards & Fleets / https://aydinozturk.com" **1. organik sonuç** olarak da görüldü → varyantlara göre site ilk sayfa organik listeye girebiliyor.

### 4.2 `site:aydinozturk.com` — SERP: https://www.google.com/search?q=site:aydinozturk.com&hl=tr&gl=tr

Sayfa başlığı: `site:aydinozturk.com - Google'da Ara`. AI Kutusu yok; KP yok; PAA yok.

| # | Başlık | Görünen URL | İlinti |
|---|---|---|---|
| 1 | Aydın Öztürk — Systems Architect for Shipyards & Fleets | https://aydinozturk.com | **site** |
| 2 | Tersaneler ve Filolar için Sistem Mimarı - Aydın Öztürk | https://aydinozturk.com › … | **site** |
| 3 | DriveInsight Privacy Policy - Aydın Öztürk | https://aydinozturk.com › … | **site** |
| 4 | Zapp Privacy Policy - Aydın Öztürk | https://aydinozturk.com › … | **site** |
| 5 | DriveInsight Gizlilik Politikası - Aydın Öztürk | https://aydinozturk.com › driveinsight › gizlilik | **site** |
| 6 | Zapp Gizlilik Politikası - Aydın Öztürk | https://aydinozturk.com › zapp › gizlilik | **site** |
| 7 | Modern bir tersane için uçtan uca ERP platformu kurmak | https://aydinozturk.com › tersane-erp-donusumu | **site** |
| 8 | Vessel telemetry that survives bad connectivity - Aydın Öztürk | https://aydinozturk.com › … | **site** |
| 9 | Building an end-to-end ERP platform for a modern shipyard | https://aydinozturk.com › s… | **site** |
| 10 | Rebuild or integrate: replacing a struggling Gantt - Aydın Öztürk | https://aydinozturk.com › r… | **site** |

**Okuma:** 3 turda da **10/10 sonuç aydinozturk.com sayfası** (ana sayfa EN+TR, 2 ürünün 4 gizlilik sayfası, 4 blog yazısı). Snippet örnekleri: "I build software products for shipbuilding and maritime operations…", "DriveInsight (the 'app') is a diagnostics app developed by Aydın Öztürk… (18 Eki 2026)", "Zapp… remote control app… (16 Eki 2026)". **Google indeksi sitenin ~10 sayfasını içeriyor** — #266'daki Bing "site: → 0 sayfa" bulgusunun aksine. (Sitemap 18 URL idi — #267; site: listesi en azından yaygın sayfaları gösteriyor, derin sayı garantisi değil.)

### 4.3 `aydinozturk` — SERP: https://www.google.com/search?q=aydinozturk&hl=tr&gl=tr

Sayfa başlığı: `aydinozturk - Google'da Ara`. Google sorguyu yeniden yorumladı: **"Sonuçlar şununla ilgili: aydin ozturk"** (+ "Yine de şu sorguyu ara: aydinozturk"). Varlık başlığı: **"Aydın Öztürk | Müzisyen"** (Knowledge Panel benzeri; klasik `#kp-wp` seçicisi bu düzende tutmuyor).

| # | Başlık | Görünen URL | İlinti |
|---|---|---|---|
| 1 | Aydın Öztürk (@aydinozturkkk) Instagram (5,5 B+ takipçi) | instagram | başka kişi |
| 2 | Aydın ÖZTÜRK — Türkiye Yazarlar Sendikası | https://turkiyeyazarlarsendikasi.org › aydin-ozturk | başka kişi (şair/yazar) |
| 3 | Aydın Öztürk Official — YouTube Music | https://music.youtube.com › … | başka kişi (müzisyen) |
| 4 | Yılların Zehir Süzgeci | Official Video © 2025 İber Prodüksiyon — YouTube | başka kişi (müzisyen) |
| 5 | (aynı video, 2. kart) | YouTube | başka kişi |
| 6 | Aydın Öztürk düet. Ebru Koşar - Hüzün Güzeli © 2025 — YouTube | YouTube | başka kişi (müzisyen) |
| 7 | (aynı düet, 2. kart) | YouTube | başka kişi |
| 8 | Aydın Öztürk - Ah Yüreğim (Sana Mecnun) — YouTube · Kalan Müzik (24 Haz 2022) | YouTube | başka kişi (müzisyen) |
| 9 | (aynı parça, 2. kart) | YouTube | başka kişi |
| 10 | Aydın Öztürk — Vikipedi | https://tr.wikipedia.org › wiki › Aydın_Öztürk | başka kişi (gazeteci, d. 1939) |
| 11 | Aydın Öztürk — Türk Edebiyatı İsimler Sözlüğü | https://teis.yesevi.edu.tr › madde-detay › ozturk-aydin | başka kişi (gazeteci) |
| 12 | Aydın Öztürk Bio — Ekoten | https://www.ekoten.com.tr › aydin-ozturk-bio | başka kişi (tekstil mühendisi, Ege Ünv. 1991) |

**Okuma:** 15/15 sonuç **başka kişi** (müzisyen baskın; Vikipedi'deki gazeteci, şair, akademisyen-yönetici). Bu kişinin sitesi/profilleri token sorgusunda **görünmüyor**; Google `aydinozturk`'u `aydin ozturk` ismine eşleyip "Müzisyen" varlığını ön plana almış.

### 4.4 `aydinozturk linkedin` — SERP: https://www.google.com/search?q=aydinozturk%20linkedin&hl=tr&gl=tr

Sayfa başlığı: `aydinozturk linkedin - Google'da Ara`. Öneri: "Bunu mu demek istediniz? aydin ozturk linkedin". **AI Bakışı VAR.**

**AI Bakışı (20:10 turu, birebir):** "LinkedIn üzerinde 'Aydın Öztürk' adıyla kayıtlı çok sayıda farklı profesyonel bulunuyor. Öne çıkan bazı profiller şunlardır: **Aydın Öztürk: Software Development Manager / Architect (UZMAR Technology)**; Aydın Öztürk: Otomotiv Profesyoneli (Doğuş Otomotiv); Aydın Öztürk: Cash Register Operator (Aka Otomotiv - Bursa); Aydın Öztürk: Network Uzmanı (Servus Bilgisayar A.Ş.); Av. Aydın…".
*(20:07 turu varyasyonu aynı 1. profil ile: "Aydın Öztürk – Software Development Manager / Architect | Expert in IoT & ERP Solutions | Digital Transformation Leader at UZMAR (LinkedIn Profili)".)*

| # | Başlık | Görünen URL | İlinti |
|---|---|---|---|
| AI | Öne çıkan profiller (AI Kutusu) | linkedin +1 | **kişi (1. sıradaki profil)** |
| 1 | 50+ "Aydın Ozturk" profili | https://tr.linkedin.com › Aydın › tr-7585-İstanbul,-İstanbul | LinkedIn dizini |
| 2 | 200+ "Aydin Özturk" profiles | https://www.linkedin.com › pub › dir › Aydin › ÖzTurk | LinkedIn dizini |
| 3 | AYDIN ÖZTÜRK - Aka Otomotiv'de Cash Register … | https://tr.linkedin.com › … | başka kişi |
| 4 | Aydin ÖZTÜRK - Servis Teknisyeni - Nordex Group Türkiye | linkedin | başka kişi |
| 5 | Aydın Öztürk posted on LinkedIn (Lincoln Electric Türkiye, 3 yıl önce) | linkedin | başka kişi |
| 6 | Aydın Öztürk - Network / Servus Bilgisayar A.Ş. | linkedin | başka kişi |
| 7 | aydın öztürk - Av. Aydın ÖZTÜRK - Avukat | linkedin | başka kişi |
| 8 | aydın öztürk - pişirici / ekmekçiler gıda | https://tr.linkedin.com › … | başka kişi |

**Okuma:** Kişinin LinkedIn'i `domain-history.md`'deki `linkedin.com/in/aydinozturk` URL'si **organik listede ilk ~12 sonuçta görünmedi**; Google AI Özeti'nde bu profilin başlığı ve "UZMAR Technology" atamasıyla **öne çıkan profillerin 1.'si** listelendi — yani Google, sorgu bağlamında doğru kişiyi tanıyor ama klasik SERP pozisyonu (dizin sayfası + başka kişilerin profilleri arasında) ilk sayfanın derinlerine düşüyor.

### 4.5 `aydinozturk twitter` — SERP: https://www.google.com/search?q=aydinozturk%20twitter&hl=tr&gl=tr

Sayfa başlığı: `aydinozturk twitter - Google'da Ara`. Öneri: "Bunu mu demek istediniz? aydin öztürk twitter". **AI Bakışı VAR.**

**AI Bakışı (20:10 turu, birebir):** "Aydın Öztürk adına ait **doğrulanmış veya aktif bir X (Twitter) hesabı bulunmamaktadır.** Ancak bu isimle veya benzer kullanıcı adlarıyla farklı sosyal medya platformlarında (Threads, Instagram vb.) profiller mevcuttur: Threads / Instagram: @_aydinozturk_ kullanıcı adıyla bilinen bir hesap…".

| # | Başlık | Görünen URL | İlinti |
|---|---|---|---|
| 1 | Aydın öztürk (aydinozturk88) - Profil | https://tr.pinterest.com › aydinozturk88 | başka kişi |
| 2 | Photo by Aydin Öztürk (@aydinozturk2635) · June 17, 2024 | instagram | başka kişi |
| 3 | Aydın Öztürk (@aydinozturk57) Instagram (230+ takipçi) | instagram | başka kişi |
| 4 | Çorabını kaybettin sanırım 😅 — Threads @_aydinozturk_ (2 hafta önce) | threads | başka kişi |
| 5 | OZAN ÖZTÜRK on X: "X'e dislike butonu geldi." | x | başka kişi |
| 6 | Günaydın 💛♥️ — Threads @_aydinozturk_ (ankara) | threads | başka kişi |
| 7 | Gün Aydı⛈️ — Threads @_aydinozturk_ (2 gün önce) | threads | başka kişi |
| 8 | aydın öztürk - İslam-tr Forum | https://islam-tr.org › uyeler › aydin-ozturk.100799 › about | başka kişi |

**Okuma:** Kişiye ait X/Twitter hesabı **yok** (AI Özeti de bunu söylüyor; başka kişinin X postu ve Threads/Pinterest/Instagram hesapları baskın). 8/8 **başka kişi**.

### 4.6 `uzmar technology` (kontrol: şirket) — SERP: https://www.google.com/search?q=uzmar%20technology&hl=tr&gl=tr

Sayfa başlığı: `uzmar technology - Google'da Ara`. **PAA VAR** ("Diğer sorular": Uzmar Denizcilik'in sahibi kimdir? / Uzmar tersanesi nerededir? / Uzmar denizcilik maaşları ne kadar? / Uzmar ne iş yapar?).

| # | Başlık | Görünen URL | İlinti |
|---|---|---|---|
| AI | UZMAR Gemi İnşa (AI Kutusu) | — | "UZMAR Gemi İnşa grubunun denizcilik endüstrisine özel ileri teknoloji ve yazılım çözümleri geliştiren teknoloji birimidir" |
| 1 | Careers — Uzmar Technology | https://www.uzmar.tech › c… | şirket (uzmar.tech) |
| 2 | CONTACT — Uzmar Technology | https://uzmar.tech › contact… | şirket (uzmar.tech) |
| 3 | News — Uzmar Shipyard | https://uzmar.com › News | şirket (uzmar.com) |
| 4 | Uzmar Römorkörcülük — Uzmar | https://www.uzmar.com.tr › iletisim | şirket (uzmar.com.tr, 1973 kurulu) |
| 5 | CV — Uzmar Shipyard | https://uzmar.com › … | şirket |
| 6 | UZMAR Is Bigger, Faster, Stronger! — News | https://uzmar.com › News | şirket |
| 7 | UZMAR \| Izmir — Facebook (3,1 B+ takipçi) | facebook | şirket |
| 8 | References — Uzmar Shipyard | https://uzmar.com › Pages | şirket |
| 9 | UZMAR GEMİ İNŞA SANAYİ VE TİC. A.Ş. — Saha İstanbul | https://www.sahaistanbul.org.tr › firma › uzmar-gemi-ins… | şirket (kayıt/üyelik) |
| 10 | YouTube / Instagram / LinkedIn / Facebook kartları | — | şirket sosyal medya |

**Okuma:** Kontrol başarılı — şirket sorgusunda 10/10 **şirket** (3 ayrı UZMAR varlığı: uzmar.com tersane, uzmar.com.tr römorkörcülük (farklı UZMAR markası), uzmar.tech teknoloji birimi; Kocaeli/Başiskele). Pipeline'ın "var olan marka → doğru sonuç" döndürdüğü teyit edildi.

---

## 5. Sınıflandırma özeti

| Sorgu | Toplam (ilk sayfa) | kişi | site | başka kişi | şehir | filler | LinkedIn dizin | Not |
|---|---|---|---|---|---|---|---|---|
| `aydinozturk.com` | 10 (+AI) | 0 | 0–1 (AI'da; A/B'ye göre organik 1.) | 10 | 0 | 0 | 0 | "aydinozturk.com.tr" önerisi |
| `site:aydinozturk.com` | 10 | 0 | **10** | 0 | 0 | 0 | 0 | karar bulgu |
| `aydinozturk` | 15 | 0 | 0 | 15 | 0 | 0 | 0 | "aydin ozturk" + "Müzisyen" varlığına eşlendi |
| `aydinozturk linkedin` | 8 (+AI) | **1 (AI 1. profil)** | 0 | 6 | 0 | 0 | 2 | organik listede in/aydinozturk görünmedi |
| `aydinozturk twitter` | 8 (+AI) | 0 | 0 | 8 | 0 | 0 | 0 | AI: "aktif X hesabı bulunmamaktadır" |
| `uzmar technology` | 10 (+AI+PAA) | 0 | 0 | 0 | 0 | 0 | 0 | kontrol: 10/10 şirket |

Şehir (Aydın ili) sonucu bu 6 sorguda hiç çıkmadı (Bing'de `"Aydın Öztürk"` sorgusunda görülen davranış Google'da bu sorgu setinde görülmedi).

---

## 6. Sonuç — "site/kişi Google'da görünüyor mu?"

- **Site: EVET, görünür.** `site:` sorgusu 10 sayfa döndürüyor; alan adı sorgusunda Google AI Özeti alan adını doğru kişiye atfediyor ("Resmi Web Sitesi"); A/B'ye göre ana sayfa alan adı sorgusunda 1. organik pozisyona da çıkabiliyor. #266/#268 raporundaki "Google'da varlık ~sıfır" çerçevesi **Bing'e özgüydü**; Google tarafı bunun aksini gösteriyor.
- **Kişi (doğrudan SERP pozisyonu): ZAYIF.** İsim token'ı `aydin ozturk`'a çözülüp müzisyen/gazeteci/şair profillerine gidiyor; kişiye ait klasik organik pozisyon ilk sayfalarda görülmedi.
- **LinkedIn: TANINIYOR AMA SIRA ALAMIYOR.** AI Özeti doğru profili "UZMAR Technology" ile 1. öne çıkan profil olarak listeliyor; organik listede dizin + 6 başka profil.
- **X/Twitter: YOK** (hem AI Özeti hem sonuçlar bunu doğruluyor).
- **Çakışma riski (Google tarafı): YÜKSEK.** "Aydın Öztürk" ismi bu sorgularda en az ~15 farklı kişiye ait canlı içeriğe (YouTube, Instagram ×7, X, Pinterest, Vikipedi, kitap sitesi) karşılık geliyor; bu kişinin farklılaşması alan adı/marka (UZMAR, aydinozturk.com) üzerinden mümkün.

## 7. Sınırlılıklar

- Sonuçlar **tarayıcının konumuna (TR host) ve oturumuna** (girişsiz, cookie'li geçmişi olan host tarayıcısı) ve **çekim anına** (2026-11-05 20:05–20:10 UTC) aittir; Google A/B'ye göre AI Kutusu içeriği ve ilk organik sonuç aynı sorguda turdan tura değişti (Bölüm 2).
- "Yaklaşık N sonuç" satırı bu SERP düzende metin olarak yok; sayı tahmini yapılmadı.
- `site:` listesi 1. sayfa (~10 sonuç); sitenin tam indeks büyüklüğü bu 10'la sınırlı değil (#267'deki 18 URL'lik sitemap ile karşılaştırılmalı).
- Knowledge Panel seçicisi (`#kp-wp`) Chrome 156'nın yeni düzeninde tutmuyor; "Aydın Öztürk | Müzisyen" varlık başlığı metin olarak doğrulandı (seçici ≠ varlığın yokluğu).
- Ham JSON çıktıları rapora eklenmedi; yeniden üretim: Bölüm 2'deki CDP ucu + `https://www.google.com/search?q=<sorgu>&hl=tr&gl=tr`.

## 8. Kaynaklar (erişim: 2026-11-05, UTC zamanlarıyla)

1. Google SERP `aydinozturk.com`: https://www.google.com/search?q=aydinozturk.com&hl=tr&gl=tr (3 tur: 20:07:33, 20:08:50, 20:10:07)
2. Google SERP `site:aydinozturk.com`: https://www.google.com/search?q=site:aydinozturk.com&hl=tr&gl=tr (3 tur: 20:07:39, 20:08:55, 20:10:12)
3. Google SERP `aydinozturk`: https://www.google.com/search?q=aydinozturk&hl=tr&gl=tr (3 tur: 20:07:45, 20:09:01, 20:10:18)
4. Google SERP `aydinozturk linkedin`: https://www.google.com/search?q=aydinozturk+linkedin&hl=tr&gl=tr (3 tur: 20:07:50, 20:09:07, 20:10:24)
5. Google SERP `aydinozturk twitter`: https://www.google.com/search?q=aydinozturk+twitter&hl=tr&gl=tr (3 tur: 20:07:56, 20:09:12, 20:10:29)
6. Google SERP `uzmar technology`: https://www.google.com/search?q=uzmar+technology&hl=tr&gl=tr (3 tur: 20:08:01, 20:09:18, 20:10:35)
7. Tarayıcı/CDP doğrulaması: `http://192.168.65.254:9222/json/version` → Chrome/156.0.8078.80 (2026-11-05 20:04 UTC, agent-3 konteynerinden)
8. Sınıflandırma kuralları ve Bing karşılaştırması: `research/aydinozturk.com/search-serp.md` (#266); indeks sinyalleri: `research/aydinozturk.com/search-indexing.md` (#267); önceki konsolide rapor: `reports/google-search-results.md` (#268)
9. Bilinen profiller (GitHub/LinkedIn) için: `research/aydinozturk.com/domain-history.md` (#263)

**Şeffaflık notu:** sekme temizliği sırasında konteynere ait olmayan, boş `about:blank` bir sekme (target `25801D78…`) de kapatıldı; bu sekmenin içeriği boştu, başka sekme (caddyserver.com) ve mevcut oturumlara dokunulmadı.
