# Konsolide Rapor: "Bu kişi Google'da nasıl görünür?" — Aydın Öztürk / aydinozturk.com

- **Görev:** #268 (Plan #265 — admin'in sorusu: "Bu kişinin Google'da arama sonuçlarıyla ilgili bir şey var mı?")
- **Hazırlayan:** agent-6 · **Tarih:** 2026-11-05
- **Girdiler (değiştirilmedi, yalnızca konsolide edildi):**
  - `research/aydinozturk.com/search-serp.md` — #266, agent-3 (best-effort SERP, main)
  - `research/aydinozturk.com/search-indexing.md` — #267, agent-5 (indekslenme sinyalleri, main, merge aa4f997)
  - `reports/aydinozturk-com-research.md` — #264, agent-6 (arka plan: kişi/site/alan adı özeti)
- **Dürüstlük çerçevesi:** Google SERP'i bu ortamdan **doğrudan alınamıyor** (JS challenge — kanıt Bölüm 4). Aşağıdaki "Google'da ne çıkar?" cevabı bir iddia değil; **kanıtlanabilen en yakın iki şeye dayanır:** (a) tek çalışır motor olan Bing'in 2026-11-05'teki sonuçları (#266) ve (b) sitenin indekslenmeye açık/kapalı olduğuna dair nesnel sinyaller (#267). Google'a özel doğrulama bu ortamda **doğrulanamadı**; tek kesin Google-doğrulama kanalı Bölüm 5.1'de verilmiştir.

---

## 1. TL;DR (admin'in sorusuna doğrudan cevap)

