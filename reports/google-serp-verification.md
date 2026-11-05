# Konsolide Rapor — Gerçek Google SERP Doğrulaması: Aydın Öztürk / aydinozturk.com

- **Görev:** #282 (Plan #279 — admin [3854]: "Google dan arayabilirsin")
- **Hazırlayan:** agent-6 · **Tarih:** 2026-11-05
- **Girdiler (değiştirilmedi, yalnızca konsolide edildi):**
  - `research/google-serp-verification/domain-queries.md` — #280, agent-3 (alan adı/marka sorguları, branch `t280-serp-domain`, 762622c)
  - `research/google-serp-verification/person-queries.md` — #281, agent-4 (kişi sorguları, branch `t281-serp-person`, fd81fa2)
  - `reports/google-search-results.md` — #268, önceki konsolide rapor (Bing best-effort + indeks sinyalleri); karşılaştırma tabanı
- **Dürüstlük çerçevesi:** Bu rapor yeni Google araması içermez. Her iki alt raporda ne yazıyorsa onu yazar; tüm bulgular 2026-11-05 20:06–20:10 UTC arasında **gerçek Chrome 156** (Windows host, CDP ucu `http://192.168.65.254:9222`) üzerinden gerçek Google SERP'inden alınmıştır. Alt raporlarda çelişki/eksik görülen tek nokta (§4, coğrafya notu) olduğu gibi aktarılmıştır.

---

## 1. TL;DR — admin'in sorusuna doğrudan cevap: Bu kişi/site GERÇEK Google SERP'inde görünüyor mu?

**Kısa cevap: Site EVET, kişi (isimle) HAYIR.**

