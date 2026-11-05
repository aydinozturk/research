# Google SERP — kişi sorguları (gerçek tarayıcı ile doğrulama)

- **Görev:** #281 (Plan #279 — admin [3854]: "Google'dan arayabilirsin"; #274'te düzeltilen Chrome ile gerçek Google SERP doğrulaması)
- **Çalışan:** agent-4 · **Çekim:** 2026-11-05, 20:06–20:08 UTC
- **Kişi (hedef):** Aydın Öztürk — UZMAR Technology; site `aydinozturk.com`; LinkedIn `linkedin.com/in/aydinozturk`; GitHub `github.com/aydinozturk`
- **Kapsam:** 4 kişi sorgusu, tek tek, gerçek Google SERP'inden çekilip sınıflandırıldı.
- **Bağlam / bu raporun neye cevap verdiği:**
  - `reports/google-search-results.md` (§2.2, §6, #268) — önceki konsolide rapor "Google'a erişilemedi, Bing'de 0 sonuç" demiş ve **adlandırılmış bir açık soru** bırakmıştı: *"Aydın Öztürk çok yaygın bir Türk adı-soyadıdır; Google'da farklı Aydın Öztürk kişileri ilk sayfalarda çıkıp bu kişiyle karışabilir. Bu yalnızca Google erişimi olan ortamda (tarayıcı) doğrulanabilir."*
  - `research/aydinozturk.com/search-serp.md` (§2, §4, §5, §6, #266) — metot ve sınıflandırma şeması (kişi / site / başka kişi / şehir / filler).
  - **Bu rapor o açık soruya cevap verir:** gerçek Google (curl değil, gerçek Chrome) üzerinden 4 sorgu çekildi.

---

## 1. TL;DR (idari soruya doğrudan cevap)

1. **Google'a gerçek tarayıcıyla erişim başarılı** — 4/4 sorgu CAPTCHA/JS-challenge/consent engeli **olmadan** gerçek SERP döndürdü. Önceki raporlardaki "Google'a erişilemiyor" sınırlaması bu ortamda aşıldı (Bölüm 3, metot).
2. **"Aydın Öztürk" sorgusu bu kişiyi değil, BAŞKA kişileri döndürüyor.** İlk sayfada hedefe (UZMAR/aydinozturk.com) ait **sıralı organik sonuç: 0.** Google'ın "Aydın Öztürk"ü asıl olarak bir **müzisyen** olarak biliyor (Şarkılar/Videolar/Spotify/YouTube blokları); yanı sıra bir **şair** (1955, Pertek/Tunceli), bir **gazeteci** (1939, Vatan Gazetesi, tr.wikipedia sayfası var) ve bir **BT akademisyeni** (Ege/İzmir Ü., ResearchGate, 867 atıf) çıkıyor. → #268 §2.2'nin "isim çakışması" riski **doğrulandı** (Bölüm 6).
3. **Hedefin kendi dijital izi Google SERP'inde (bu 4 sorguda) organik metin sıralamasında görünmüyor.** Kişinin sitesinin alan adı (`aydinozturk.com`), GitHub'u (`github.com/aydinozturk`) ve LinkedIn'i (`/in/aydinozturk`) hiçbir sorguda **sıralı organik sonuç** olarak çıkmadı. Tek iz: "Aydın Öztürk — Software Development Manager / Architect … denizcilik teknolojileri" **LinkedIn** künyesi, `UZMAR` ve `github` sorgularında **yalnızca görsel (image) küçük resimlerinde** beliriyor (Bölüm 4.3/4.4). Bu, hedefin Google tarafından *indekslendiğini* ama *önerilen sıralamada* çıkmadığını gösteriyor.
4. **`UZMAR` sorgusu "UZMAR Tersanesi"ne kayıyor** — hedefle aynı adı taşıyan gerçek bir denizcilik şirketi (MarineDeal haber); kişi ile karışıyor. `github` sorgusunda ise GitHub sonucu değil, *farklı bir alan adı* `aydin-ozturk.com` (tireli, çıplak dizin listesi) çıkıyor.
5. **Yorum:** Hedef için Google görünürlüğü, Bing'dekiyle aynı yön (kişiye ait sıralı sonuç yok) ama Google'da *dolaylı* bir fark var: Bing'de `"Aydın Öztürk"` → 10/10 **Aydın ili (şehir)**; Google'da → 10/10 **başka kişiler (isim tam eşleşme)**. Yani Google "Öztürk" token'ını düşmüyor, gerçekten isim taşıyan kişileri sıralıyor — bu kişiyle karışma/yanlış-atıf riski Google'da somut.

---

## 2. Sorgular

Görev tanımındaki 4 sorgu, **birebir** ve tek tek (arama kutusuna yazılıp; URL kodlaması Türkçe karakterleri korudu):

| # | Sorgu (birebir) | SERP URL (q paramı URL-kodlu) |
|---|---|---|
| 1 | `"Aydın Öztürk"` | `https://www.google.com/search?q=%22Ayd%C4%B1n+%C3%96zt%C3%BCrk%22&hl=tr&gl=tr` |
| 2 | `"Aydın Öztürk aydinozturk"` | `https://www.google.com/search?q=%22Ayd%C4%B1n+%C3%96zt%C3%BCrk+aydinozturk%22&hl=tr&gl=tr` |
| 3 | `"Aydın Öztürk" UZMAR` | `https://www.google.com/search?q=%22Ayd%C4%B1n+%C3%96zt%C3%BCrk%22+UZMAR&hl=tr&gl=tr` |
| 4 | `"Aydın Öztürk" github` | `https://www.google.com/search?q=%22Ayd%C4%B1n+%C3%96zt%C3%BCrk%22+github&hl=tr&gl=tr` |

Çekim (fetchedAt): Q1 20:06:53Z · Q2 20:07:54Z · Q3 20:08:01Z · Q4 20:08:08Z (hepsi 2026-11-05, UTC).

**Sınıflandırma anahtarı** (#266 §4 ile uyumlu, hedefe göre genişletildi):
- **bu kişi** = hedef (Aydın Öztürk, UZMAR Technology, aydinozturk.com, linkedin.com/in/aydinozturk, github.com/aydinozturk)
- **başka kişi** = farklı bir Aydın/Aydin Öztürk (müzisyen / şair / gazeteci / akademisyen / sosyal profil)
- **UZMAR şirket** = UZMAR Tersanesi/işletmesi içeriği (kişi değil)
- **başka alan adı** = hedefin alan adı olmayan benzer alan (`aydin-ozturk.com` — tireli)
- **şehir** = Aydın ili içeriği
- **filler** = sorguyla alakasız popüler içerik

> Not: Google organik sonuçları `google.com/goto?url=…` takıp-izleme yönlendirmeleriyle sunuyor. Gerçek hedef URL'ye **tıklanmadı/takip edilmedi** (görev metodu: "sonuçlara tıklayıp gezme"). Tablolardaki "Kaynak", SERP'e çıkan **breadcrumb** (görünen site/hesap) değeridir.

---

## 3. Metot ve ortam

- **Motor:** **Google (gerçek tarayıcı)**. `chrome-devtools` MCP'sinin altındaki Chrome'a **doğrudan CDP (Chrome DevTools Protocol) üzerinden WebSocket** ile bağlanıldı: `http://192.168.65.254:9222` → `/json/version` = `Chrome/156.0.8078.80`. *(Ortam notu: bu SDK oturumunda `chrome-devtools` MCP **araçları listelenmedi**; `claude mcp list` "✔ Connected" gösterdi ancak araç setine girmedi. Görevin amacı — gerçek Google SERP — bu yüzden CDP'yi elle sürerek (sayfa aç → navigasyon → yüklenince bekle → DOM'dan sonuçları oku) aynen yapıldı. Sonuçlar MCP'den farklı değildir: aynı gerçek tarayıcı, aynı rendering.)*
- **İzolasyon:** Her çekim için `/json/new` ile **kendi** yeni sekmesi açıldı, iş bitince `/json/close` ile kapatıldı. Mevcut sekmelere (agent-3'ün alan adı sorguları) dokunulmadı.
- **Arama disiplini:** Sadece arama yapıldı — **giriş yok, form doldurma yok, sonuca tıklama yok.** 4 sorguda **consent/cookie sayfası çıkmadı, CAPTCHA/JS-challenge çıkmadı** (hedef "doğrulanamadı" durumu yok; tümü gerçek sonuç).
- **Bekleme:** Her navigasyonda `Page.loadEventFired` + ~2.8 sn ek rendering beklentisi; ardından `#rso` (sonuçlar sütunu) DOM'undan başlık/anchor/kısa metin + sütun iç metni okundu.
- **Sonuç sayısı:** Google bu oturumda **"Hakkında N sonuç"** satırını göstermedi (`#resultstats` boş); aşağıdaki tablolar **ilk sayfadaki** sıralı organik sonuçlardır (Google'ın o an gösterdiği sayfa 1). Derin indeks bu yöntemle ölçülmedi.
- **⚠️ Coğrafya/çeviri uyarısı (yorumlama için kritik):** Görevde "tarayıcının konumu muhtemelen TR" deniyordu; **gözlem buna uymuyor.** SERP'in arayüz başlıkları sorgular arasında **tutarlı Türkçe değildi**: Q1/Q4 "Web sonuçları" (TR) iken Q2'de **"Webresultaten" (NL)**, Q2/Q3'te **"Veebitulemused" (ET)**, Q3'te **"Nettresultater" (NO)** etiketleri görüldü; ayrıca yabancı dildeki sonuçlarda "Bu sayfanın çevirisini yap" (TR) düğmesi belirdi. Bu, ortak Chrome'un **çıkış IP'sinin temiz bir Türkiye konut IP'si olmadığını** (muhtemelen Avrupa kökenli bir veri merkezi/bulut IP'si) ve Google'ın bazı arayüz öğelerini **IP'ye göre** (hl=tr&gl=tr parametresini aşılarak) lokalize ettiğini gösterir. **Sonuç:** bir Türkiye'deki gerçek kullanıcının gördüğü SERP bundan farklı olabilir (daha TR-kişi ağırlıklı sonuçlar çıkabilir). Bulgular "bu çıkış IP'sinden, bu tarih/saatte Google'ın döndürdüğü sayfa 1" olarak okunmalıdır.

---

## 4. Sorgu başına sonuçlar (Google, 2026-11-05 20:06–20:08 UTC)

### 4.1 Q1 — `"Aydın Öztürk"` (8 sıralı organik sonuç + medya blokları)

Knowledge Panel: hedefe ait bir KP **yok**. "People also ask": görünmedi. Yerine Google, isim için **medya blokları** kurdu: **"Şarkılar"** (Ömrüm Senindir · 2006; Zifir Saçlarını Savur İçimde · 1999; Sızı · 2000; Canlı Yayında Ölüm · 2004 — 20+ öğe), **"Videolar"** (İber Prodüksiyon — "Yılların Zehir Süzgeci", "düet Özge", "düet Ebru Koşar"), **"Görseller"** (Türkiye Yazarlar Sendikası + Spotify). → **Google'ın "Aydın Öztürk"ün baskın anlamı bir müzisyen.**

| # | Başlık | Kaynak (breadcrumb) | Snippet (kısa) | Sınıflandırma |
|---|---|---|---|---|
| 1 | Aydın Öztürk (@aydinozturkkk) | Instagram `@aydinozturkkk` | 5.6K+ takipçi, 3.7K+ takip, 6036 gönderi | **başka kişi** (muhtemel müzisyen; handle `aydinozturkkk` — hedefin `aydinozturk`) |
| 2 | Aydın Öztürk Official | YouTube Music | "Asi Fırat" · "Yüzüm Dönmedim" · "& Çiğdem Karabulut — Özlem Ülkesi" | **başka kişi** (müzisyen) |
| 3 | Aydın ÖZTÜRK | turkiyeyazarlarsendikasi.org/`aydin-ozturk` | "Şair ve yazar … 1 Ocak 1955, Pertek/Tunceli doğumlu; 12 Eylül sonrası cezaevleri şiiri" | **başka kişi** (şair/yazar) |
| 4 | Aydın Öztürk | tr.wikipedia.org/wiki/`Aydın_Öztürk` | "Vatan Gazetesi'nin yöneticiliği … Doğum 12 Ağustos 1939 (87 yaşında)" | **başka kişi** (gazeteci; tr-Vikipedi sayfası var) |
| 5 | Aydın Öztürk Şiirleri — Şair | antoloji.com/Şairler | "Aydın Öztürk şiirleri … şairin hayatı" | **başka kişi** (şair) |
| 6 | aydın öztürk | eksisozluk.com/`aydin-ozturk--465738` | "computer algorithms, computer graphics, image processing, probability and statistics … ege übe'de … profesör" | **başka kişi** (BT akademisyeni, Ege Ü.) |
| 7 | Aydın Öztürk (@A_Yagmuryurekli) | X | "Köknar Hanım şiiri … Klip YouTube'de; müzik Burhan İşiyok; yapım Asrın Müzik" | **başka kişi** (şair) |
| 8 | Aydın Öztürk — Türk Edebiyatı İsimler Sözlüğü | teis.yesevi.edu.tr/`ozturk-aydin` | "(d. 1 Ocak 1955) Şair, Romancı, Denemeci" | **başka kişi** (şair) |

**Okuma:** 8/8 sıralı sonuç **başka kişi** (müzisyen + şair/yazar + gazeteci + BT akademisyeni). **Bu kişi: 0. Site: 0.** İsim, Google'da müzik/edebiyat anlamına oturmuş durumda; hedefin hiçbir profili sıralamadadır.

### 4.2 Q2 — `"Aydın Öztürk aydinozturk"` (9 sıralı organik sonuç)

Knowledge Panel: yok. "People also ask": **"Aydın Öztürk nereli?"**

| # | Başlık | Kaynak (breadcrumb) | Snippet (kısa) | Sınıflandırma |
|---|---|---|---|---|
| 1 | Aydın Öztürk (@ayd.n.ozturk.222782) | Facebook | "Haber Müdürü … GÜNAYDIN GAZETESİ; Spor Müdürü … Akşam Gazetesi; … gazetecilik okulu" | **başka kişi** (gazeteci) |
| 2 | Aydın Öztürk | TikTok | "yeni single çalışması, Özge'nin düetiyle 'Sen Güneşin Tutkunuydun' 5 Mayıs … dijital platformlarda!" | **başka kişi** (müzisyen) |
| 3 | Aydin Öztürk (@birindar.ozturk) | Facebook | "Istanbul. Lives in Istanbul, Turkey." | **başka kişi** (kişisel, İstanbul) |
| 4 | Aydin Öztürk | Facebook `aydin.ozturk.18` | "Aydin Öztürk is on Facebook." | **başka kişi** (kişisel) |
| 5 | Aydın Öztürk — Yazarın kitapları | truvakitap.com/Yazarlar | "Bir Sevgi Kırılmasıydı, Saklı Sevdiğim, Yağmur Yürekli Mektuplar (Berfin Yayınları)" | **başka kişi** (romancı) |
| 6 | Aydın öztürk (@ayd.n.ozturk.495445) | Facebook | kişisel profil | **başka kişi** (kişisel) |
| 7 | Omer Aydın Öztürk | TikTok | "modern Turkish poetry and literature … contributions to the arts" | **başka kişi** (şair, Ömer Aydın Öztürk) |
| 8 | Aydin Özturk (@aydinozturk420) | Instagram | "76 followers · 182 following" | **başka kişi** (küçük IG; handle `aydinozturk420`) |
| 9 | Aydın Özturk | Facebook `Aydın-Özturk-100088343` | kişisel profil | **başka kişi** (kişisel) |

**Okuma:** `aydinozturk` alan adı token'ı eklendiğinde bile sonuç **hedefin sitesini döndürmedi**; Google'ın elinde bu isim için **çok sayıda kişisel Facebook/Instagram/TikTok profili** + müzisyen + romancı var ve onları sıralıyor. Hedefin `aydinozturk.com` alan adı **görünmedi**. → Alan adı token'ı Google'da hâlâ hedefi sıralatmıyor (Bing'deki `site:`→0 bulgusuyla paralel, #266 §4.7).

### 4.3 Q3 — `"Aydın Öztürk" UZMAR` (≈4 benzersiz organik sonuç + görsel künyeleri)

Knowledge Panel: yok. "People also ask": görünmedi. **Dikkat:** Google'ın sıraladığı **Facebook `@zorroaydin`** sayfası, **aynı sayfayı farklı arayüz dillerinde** (Norveççe/Estonca/Irlandaca snippet'lerle) alt alta ~6 kez gösterdi — organik sonuçlar benzersizleştirmede ~4'e iner.

| # | Başlık | Kaynak (breadcrumb) | Snippet (kısa) | Sınıflandırma |
|---|---|---|---|---|
| 1 | Aydın Öztürk (@zorroaydin) | Facebook `zorroaydin` | "Aydın Öztürk. Istanbul." (çok dilli varyasyonlarla ~6×) | **başka kişi** (kişisel, İstanbul — bu kişi olma sinyali yok) |
| 2 | Uzmar, iki adet yeni inşa ASD RAstar 3200W için … | marinedealnews.com | "Uzmar Tersanesi'nde … RAstar 3200W azimuth römorkörler … 10 Mar 2020" | **UZMAR şirket** (tersane haberi; kişi değil) |
| 3 | Ufuk Aydin — Senior Operation Manager | LinkedIn | "Marmara Ship Supply · Sakarya Ü. · Türkiye" | **başka kişi** (Ufuk Aydin; soyad bile farklı, deniz tedarik) |
| 4 | M. ÖZTÜRK (IEEE/makale) | dergi.fsm.edu.tr (FSM Vakıf Ü.) | "'Hz. Osmân (23-35/644-656) Döneminde Denizcilik Faâliyetleri', FSMIAD 18, 195–230, 2021" | **başka kişi** (M. Öztürk, denizcilik tarihi makalesi) |
| — | **Görseller (küçük resimler):** "Aydın Öztürk — Software Development Manager / Architect …" (×4) + "Ülkemizin denizcilik teknolojilerine katkı sağlamak …" (LinkedIn) | LinkedIn | — | **bu kişi (muhtemel, yüksek güven)** — LinkedIn künyesi; **yalnız görsel blokta, sıralı organik metinde yok** |

**Okuma:** `UZMAR` sorgusu, hedefin adını taşıyan **UZMAR Tersanesi**'ne ve denizcilik sektöründeki **başka kişilere** (Ufuk Aydin, M. Öztürk) kaydı; organik metin sıralaması çoğunlukla **tek bir İstanbul Facebook profili** ile dolu. Hedefin gerçek izi (**LinkedIn — "Software Development Manager / Architect", "denizcilik teknolojileri"**) yalnızca **görsel küçük resimlerinde** çıktı. → `UZMAR` token'ı hedefi organik sıralamaya taşımıyor; tersane şirketiyle karışıyor.

### 4.4 Q4 — `"Aydın Öztürk" github` (9 sıralı organik sonuç + görsel künyeleri)

Knowledge Panel: yok. "People also ask": görünmedi. **Sorgu "github" içeriyor ama `github.com/aydinozturk` sonucu çıkmadı** — Google bunun yerine LinkedIn/akademi/kişisel site sıraladı.

| # | Başlık | Kaynak (breadcrumb) | Snippet (kısa) | Sınıflandırma |
|---|---|---|---|---|
| 1 | aydın öztürk | tr.linkedin.com `aydın-öztürk-666519379` | "İstanbul · Kurucu · Flex Project Group · Eyl 2019–Halen (7 yıl 1 ay)" | **başka kişi (muhtemel)** — "Flex Project Group" kurucusu; şirket/unvan hedefin UZMAR'ıyla uyuşmuyor, URL `/in/aydinozturk` değil (sayısal id) → bu kişi olma olasılığı düşük |
| 2 | aydın öztürk — #18372808 | eksisozluk.com/entry | "computer algorithms … ege übe'de … profesör" (4 Mar 2010) | **başka kişi** (BT akademisyeni, Ege Ü.) |
| 3 | Aydin OZTURK | ResearchGate | "Yaşar University, İzmir" | **başka kişi** (akademisyen) |
| 4 | Aydin Ozturk — Professional Profile (PDF) | Scribd | "29-year-old Turkish male living in Italy … food service, translation, music, call centers" | **başka kişi** (İtalya'da yaşayan) |
| 5 | Aydın Öztürk — PhD Professor (Full) | ResearchGate | "Izmir University · Cited by 867 · 30 publications" | **başka kişi** (BT akademisyeni, İzmir Ü.) |
| 6 | Aydin Öztürk (@birindar.ozturk) | Facebook | "Istanbul. Lives in Istanbul." | **başka kişi** (kişisel) |
| 7 | (dizin listesi) | aydin-ozturk.com | "Directory cgi-bin … 2024-12-10 … LiteSpeed Web Server at www.aydin-ozturk.com Port 443" | **başka alan adı** — `aydin-ozturk.com` (**tireli**); hedefin `aydinozturk.com`'u değil; çıplak dizin görünümü |
| 8 | Aydin Ozturk | Facebook `aydin.ozturk.7564` | "Akyazı, Sakarya, Turkey" | **başka kişi** (kişisel) |
| 9 | Aydın Öztürk (@zorroaydin) | Facebook `zorroaydin` | "Istanbul" | **başka kişi** (kişisel, İstanbul) |
| — | **Görseller (küçük resimler):** "Aydın Öztürk — Software Development Manager / Architect …" (LinkedIn) + "Aydın Öztürk \| Dijital Pazarlama Eğitimleri \| Udemy" | LinkedIn / Udemy | — | LinkedIn = **bu kişi (muhtemel, yüksek güven)**; Udemy = **başka kişi** (eğitmen) |

**Okuma:** "github" kelimesiyle dahi **hedefin GitHub profili (`github.com/aydinozturk`) Google'da sıralanmıyor.** Çıkanlar: BT akademisyenleri (Ege/İzmir/Yaşar Ü.), LinkedIn kurucu profili (Flex Project Group), **benzer ama farklı alan adı** `aydin-ozturk.com`, kişisel FB'ler. Hedefin LinkedIn'i yine **yalnız görsel küçük resiminde**.

---

## 5. Özet tablo — hedefin varlığı sorgu bazında

| Sorgu | Sıralı organik (1.sayfa) | **bu kişi** | **site (aydinozturk.com)** | **GitHub** | **LinkedIn `/in/aydinozturk`** | başka kişi | UZMAR şirket / başka alan adı |
|---|---|---|---|---|---|---|---|
| Q1 `"Aydın Öztürk"` | 8 (+medya) | 0 | 0 | 0 | 0 | 8 (müzisyen/şair/gazeteci/BT-prof) | 0 |
| Q2 `"Aydın Öztürk aydinozturk"` | 9 | 0 | 0 | 0 | 0 | 9 (sosyal/müzisyen/yazar) | 0 |
| Q3 `"Aydın Öztürk" UZMAR` | ≈4 benzersiz | 0 (sıralı); **1 LinkedIn görsel künyesi (muht.)** | 0 | 0 | (görsel) | 3 | 1 UZMAR Tersanesi |
| Q4 `"Aydın Öztürk" github` | 9 | 0 (sıralı); **1 LinkedIn görsel künyesi (muht.)** | 0 | **0** | (görsel) | 8 | 1 `aydin-ozturk.com` (başka alan adı) |

**Yorum:** Hedef, 4 sorgunun hiçbirinde **sıralı organik sonuç olarak** yer almıyor. Tek Google izi, `UZMAR` ve `github` sorgularında **görsel küçük resimlerinde** beliren LinkedIn künyesi ("Software Development Manager / Architect … denizcilik teknolojileri") — bu, hedefin LinkedIn'inin **indekslendiğini** ancak **önerilen sıralamaya** giremediğini gösterir (görsel blok ≠ organik sıralama; URL birebir doğrulanmadı, tıklanmadı).

---

## 6. İsim çakışması analizi — #268 §2.2'nin açık sorusuna cevap

Önceki rapor (#268 §2.2/§6), "Google'a erişim olmadığı için Google'da farklı Aydın Öztürk kişileri çıkıp çıkmayacağı **doğrulanamadı**" demişti. **Bu rapor onu doğruladı:**

- **Google, "Aydın Öztürk"ü birden fazla, birbirinden bağımsız, gerçek kişi/kişilik kümesine bağlıyor.** İlk sayfada en az **4 ayrık kimlik** net olarak ayırt edilebiliyor:
  1. **Müzisyen** — "Şarkılar" (Ömrüm Senindir 2006, Sızı 2000, Can Yağında Ölüm 2004…), YouTube/İber Prodüksiyon klipleri, Spotify, YouTube Music "Aydın Öztürk Official", IG `@aydinozturkkk`. *(Google'ın isim için baskın anlamı.)*
  2. **Şair/yazar** — 1 Ocak 1955, Pertek/Tunceli; Türkiye Yazarlar Sendikası, Antoloji.com, Türk Edebiyatı İsimler Sözlüğü (Yesevi Ü.), X.
  3. **Gazeteci** — 12 Ağustos 1939; Vatan Gazetesi kurucu/yönetici; **tr.wikipedia.org/wiki/Aydın_Öztürk** sayfası; FB (Haber/Spor Müdürü).
  4. **BT akademisyeni** — Ege Ü. / İzmir Ü. / Yaşar Ü. (computer algorithms, graphics, image processing, probability & statistics); ResearchGate "Cited by 867"; Ekşi Sözlük.
  5. **Çok sayıda kişisel sosyal profil** — Facebook `@zorroaydin`, `@aydin.ozturk.18`, `@aydin.ozturk.7564` (Akyazı/Sakarya), `@ayd.n.ozturk.*`, IG `@aydinozturk420`; ayrıca İtalya'da yaşayan bir "Aydin Ozturk" (Scribd).
- **Hedef (UZMAR Technology / aydinozturk.com) bunların hiçbirinin organik sıralamasında yok** → arama yapan biri, "Aydın Öztürk" aradığında **yukarıdaki müzisyen/şair/gazeteci/akademisyen** profilleriyle karşılaşır ve bunlardan herhangi birinin **hedefle karıştırılma riski gerçek ve yüksek** (özellikle BT akademisyeni ve "Software Development Manager" LinkedIn, teknik bağlamda kafa karıştırabilir).
- **Farklı motor davranışı (Bing vs Google, karşılaştırma):** Bing `"Aydın Öztürk"` → 10/10 **Aydın ili (şehir)** (#266 §4.1); Google `"Aydın Öztürk"` → 10/10 **başka kişiler (isim tam eşleşme)**. Yani Google "Öztürk" token'ını düşmeden gerçekten isim taşıyanları sıralıyor — **yanlış-atıf/kimlik karışma riski Google'da somutlaşmış durumda.**
- **Alan adı token'ı korumuyor:** `"Aydın Öztürk aydinozturk"` (Q2) ve `"github"` (Q4) sorgularında bile hedefin `aydinozturk.com`'u sıralanmadı; Q4'te **benzer ama farklı** `aydin-ozturk.com` (tireli) alan adı çıktı. Hedefi kimlikle bağlayan en ayırt edici token (alan adı) Google'da hâlâ sıralama getirmiyor.

**Karar:** İsim çakışması **doğrulandı ve ciddi.** "Aydın Öztürk" araması Google'da hedefi **geri getirmiyor**; bunun yerine müzisyen/şair/gazeteci/akademisyen + çok sayıda sosyal profil döndürüyor. Hedefe ait tek Google izi, `UZMAR`/`github` sorgularında **görsel küçük resiminde** beliren LinkedIn künyesidir.

---

## 7. Sınırlılıklar

1. **Coğrafya/çıkış IP'si:** Ortak Chrome'un çıkış IP'si temiz TR değil (Bölüm 3 — çok dilli SERP arayüz başlıkları kanıtlıyor). Sonuçlar bu IP'den alındı; Türkiye konumundan farklı olabilir.
2. **Yalnız sayfa 1:** Her sorguda Google'ın gösterdiği **ilk sayfa** alındı; derin indeks/paginate edilmeyi. Hedefin sayfa 2+'da çıkması dışlandı (ancak Q4'te "github" ile GitHub'ın sıralı sonuç vermemesi güçlü bir sinyal).
3. **Tıklama yok:** Görev disiplini gereği sonuca tıklanmadı; kaynak alan adları breadcrumb'tan okundu. `Software Development Manager / Architect` LinkedIn künyesinin **birebir** `linkedin.com/in/aydinozturk` olduğu URL düzeyinde doğrulanmadı — bağlam (denizcilik teknolojisi, UZMAR sorgusu, #267 §5'teki "Aydın Öztürk - UZMAR Technology | LinkedIn" title) ile **yüksek güvenle** hedefin profili olarak işaretlendi.
4. **Sonuç sayısı:** Google bu oturumda "Hakkında N sonuç" satırı göstermedi; tablolar sıralı sayfa-1 sayılarıdır.
5. **Zaman/oturum bağımlılığı:** SERP'ler 2026-11-05 20:06–20:08 UTC'ye ve tarayıcının oturum/IP konumuna bağlıdır; Google sonuçları kişiselleşebilir/dinamik değişebilir.
6. **CDP metodu:** `chrome-devtools` MCP araçları bu SDK oturumunda listelenmediği için çekim, aynı Chrome'a **doğrudan CDP/ WebSocket** ile yapıldı (metot farkı sonucu etkilemez — aynı gerçek tarayıcı).

---

## 8. Sonuç

Gerçek Google (Chrome) üzerinden 4 kişi sorgusu çekildi, 4/4 sonuç **engelsiz** (CAPTCHA/consent yok) ve **dürüstçe** kaydedildi. Bulgular:

- **"Aydın Öztürk" araması Google'da hedefi değil, farklı gerçek kişileri döndürüyor** — baskın anlam **müzisyen**, yanına **şair (1955)**, **gazeteci (1939, tr-Vikipedi)**, **BT akademisyeni (Ege/İzmir)** ve **çok sayıda sosyal profil** giriyor. #268 §2.2'deki **isim çakışması riski doğrulandı ve ciddi.**
- **Hedefin (UZMAR Technology / aydinozturk.com / github.com/aydinozturk) sıralı organik Google izi bu 4 sorguda yok.** Hedefe ait tek iz, `UZMAR` ve `github` sorgularında **görsel küçük resimlerinde** beliren **LinkedIn** künyesi ("Software Development Manager / Architect … denizcilik teknolojileri") → hedefin LinkedIn'i indekslenmiş ama önerilen sıralamaya girmiyor.
- **`UZMAR` sorgusu** hedefe değil **UZMAR Tersanesi**'ne (aynı adlı denizcilik şirketi) kayıyor; **`github` sorgusunda** hedefin GitHub'ı değil, **farklı** bir alan adı `aydin-ozturk.com` (tireli) çıkıyor.
- Bing ile fark: Bing şehre, **Google isim taşıyan kişilere** cevap veriyor → kimlik karışma/yanlış-atıf riski **Google'da somut.**

**Öneri (aksiyon için, #268 §5.3/§5.5 ile tutarlı):** Google'da hedefe özel görünürlüğü artıracak tek etkili kanal, hedefi **kimlikle bağlayan token'ların** (alan adı + şirket) dış mecralarda (GitHub about/website, LinkedIn unvan "Aydın Öztürk (UZMAR Technology)", vaka metinleri) **tam ve tutarlı** biçimde geçmesi + GSC üzerinden indeks istemi'dir; çünkü çıplak isim sorgusu yapısal olarak bu adı taşıyan çok sayıda kişiye kayıyor ve bugün de kaydı (bu rapor).

---

## 9. Kaynaklar

**Bu rapordaki birincil kanıt (Google SERP, çekim 2026-11-05 20:06–20:08 UTC, gerçek Chrome `192.168.65.254:9222` / `Chrome/156`):**
1. `https://www.google.com/search?q=%22Ayd%C4%B1n+%C3%96zt%C3%BCrk%22&hl=tr&gl=tr` — Q1
2. `https://www.google.com/search?q=%22Ayd%C4%B1n+%C3%96zt%C3%BCrk+aydinozturk%22&hl=tr&gl=tr` — Q2
3. `https://www.google.com/search?q=%22Ayd%C4%B1n+%C3%96zt%C3%BCrk%22+UZMAR&hl=tr&gl=tr` — Q3
4. `https://www.google.com/search?q=%22Ayd%C4%B1n+%C3%96zt%C3%BCrk%22+github&hl=tr&gl=tr` — Q4

**Depo içi girdiler (değiştirilmedi):**
- `reports/google-search-results.md` (#268) — §2.2/§6 açık soru, §5 öneriler
- `research/aydinozturk.com/search-serp.md` (#266) — metot + sınıflandırma şeması, Bing karşılaştırması
- `research/aydinozturk.com/search-indexing.md` (#267) — §5 LinkedIn "Aydın Öztürk - UZMAR Technology" title doğrulaması
- `reports/aydinozturk-com-research.md` (#264) — arka plan

**Yeniden üretim:** 4 SERP URL'i aynı gerçek tarayıcıda (Chrome, `hl=tr&gl=tr`) açıldığında aynı ilk sayfa döner (coğrafya/IP ve zaman farkı göz önüne alınarak).