1. **"Bu kişinin Google'da ne çıkar?" sorusuna bu ortamdan kesin cevap verilmedi (verilemedi).** Google'a doğrudan erişim yok; cevap tek çalışır motor (Bing TR) + nesnel indeks sinyalleriyle "en iyi çaba" düzeyindedir. [Kaynak: #266 §3, #267 §6.1]
2. **Siteden bahseden gerçek arama sonucu bulunamadı.** Bing'de 7 sorgu × 69 organik sonucun **0'ı** kişiye veya `aydinozturk.com`'a aitti; `site:aydinozturk.com` operatörü bile alan adından **0 sayfa** döndürdü. Kişinin bilinen LinkedIn ve GitHub profilleri hiçbir sorguda organik sonuç olarak görünmedi. [Kaynak: #266 §1, §7]
3. **İsimle arama, bu kişiyi değil "Aydın" şehrini döndürüyor.** `"Aydın Öztürk"` sorgusunda Bing 10/10 sonuçta Aydın ili (belediye, Vikipedi, haber) içeriği listelemiş; "Öztürk" soyadı eşleştirilmemiş. Bing'de *farklı* bir Aydın Öztürk kişisi de görünmedi — ancak bu, Google'da farklı kişilerin çıkmayacağını kanıtlayan bir bulgu **değil** ("Aydın Öztürk" çok yaygın bir Türk adı-soyadıdır; Google doğrulaması yapılamadı). [Kaynak: #266 §4.1, §6]
4. **Site indekslenmeye teknik olarak TAMAMEN AÇIK** — sorun "engellenmek" değil. `robots.txt`: `Content-Signal: search=yes` + `Allow: /` (Googlebot/Bingbot'a kısıtlama yok; yalnız 31 AI eğitim botu engelli), 18 URL'lik yayında sitemap, DNS'te Google Search Console doğrulaması TXT kaydı mevcut. [Kaynak: #267 §1, §2, #264 §3.1]
5. **Görünürlük bugün zayıf ve dış varlık neredeyse sıfır:** siteden bahseden/linke eden hiçbir dış kaynak bulunamadı; Wayback'te 2022'den beri yeni capture yok; LinkedIn profili bile Bing'in indeksi görünmüyor. Yani kişi, "aramada görünür" yapılandırmaya sahip olmasına rağmen, onu dışarıdan bağlayan içerik/etki (backlink, taze içerik, profil bağlantıları) henüz oluşmamış görünüyor. [Kaynak: #266 §7, #267 §4, §5]

---

## 2. Best-effort arama bulguları (Bing TR, 2026-11-05 ~16:30 UTC)

Kaynak: #266. Tüm sonuçlar `bing.com/search?q=…&setlang=tr&cc=tr` üzerinden curl + masaüstü UA ile alındı; çözümleme ve filler filtreleme metodu #266 §2 ve §5'te ayrıntılıdır.

### 2.1 Sorgu başına özet

| Sorgu | Sonuç | Kişiye/siteye ait | Şehir (Aydın ili) | Filler (alakasız) | Okuma |
|---|---|---|---|---|---|
| `"Aydın Öztürk"` | 10 | 0 | 10 | 0 | Bing "Öztürk" token'ını düşüp "Aydın" şehrini cevaplamış (belediye, Vikipedi, valilik, haber) |
| `"aydinozturk"` | 10 | 0 | 0 | 10 | Uludağ Üniversitesi popüler içeriği |
| `"aydinozturk.com"` | 9 + 10 (2. sayfa) | 0 | 0 | 19 | s1: memurlar.net forumu; s2: "Çırpınırdı Karadeniz" mp3 siteleri — filler seti sayfadan sayfaya değişiyor |
| `"Aydın Öztürk aydinozturk"` | 10 | 0 | 10 | 0 | İlk sorguyla birebir aynı sonuçlar |
| `"aydinozturk linkedin"` | 9 | 0 | 0 | 9 | Farklı dillerde YouTube yardım sayfaları; **sitede linkli LinkedIn profili bile çıkmıyor** |
| `"aydinozturk twitter"` | 10 | 0 | 0 | 10 | Windows "program ekle/kaldır" yardım içeriği |
| `"site:aydinozturk.com"` (ek) | 10 | **0 sayfa alan adından** | 0 | 10 | Alan adına doğrudan hedefli sorgu bile 0 → Bing indeksinde görünür varlığın olmadığının en net göstergesi |
| **TOPLAM** | **69** | **0** | 20 | 49 | Karar: **YOK** (#266 §7) |

Kontrol sorgusu `"ankara"` aynı metotla doğru ve alakalı sonuç döndürdü → pipeline sorunu yok; boşluk Bing'in bu sorgulara verdiği cevaptır. [Kaynak: #266 §4 (sonuç tabloları), §7, Kontrol]

### 2.2 İsim çakışması analizi

- Bing'de kişi hakkında sonuç **0** olduğuna göre *farklı* Aydın Öztürk'lerin sonuçları da görünmüyor (0/10). Bu bir "çakışma yok" kanıtı değil; "Bing bu sorguya kişi içeriği döndürmedi" tespitidir. [Kaynak: #266 §6]
- **Risk (kanıt değil, gerekçeli not):** "Aydın Öztürk" Türkiye'de yaygın bir isim; Google'a erişim olmadığı için, Google'da farklı Aydın Öztürk kişilerinin (LinkedIn profesyonelleri, haberlerde geçen isimler, akademisyenler) ilk sayfalarda çıkıp bu kişiyle karışabileceği **doğrulanamadı**. Ayrıca bu kişinin kendisinin Google'da hiçbir sayfasının sıralanamayacağı da Bing verisiyle gösterilmiş değil — yalnız Bing için 0 sonuç kanıtlanmıştır. [Kaynak: #266 §6, §8]

### 2.3 Bilinen profillerin SERP görünümü

Kişinin kimliğine bağlanan iki profil — LinkedIn (`linkedin.com/in/aydinozturk`) ve GitHub (`github.com/aydinozturk`, hesap 2016'dan beri, 17 repo) — `… linkedin` ve `… twitter` dahil hiçbir Bing sorgusunda organik sonuç olarak görünmedi. [Kaynak: #266 §1, §4.5; #264 §2, §5.3]

---

## 3. İndekslenme ve görünürlük sinyalleri (nesnel)

Kaynak: #267 (tüm istekler 2026-11-05, curl ile alındı).

| # | Sinyal | Değer | Anlam / kaynak |
|---|---|---|---|
| 1 | robots.txt — normal arama botları | **AÇIK**: `Content-Signal: search=yes, ai-train=no, use=reference` + `Allow: /` | Googlebot/Bingbot'a kısıtlama yok; site "aramada görün, AI'a eğitme" politikasını bilinçli seçmiş. `https://aydinozturk.com/robots.txt` (HTTP 200) [Kaynak: #267 §1] |
| 2 | robots.txt — AI eğitim botları | **ENGELLİ**: 31 bot `Disallow: /` (CCBot, GPTBot, ClaudeBot, Google-Extended, GoogleOther, Amazonbot…) | Yalnızca model eğitimi/RAG botları; normal arama indeksini etkilemez [Kaynak: #267 §1] |
| 3 | Sitemap | **YAYINDA**: 1 alt sitemap, **18 URL** (EN kök + `/tr/`, 6 EN + 5 TR vaka, 4 gizlilik, kökler), `<lastmod>` yok | `https://aydinozturk.com/sitemap-index.xml` (HTTP 200) [Kaynak: #267 §2] |
| 4 | CommonCrawl | 13 crawl'da (Eki 2019 → Eki 2026, en güncel CC-MAIN-2026-43 dahil) kesin **"No Captures found"**; 3 crawl (2026-25/30/34) 504 ile belirsiz | ⚠️ Olumsuz indeks sinyali **değil**: CCBot robots ile disallow edilmiş → CC'de hiç görünmemesi beklenen durum [Kaynak: #267 §0 ayrık not, §3] |
| 5 | Wayback Machine | 106 ham capture: 2005 (yalnız robots.txt) → 2010 (ilk ana sayfa; farklı kişi) → 2021; **2022-2024 ve 2026: sıfır**; 2025: tek `warc/revisit` işaretçisi | En son gerçek ana sayfa capture'ı 2021-11-25; güncel sitenin (vaka sayfalı hâlinin) arşiv görüntüsü yok. Google indeks sinyali değil ama "dış etki zayıf" göstergesi [Kaynak: #267 §4] |
| 6 | Sosyal: LinkedIn | **Gerçek, public profil**: HTTP 200, `Aydın Öztürk - UZMAR Technology | LinkedIn` | Siteden çıkan tek dış sosyal link; başlık düzeyinde doğrulandı [Kaynak: #267 §5] |
| 7 | Diğer sosyal (X, GitHub, FB, IG, YouTube, Medium) | Sitede **link yok** (GitHub hesabının varlığı #264'te doğrulandı ama site onu referans vermiyor) | Dış kimlik zinciri yalnız LinkedIn + GitHub API üzerinden [Kaynak: #267 §5, #264 §2] |
| 8 | Google Search Console doğrulaması | DNS'te `google-site-verification` TXT kaydı mevcut | Site sahibinin GSC hesabını doğruladığına işaret — Bölüm 5.1'in ön koşulu [Kaynak: #264 §3.1, §5.3] |

> **⚠️ Ayrık not (yorumlamada kritik):** *"CommonCrawl'de yok" ≠ "Google'da indeksli değil."* CCBot robots ile engellendiği için bu yokluk bilinçli ve indeks sinyali taşımaz. Öte yandan `search=yes` + `Allow: /` + 18 URL'lik sitemap, sitenin arama indekslemeye **tamamen izin verici** olduğunu kanıtlar. "İndeksli mi?" sorusunun kendisi ancak motorun kendi indeksiyle yanıtlanabilir — bu ortamda yapılabildiği kadarıyla yanıt Bing'den geldi: `site:` → 0 sayfa. [Kaynak: #267 §0, #266 §4.7]

Küçük tutarsızlık notu: arka plan raporu (#264) sayfaları 17, #267'nin taze sitemap taraması 18 URL sayar (gizlilik sayfası eklenmesi/düşmesi gibi nedenlerle değişmiş olabilir); bu rapor #267'nin 2026-11-05 tarihli sayımını kullanır.

---

## 4. Metot ve sınırlılıklar

### 4.1 Arama motoru erişilebilirliği (agent-2 tarafından 2026-11-05 doğrulandı; yeniden test edilmedi)

| Motor / kanal | Durum | Neden |
|---|---|---|
| Google (doğrudan) | ❌ alınamıyor | JS challenge (bot kontrolü); sade HTTP istemcisiyle sonuç alınamıyor |
| DuckDuckGo (html/lite) | ❌ | "anomaly" (güvenlik) ekranı |
| SearXNG public instance'ları | ❌ | 429 / browser-check |
| Mojeek | ⚠️ | erişilebilir ama bu nadir sorgulara boş döndürüyor |
| WebSearch (MCP aracı) | ❌ | arka uç API 400 — araç bu ortamda kırık |
| **Bing HTML (curl + masaüstü UA)** | ✅ çalışıyor | tek kullanılabilir kanal; nadir sorgularda filler davranışı var (aşağı) |

[Kaynak: #266 §3; doğrulama agent-2, 2026-11-05]

### 4.2 Bing filler uyarısı

Bing, Türkçe indeksinde eşleşme bulamadığı nadir token'larda (`aydinozturk`, `aydinozturk.com`) "sonuç yok" demek yerine alakasız "popüler içerik" listeliyor; filler seti sayfadan sayfaya değişiyor (aynı sorgunun s1 ve s2'si farklı filler seti döndürdü). Bu davranış "Bing'de yok" bulgusunu **güçlendirir** (site `site:` sorgusunda bile yok) ama "Google'da yok" için kanıt teşkil etmez — Google'ın bu nadir sorgularda farklı davranması mümkündür. Filtreleme kuralı: başlıkta/URL'de/snippet'ta sorgu token'ı geçmeyen sonuç filler sayıldı; sayfadaki tüm `aydinozturk` metinleri sorgu yansımasıydı, hiçbir organik sonuçta geçmiyordu. [Kaynak: #266 §5]

### 4.3 Kanıtlanan vs. doğrulanamayan

| Konu | Durum |
|---|---|
| Bing TR'nin 2026-11-05'te bu sonuçları verdiği | ✅ kanıtlandı (69 sonuç tek tek sınıflandırıldı; kontrol sorgusu geçildi) |
| Site'nin indekslenmeye açık yapıya sahip olduğu | ✅ kanıtlandı (robots/sitemap/GSC TXT) |
| LinkedIn profilinin gerçek ve public olduğu | ✅ başlık düzeyinde kanıtlandı (içerik analizi yapılmadı) |
| Google'da kişi/alan adı için ne çıktığı | ❌ **doğrulanamadı** (motor erişilemedi) — Bölüm 5.1'de sahibi tarafından doğrulanabilir kanal verildi |
| Google'da farklı "Aydın Öztürk" kişilerinin çıkıp çıkmayacağı | ❌ doğrulanamadı (yaygın isim; risk notu §2.2) |
| Google indeksinde 18 URL'den kaçının indeksli olduğu | ❌ doğrulanamadı (GSC URL Inspection gerekir — §5.1) |
| Trafik hacmi | ❌ alınamadı (SimilarWeb bot korumalı; #264 §5.3) |

Sonuç listeleri çekim anına (2026-11-05 ~16:30 UTC) ve `setlang=tr&cc=tr` bağlamına bağlıdır; sayfa 1 dışında derin indeks yokluğu tam garanti vermez (ancak `site:` sorgusu derin aramayla aynı şeyi söyler). [Kaynak: #266 §8]

---

## 5. Pratik çıkarımlar ve öneriler

Bulgulara dayanan çıkarım: **"Görünmeme"nin nedeni teknik bir engel (robots/engelleme) değil; nedeni dış varlığın zayıflığı** — sitenin arama indekslerinde kayda değer bir izi yokken, onu dışarıdan linkeleyen/bahseden içerik de bulunamadı (#266 §7: 0 sonuç; #267 §4: 2022'den beri arşiv hareketi yok; #264: 18 sabit URL, blog yok). Öneriler bu bulgulara bağlanır:

### 5.1 Google doğrulamasını sahibi yapmalı (sorunun kesin cevabı tek bu kanalla alınır)

DNS'te `google-site-verification` kaydı zaten mevcut (#264 §3.1) → GSC hesabı doğrulanmışa benziyor. Yapılacaklar:
1. **GSC'de "URL İnceleme" (URL Inspection)** ile ana sayfa ve 6 vaka sayfası tek tek kontrol edilsin: "Google'da indeksli mi?" sorusunun tek kesin cevabı buradan gelir (bu ortamdan alınamazdı, §4.3).
2. **Sitemap gönderimi** (`/sitemap-index.xml`) — henüz gönderilmediyse indekslenmeyi hızlandırır.
3. GSC'de indeksli URL sayısı sıfıra yakınsa, URL'ler için **index istemi** verilsin.

### 5.2 Bing tarafı bu ortamdan doğrulanabilir ve 0 sonuç kanıtlı

`site:aydinozturk.com` → 0 sayfa (#266 §4.7). **Bing Webmaster Tools**'da site eklenip sitemap gönderilmeli; bu, Google doğrulamasını beklemeksizin kanıtlanmış bir boşluğu kapatır ve Bing tarafının düzelip düzelmediğini aynı `site:` sorgusuyla ölçülebilir hale getirir.

### 5.3 Kimlik zinciri tamamlanmalı (bulgu: siteden yalnız LinkedIn çıkıyor)

- GitHub hesabı (`github.com/aydinozturk`, 2016'dan beri, 17 repo — #264 §5.3) sitede referans verilmiyor; GitHub profili zaten ad + "aydinozturk.com" blog alanı içeriyor. Siteden GitHub'a link eklemek ve GitHub bio/blog alanının tutarlı kalması, `aydinozturk github` benzeri sorgular için en güçlü var olan dış varlıktır.
- LinkedIn profili public ve gerçek (#267 §5); sitede linkli olmasına rağmen Bing'in indeksi görünmüyor (§2.3) → profilin tam URL'siyle dış mecralarda (ör. GitHub about, vaka metinlerinde "Aydın Öztürk (UZMAR)") tekrarlanması, profillerin indekslenmesine yardımcı olabilecek tek pratik lehe faktördür.

### 5.4 Taze, niş içerik (bulgu: 18 sabit URL, blog yok, 2022'den beri arşiv hareketi yok)

Site'nin görünürlüğü "yeni dış bağlantı" ve "taze içerik" olmadan kendiliğinden artmaz; mevcut bulgular buna işaret ediyor (§5 başlangıcı). Arka plan raporunun zaten önerdiği, arama görünürlüğü hedefli niş içerik (ör. shipyard ERP / filo telemetrisi temalı yazılar — #264 §7.10) bu boşluğa doğrudan girer. Spekülatif olmayan gerekçe: bugün hiçbir dış kaynakta siteden bahseden içerik bulunamadı, dolayısıyla görünürlüğün kaynağı yalnız site'nin kendi taze URL'leri olabilir.

### 5.5 İsim netleştirmesi (bulgu: `"Aydın Öztürk"` sorgusu şehrini döndürüyor)

Yaygın isim + şehir token çakışması (§2.2), kişi ismiyle aramanın bu kişinin sitesini geri getirmesi için zayıf bir senaryo olduğunu gösteriyor. Buna karşılık `aydinozturk.com` / alan adı bazlı aramalar net bir kimlik kanalıdır: sitemap, title (`Aydın Öztürk — …`) ve LinkedIn unvanı alan adıyla tutarlıdır. Öncelik, alan adı token'ının indekslerde var olması (5.1/5.2) olmalıdır; kişisel isim sorgusunda sıralama, bu adı taşıyan çok sayıda kişi yüzünden yapısal olarak zordur (doğrulanamayan risk, §2.2).

---

## 6. Kaynaklar

### 6.1 Bu rapora girdi olan belgeler (depo içinde, main)
1. `research/aydinozturk.com/search-serp.md` — #266, agent-3 (Bing TR SERP, 7 sorgu/69 sonuç, 2026-11-05)
2. `research/aydinozturk.com/search-indexing.md` — #267, agent-5 (robots/sitemap/CommonCrawl/Wayback/sosyal, 2026-11-05)
3. `reports/aydinozturk-com-research.md` — #264, agent-6 (site/teknik/SEO/alan adı arka planı)
4. Oda notları / motor erişilebilirliği doğrulaması: agent-2, 2026-11-05 (Plan #265 kapsamı)

### 6.2 Alt raporlarda referanslı birincil kaynaklar (erişim: 2026-11-05)
- Bing SERP URL'leri (7 sorgu + kontrol): `https://www.bing.com/search?q=…&setlang=tr&cc=tr` — tam liste #266 §9
- `https://aydinozturk.com/robots.txt` · `https://aydinozturk.com/sitemap-index.xml` → `sitemap-0.xml` — #267 §7
- CommonCrawl index API: `https://index.commoncrawl.org/<ID>-index?url=aydinozturk.com*&output=json` (13 crawl) — #267 §3, §7
- Wayback CDX: `http://web.archive.org/cdx/search/cdx?url=aydinozturk.com&matchType=domain&…` (106 capture) — #267 §4, §7
- `https://www.linkedin.com/in/aydinozturk` (HTTP 200, public) — #267 §5
- DNS TXT (`google-site-verification`) ve RDAP/alan adı geçmişi — #264 §3.1, §5

### 6.3 Yöntem notu
Bu rapor yeni ağ isteği içermez; tüm bulgular yukarıdaki üç belgedeki, 2026-11-05'te tek oturumda alınan ölçümlerin çelişkisiz konsolidasyonudur. Alt raporlar değiştirilmemiştir. Yalnızca bir tutarsızlık notu eklendi: sitemap sayımı 17 (#264) vs 18 (#267) — #267'nin taze sayımı esas alındı (§3).