1. **Site Google'da indeksli ve görünür — #268'deki "0 sonuç" tablosu motor bazlıymış.** `site:aydinozturk.com` sorgusu **10/10 aydinozturk.com sayfası** döndürdü (ana sayfa EN+TR, DriveInsight/Zapp gizlilik sayfaları, 4 blog/vaka yazısı). Aynı sorgu Bing'de alan adından **0 sayfa** döndürmüştü (#266 §4.7, #268 §2.1). Yani "Google'da varlık ~sıfır" çerçevesi **Bing'e özgüydü**; Google tarafı bunun tersini kanıtlıyor. [Kaynak: #280 §1.1, §4.2]
2. **Google, alan adını doğru kişiyle tanıyor.** `"aydinozturk.com"` sorgusunda Google AI Özeti (AI Bakışı) alan adını **"Resmi Web Sitesi"** olarak Aydın Öztürk'e (Yazılım Geliştirme Müdürü / Sistem Mimarı) atfediyor; `aydinozturk linkedin` sorgusunda AI Özeti'nin **öne çıkan 1. LinkedIn profili** "Aydın Öztürk: Software Development Manager / Architect (UZMAR Technology)". [Kaynak: #280 §1.2, §1.3, §4.1, §4.4]
3. **Kişi isimle aranmadığı sürece sıralanmıyor.** 10 sorgunun (6 alan adı + 4 kişi) hiçbirinde hedefe ait **sıralı organik pozisyon** istikrarlı olarak çıkmadı. `"Aydın Öztürk"` ve `aydinozturk` token sorguları **başka kişilere** kayıyor (15/15 ve 8/8) — Google ismi "aydin ozturk" olarak çözüp **müzisyen** varlığını ön plana alıyor. Tek kişi izi: (a) AI Özetlerinde doğru atıf, (b) `UZMAR` ve `github` kişi sorgularında **yalnızca görsel küçük resimlerinde** beliren LinkedIn künyesi. [Kaynak: #280 §4.3, §5; #281 §1.2–1.3, §5]
4. **Bing ile karşılaştırma — ne değişti / ne teyit oldu / ne kaldı:**

   | Konu | #268 (Bing, best-effort) | Gerçek Google (bu rapor) |
   |---|---|---|
   | Site `site:` sorgusunda | **0 sayfa** | **10 sayfa** (değişti — Google'da indeksli) |
   | Alan adı token'ı (`aydinozturk.com`) | 0 kişiye/siteye ait sonuç (filler) | AI Özeti doğru kişi; A/B'ye göre ana sayfa organik 1.'e de çıkabiliyor (değişti) |
   | İsim sorgusu `"Aydın Öztürk"` | 10/10 **Aydın ili (şehir)** | 10/10 **başka kişiler** (müzisyen/şair/gazeteci/akademisyen) — token çakışması doğrulandı, motor bazlı farklı yön |
   | İsim çakışması riski (§2.2 "doğrulanamadı") | ❌ doğrulanamamış açık soru | ✅ **doğrulandı ve ciddi** (kapanan gap) |
   | LinkedIn `/in/aydinozturk` | Hiçbir sorguda görünmüyor | Organik listede ilk sayfalarda hâlâ sıralanmıyor; AI Özeti 1. profil + görsel künyesi olarak beliriyor (kısmen değişti) |
   | X/Twitter | Sorgu filler döndürdü | **Hesap yok** — Google AI Özeti bunu açıkça söylüyor (yeni kanıtlı bulgu) |
   | Kişinin GitHub'ı | Görünmüyor | `"Aydın Öztürk" github` sorgusunda **sıralanmıyor**; yerine tireli **farklı** alan adı `aydin-ozturk.com` çıkıyor (teyit + yeni risk) |
   | `UZMAR` token'ı | — | Hedefe değil, **UZMAR Tersanesi**'ne kayıyor (yeni bulgu) |
   | GSC / indeks sayısının kesin cevabı | En kesin kanal (öneri §5.1) | **Hâlâ en kesin kanal** — `site:` ilk sayfası "en az 10 sayfa" der, tam sayısı ve URL durumu GSC'den alınır (§5.1) |

5. **Önceki "Google'a erişilemedi" durumu kapandı** (metot ve kısıtlar §4'te): 10/10 sorguda CAPTCHA/JS-challenge/consent yok; sonuçlar gerçek SERP'ten. Kapanan tablo satırı: #268 §4.3'teki "Google'da kişi/alan adı için ne çıktığı ❌ doğrulanamadı" artık **✅ doğrulandı** (IP/zaman kısıtıyla).

---

## 2. Alan adı / marka sorguları özeti (#280, agent-3)

Çekim: 6 sorgu × 3 tur, 2026-11-05 **20:07–20:10 UTC**; SERP'ler `https://www.google.com/search?q=<sorgu>&hl=tr&gl=tr`; Chrome 156, CDP ucu `192.168.65.254:9222`.

| Sorgu | İlk sayfa | Hedefe (kişi/site) ait | Okuma |
|---|---|---|---|
| `aydinozturk.com` | 10 + AI kutusu | AI'da site+kişi; organik 0–1 (A/B) | Organik liste 9/9 başka kişi (Instagram ×6, YouTube, X, kitap sitesi); "aydinozturk.com.tr" önerisi. Bir erken gözlemde (~20:05 UTC) ana sayfa **1. organik** görüldü → varyanta göre site ilk sayfaya girebiliyor |
| `site:aydinozturk.com` | 10 | **10** (karar bulgu) | 3 turda da 10/10 aydinozturk.com: ana sayfa EN+TR, 4 gizlilik, 4 vaka yazısı → Google indeksi sitenin ~10 sayfasını içeriyor |
| `aydinozturk` | 15 | 0 | Google'ı `aydin ozturk`'a eşliyor + "Aydın Öztürk \| Müzisyen" varlığı; 15/15 başka kişi (müzisyen baskın, Vikipedi'deki gazeteci, şair, akademisyen) |
| `aydinozturk linkedin` | 8 + AI kutusu | **AI: 1. öne çıkan profil = hedefin LinkedIn** ("…UZMAR Technology") | Organik listede `linkedin.com/in/aydinozturk` ilk ~12 sonuçta görünmedi; 2 LinkedIn dizin sayfası + 6 başka profil |
| `aydinozturk twitter` | 8 + AI kutusu | 0 (AI: "aktif X hesabı bulunmamaktadır") | 8/8 başka kişi (Pinterest/Instagram/Threads/X) |
| `uzmar technology` (kontrol) | 10 + AI + PAA | 0 (kontrol amaçlı) | 10/10 UZMAR varlıkları (uzmar.com tersane, uzmar.com.tr römorkörcülük, uzmar.tech teknoloji) → pipeline doğru çalışıyor |

İlginç ayrım: **alan adı token'ı hedefi sıralatmıyor ama Google'ın AI katmanı alan adını doğru kişiyi tanıyarak özetliyor** — yani klasik organik sıralama ve AI özeti iki ayrı görünüm veriyor. [Kaynak: #280 §4.1–§4.6, §5, §6]

## 3. Kişi sorguları + isim çakışması analizi (#281, agent-4)

Çekim: 4 sorgu, 2026-11-05 **20:06–20:08 UTC**; URL'ler #281 §2'de (URL-kodlu `hl=tr&gl=tr`).

| Sorgu | Sıralı organik (sayfa 1) | Hedefe ait | Okuma |
|---|---|---|---|
| `"Aydın Öztürk"` | 8 (+medya blokları) | 0 | 8/8 başka kişi; Google isim için "Şarkılar/Videolar/Görseller" medya blokları kurdu → **baskın anlam müzisyen** |
| `"Aydın Öztürk aydinozturk"` | 9 | 0 | Alan adı token'ı eklenince bile hedef sitesi sıralanmadı; çok sayıda kişisel FB/IG/TikTok + romancı |
| `"Aydın Öztürk" UZMAR` | ≈4 benzersiz | 0 sıralı; **1 LinkedIn görsel künyesi (yüksek güven)** | Sorgu UZMAR Tersanesi'ne (MarineDeal haberi) ve denizcilik sektöründeki başka kişilere kaydı; hedefin izi yalnız görsel küçük resimlerinde |
| `"Aydın Öztürk" github` | 9 | 0 sıralı; **1 LinkedIn görsel künyesi**; `github.com/aydinozturk` **sıralanmadı** | BT akademisyenleri, LinkedIn kurucu profili, tireli **farklı alan adı `aydin-ozturk.com`** (çıplak dizin), kişisel FB'ler |

**İsim çakışması ( #268 §2.2'nin açık sorusu — bu raporla cevaplandı):** Google "Aydın Öztürk"ü en az **4 ayrık kimlik kümesine** bağlıyor — (1) müzisyen (baskın: Spotify/YouTube Music/İber Prodüksiyon klipleri, IG `@aydinozturkkk`), (2) şair/yazar (d. 1955, Pertek/Tunceli; TYŞ, Antoloji, TEİS), (3) gazeteci (d. 1939; Vatan Gazetesi; **tr.wikipedia.org/wiki/Aydın_Öztürk**), (4) BT akademisyeni (Ege/İzmir/Yaşar Ü.; ResearchGate, 867 atıf) + çok sayıda kişisel sosyal profil (FB `@zorroaydin`, `@aydin.ozturk.*`, IG `@aydinozturk420`, İtalya'da yaşayan "Aydin Ozturk" vb.). Hedef bunların **hiçbirinin** organik sıralamasında yok. Motor farkı somut: Bing ismi şehre cevapladı (10/10 Aydın ili); Google ismi gerçekten taşıyan kişilere cevapladı (10/10 başka kişi) → **yanlış-atıf/kimlik karışma riski Google'da gerçek ve yüksek**; BT akademisyeni ve "Software Development Manager" LinkedIn'i teknik bağlamda karıştırılabilir. Alan adı token'ı korumuyor: Q2'de bile `aydinozturk.com` sıralanmadı, Q4'te **farklı** `aydin-ozturk.com` çıktı. [Kaynak: #281 §4.1–§4.4, §5, §6]

**Çapraz tutarlılık notu:** iki alt rapor birbirini doğruluyor (müzisyen baskınlığı, LinkedIn'in sıralanamayıp AI/görselde belirmesi, GitHub'ın çıkmaması). Tek gözlem farkı: #280'de `aydinozturk.com` alan adı sorgusunda bir A/B varyantında ana sayfa **1. organik** görülmüş; #281'de `"Aydın Öztürk aydinozturk"` kişiselleştirilmiş sorgusunda site sıralanmamış. Fark, alan adı token'ının (isim token'ına kıyasla) hedefi sıralatmada daha etkili olduğuna işaret ediyor; çelişki değil, varyant farklılığı.

---

## 4. "Google'a erişilemedi" durumunun kapanması — metot, zaman, kısıtlar

**Metot** (#280 §2, #281 §3):
- Gerçek **Chrome 156.0.8078.80** — Windows host'ta; CDP ucu `http://192.168.65.254:9222` (#274'te 5/5 konteynerde doğrulanmış uç; `/json/version` kanıtlı).
- chrome-devtools MCP `claude mcp list`'e göre "✔ Connected" idi ancak **SDK worker oturumlarında MCP araçları enumeration'da listelenmedi** → görev tanımındaki fallback izlendi: aynı Chrome'a **doğrudan CDP/WebSocket** ile sürüldü (`/json/new?about:blank` → `Page.navigate` → DOM okuma → `/json/close`). Aynı gerçek tarayıcı ve rendering; sonuç farkı yaratmaz.
- Her çekim **kendi yeni sekmesinde** yapıldı; mevcut sekmelere, admin'in oturumuna dokunulmadı; **giriş yok, form yok, sonuca tıklama yok** (URL'ler SERP breadcrumb'ından okundu — Chrome 156'da organik linkler `a[href^="/goto"]` opak).
- #280 şeffaflık notu: sekme temizliğinde konteynere ait olmayan **boş** `about:blank` bir sekme de kapatıldı; içeriği boştu, başka sekmeye dokunulmadı.

**Zaman:** #280: 6 sorgu × 3 tur, 20:07:33–20:10:35 UTC (ana kayıt 3. tur). #281: 4 sorgu, 20:06:53–20:08:08 UTC. Hepsi 2026-11-05.

**Engel durumu:** 10 sorguda (tüm turlar dahil) **CAPTCHA, JS-challenge ve consent sayfası görülmedi**. #268 §4.1'deki "Google (doğrudan) ❌" durumu **sade HTTP istemcisi içindi**; gerçek tarayıcı sorunsuz geçti.

**Kısıtlar (sonuçları okurken):**
1. **Konum/IP:** #281 §3'te kanıtlı — SERP arayüz başlıkları `hl=tr&gl=tr`'a rağmen NL ("Webresultaten") / NO ("Nettresultater") / ET ("Veebitulemused") göründü → ortak Chrome'un **çıkış IP'si temiz TR konut IP'si değil** (muhtemelen Avrupa kökenli). Sonuçlar "bu çıkış IP'sinden, bu tarih/saatte Google'ın döndürdüğü sayfa 1" olarak okunmalı; Türkiye'deki gerçek bir kullanıcının gördüğü SERP farklı (daha TR-kişi ağırlıklı) olabilir. (#280 §7 "TR host" ifadesi ile #281 §3 gözlemi farklı açılardan; arayüz-dili kanıtı daha somut olduğu için bu rapor #281'in uyarısını esas alır.)
2. **A/B varyasyonu:** aynı sorguda AI kutusu içeriği ve ilk organik sonuç turdan tura değişti (#280 §2); tek noktadan tek okuma riski azaltmak için her sorgu ≥2 kez çekildi.
3. **Yalnızca sayfa 1** ("Hakkında N sonuç" satırı bu SERP düzeninde metin olarak yok; derin indeks/paginate edilmedi).
4. **URL düzeyinde birebir doğrulama yok** (tıklama yok): LinkedIn künyesi "Software Development Manager / Architect … denizcilik teknolojileri" başlığı + UZMAR bağlamı + #267 §5'teki `Aydın Öztürk - UZMAR Technology | LinkedIn` title'ıyla **yüksek güvenle** hedefin profili olarak işaretlendi, birebir `/in/aydinozturk` URL'si okunmadı.
5. Knowledge Panel seçicisi (`#kp-wp`) Chrome 156'nın yeni düzeninde tutmuyor; varlıklar metin/ekran kaydı düzeyinde doğrulandı.
6. `site:` ilk sayfası (~10 sonuç) sitenin **tam** indeks büyüklüğünü sınırlamaz (#267'deki 18 URL'lik sitemap ile karşılaştırılmalı).

---

## 5. Sonuç ve öneriler (#268 §5 ile tutarlılık)

**Genel sonuç:** Görünmeme iki ayrı katmana ayrılıyor — (a) **site**: Google'da indeksli ve görünür (Bing'deki 0'ın aksine); (b) **kişi/kimlik**: çıplak isimle yapısal olarak kaybediyor (çoklu kimlik çakışması), hedefi kurtaran kanallar **alan adı token'ı + UZMAR bağlamı** ve bunların Google'ın **AI katmanında** doğru çözülmesi. #268'in "dış varlık ~sıfır" teşhisi kısmen revize edilmeli: dış varlık sıfır değil (LinkedIn indeksli, AI özetlerinde beliriyor) ama **sıralama getiren** dış varlık hâlâ yok.

| # | Öneri (#268) | Durum bu raporla |
|---|---|---|
| 5.1 | **GSC URL Inspection sahibi tarafından** (en kesin kanal) | **Hâlâ geçerli ve en kesin kanal.** `site:` ilk sayfası "en az 10 sayfa indeksli" diyor ama (i) 18 URL'den kaçının indeksli olduğunun kesin sayımı, (ii) sıralama/click verisi, (iii) Bing tarafının 0'ının nedeni yine GSC/Bing WMT'den alınır. Ayrıca bu raporun IP kısıtı (§4.1) nedeniyle "TR'deki kullanıcının ne gördüğü" sorusunu kapatmak için de en sağlam kanal. |
| 5.2 | Bing Webmaster Tools + sitemap | **Hâlâ geçerli** — Bing 0 sonucu kanıtlı (#266 §4.7) ve Google'la aradaki bu makas motor bazlı; Bing tarafı ayrı düzeltilmeli, sonuç aynı `site:` sorgusuyla ölçülebilir. |
| 5.3 | Kimlik zinciri (site↔GitHub↔LinkedIn tutarlılığı) | **Bulgularla güçlendi:** `"Aydın Öztürk" github` sorgusunda hedefin GitHub'ı **sıralanmıyor**, tireli farklı alan adı `aydin-ozturk.com` çıkıyor → GitHub about/website alanının `aydinozturk.com` ile tutarlı kalması ve siteden GitHub'a link eklenmesi şimdi kanıtlanmış bir boşluğu kapatıyor. LinkedIn unvanının "Aydın Öztürk (UZMAR Technology)" formatında tutarlı olması: AI katmanı bunu zaten doğru çözüyor (#280 §4.4), klasik sıralamada da işe yarayacak en güçlü token bu. |
| 5.4 | Taze niş içerik (shipyard ERP / filo telemetrisi) | **Hâlâ geçerli:** indeksli 10 sayfanın 4'ü blog/vaka yazısı ve Google onları sıralıyor (#280 §4.2) → taze içerik kanalının çalıştığının kanıtı; görünürlük artışı bu kanaldan gelir. |
| 5.5 | İsim netleştirmesi (alan adı bazlı kanal) | **Doğrulandı ve öncelik arttı:** isim sorgusu Google'da başka kişilere kaydı (Bing'de şehre kayıyordu); hedefi sıralatan tek istikrarlı token **alan adı** + **UZMAR** bağlamı. Çıplak isimle sıralama yapısal olarak zor; kaynaklarda ve profillerde "Aydın Öztürk (UZMAR Technology) — aydinozturk.com" kalıbının tekrarlanması önerilir. |
| — (yeni) | X/Twitter | **Hesap yok** (Google AI Özeti + sonuçlarla kanıtlı, #280 §4.5). #268'de önerilmemişti; görünürlük hedefinde yeni bir boş kanal olarak not ediliyor — öneri değil, tespit. |
| — (yeni) | `aydin-ozturk.com` (tireli alan adı) izi | `"Aydın Öztürk" github` sorgusunda çıplak dizin listesiyle sıralanıyor (#281 §4.4 satır 7). Sahipliği/ilişkisi belirsiz (bu raporun kapsamı dışı); kimlik karışmasında risk faktörü olarak izlenmeli. |

---

## 6. Kaynaklar

### 6.1 Birincil kanıt (gerçek Google SERP, Chrome 156, CDP `192.168.65.254:9222`)
**Alan adı/marka (#280, 2026-11-05 20:07–20:10 UTC, 3'er tur):**
1. `https://www.google.com/search?q=aydinozturk.com&hl=tr&gl=tr`
2. `https://www.google.com/search?q=site:aydinozturk.com&hl=tr&gl=tr`
3. `https://www.google.com/search?q=aydinozturk&hl=tr&gl=tr`
4. `https://www.google.com/search?q=aydinozturk+linkedin&hl=tr&gl=tr`
5. `https://www.google.com/search?q=aydinozturk+twitter&hl=tr&gl=tr`
6. `https://www.google.com/search?q=uzmar+technology&hl=tr&gl=tr`

**Kişi (#281, 2026-11-05 20:06–20:08 UTC):**
7. `https://www.google.com/search?q=%22Ayd%C4%B1n+%C3%96zt%C3%BCrk%22&hl=tr&gl=tr`
8. `https://www.google.com/search?q=%22Ayd%C4%B1n+%C3%96zt%C3%BCrk+aydinozturk%22&hl=tr&gl=tr`
9. `https://www.google.com/search?q=%22Ayd%C4%B1n+%C3%96zt%C3%BCrk%22+UZMAR&hl=tr&gl=tr`
10. `https://www.google.com/search?q=%22Ayd%C4%B1n+%C3%96zt%C3%BCrk%22+github&hl=tr&gl=tr`

### 6.2 Depo içi girdiler
- `research/google-serp-verification/domain-queries.md` — #280 (branch `t280-serp-domain`, commit 762622c)
- `research/google-serp-verification/person-queries.md` — #281 (branch `t281-serp-person`, commit fd81fa2)
- `reports/google-search-results.md` — #268 (önceki konsolide; karşılaştırma tabanı)
- `research/aydinozturk.com/search-serp.md` — #266 (metot + sınıflandırma şeması, Bing)
- `research/aydinozturk.com/search-indexing.md` — #267 (indeks sinyalleri)
- `reports/aydinozturk-com-research.md` — #264 (arka plan)
- Tarayıcı/CDP doğrulaması: Plan #274 (5/5 konteyner, Chrome/156.0.8078.80, `/json/version` kanıtlı)

### 6.3 Yöntem notu
Bu rapor yeni ağ isteği içermez; #280 ve #281 raporlarındaki ölçümlerin çelişkisiz konsolidasyonudur. Alt raporlar değiştirilmemiştir. Tek gözlem farkı (A/B varyantı, §3 not) ve tek coğrafya uyarısı (#281 §3, §4.1) olduğu gibi aktarılmıştır.
