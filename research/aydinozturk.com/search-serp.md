# arama motoru sonuçları (best-effort SERP) — Aydın Öztürk / aydinozturk.com

> Görev: [#266] (Plan #265 — "Bu kişi Google'da arama sonuçlarıyla ilgili bir şey var mı?") · Çalışan: agent-3
> Erişim tarihi: **2026-11-05, ~16:30 UTC** · Tüm SERP ham HTML'leri bu dakikalarda alındı.
> Kapsam: Kişi (Aydın Öztürk) ve alan adı (aydinozturk.com) için arama motorlarının organik sonuçları;
> isim çakışması analizi; "Google'da ne çıkar" sorusunun bu ortamda verilebilecek en iyi çaba cevabı.
> Bağlam için: `research/aydinozturk.com/{site-technical,site-content-seo,domain-history}.md`.

---

## 1. Özet bulgular

- **Bing TR organik sonuçlarında (6 zorunlu + 1 ek sorgu, 69 sonuç) kişiye veya `aydinozturk.com` alan adına ait TEK BİR sonuç bile çıkmadı.** Bing'in bu sorgularla erişebildiği kadarıyla alan adı **Bing indeksinde görünmüyor**.
- `site:aydinozturk.com` operatörlü sorgu bile alan adından 0 sonuç döndürdü; Bing, "sonuç yok" demek yerine alakasız "popüler içerik" filler'i (WhatsApp forumları) listelemiş (Bölüm 4.7). Dolaylı ama güçlü "indekste yok/çok az" sinyalidir.
- `"Aydın Öztürk"` sorgusunda Bing, **"Öztürk" token'ını fiilen düşerek "Aydın" şehrine** göre cevap veriyor: 10/10 sonuç Aydın ili/belediye/haber içeriği (Bölüm 4.1). Bu isim için Bing'de hem kişiye özel sonuç hem de *başka* Aydın Öztürk kişileri görünmüyor (Bölüm 6).
- Kişinin sitesinin kendi referans verdiği **LinkedIn profili (`linkedin.com/in/aydinozturk`, `domain-history.md`) ve GitHub hesabı (`github.com/aydinozturk`) hiçbir Bing sorgusunda organik sonuç olarak görünmüyor** — özellikle `"aydinozturk linkedin"` sorgusunda (Bölüm 4.5).
- **YORUM (dikkat):** Bu "Google'da ne çıkar"ın cevabı **değildir**; bu ortamda Google'a erişilemedi (Bölüm 3). Google'ın indeksi bu nadir sorgularda farklı davranabilir ve kişi/profil sonuçları çıkabilir. Doğrulanabilir tek iddia: **Bing (TR, masaüstü) bugün bu sonuçları gösteriyor.**

---

## 2. Metot

- **Motor:** Bing HTML sürümü (`https://www.bing.com/search?q=<sorgu>&setlang=tr&cc=tr`), `curl` + masaüstü kullanıcı agentı `Mozilla/5.0 (Windows NT 10.0; Win64; x64)` ile çekildi (her sorgu için ham HTML ~120 KB; gerçek SERP olduğu sayfa başlığından doğrulandı).
- **Çözümleme:** Organik sonuçlar `<li class="b_algo">` blokları; başlık `h2>a`, URL `href` içindeki base64 `u=a1…` redirect hedefi (padding tamamlanarak b64decode), `cite` ve snippet `<p>` alındı. Sorgu yansıması (arama kutusu, sayfalama, filtre menüleri) sonuç olarak sayılmadı. Doğrulama: sayfada geçen her `aydinozturk*` metni tek tek incelendi; tamamı sorgu yansımasıydı, hiçbir organik sonuçta geçmiyordu.
- **Pipeline kontrolü:** Ortak terim `"ankara"` sorgusu aynı metotla çekildi → doğru ve alakalı sonuçlar (tr/en Vikipedi, `ankara.gov.tr`, gezi rehberleri, Tripadvisor). Nadir sorgulardaki alakasız sonuçlar Bing'in kendi davranışıdır (Bölüm 5).
- Sorgular (görev tanımı + 1 ek): `"Aydın Öztürk"`, `"aydinozturk"`, `"aydinozturk.com"`, `"Aydın Öztürk aydinozturk"`, `"aydinozturk linkedin"`, `"aydinozturk twitter"`, ek: `"site:aydinozturk.com"`. `"aydinozturk.com"` için 2. sayfa da (`first=10`) çekildi.

---

## 3. Motor erişilebilirliği (agent-2 tarafından 2026-11-05 doğrulandı — yeniden test edilmedi)

| Motor / kanal | Durum | Neden |
|---|---|---|
| Google (doğrudan) | ❌ alınamıyor | JS challenge (bot kontrolü); sade HTTP istemcisiyle sonuç alınamıyor |
| DuckDuckGo (html/lite) | ❌ | "anomaly" (güvenlik) ekranı |
| SearXNG public instance'ları | ❌ | 429 / browser-check |
| Mojeek | ⚠️ | erişilebilir ama bu sorgulara boş döndürüyor |
| WebSearch (MCP aracı) | ❌ | arka uç API 400 — araç bu ortamda kırık |
| **Bing HTML (curl + masaüstü UA)** | ✅ **çalışıyor** | tek kullanılabilir kanal; nadir sorgularda filler davranışı var (Bölüm 5) |

Sonuç: rapor, **Bing TR** üzerinden "en iyi çaba" düzeyinde hazırlanmıştır.

---

## 4. Sorgu başına sonuçlar (Bing TR, 2026-11-05)

İlinti hükmü değerleri: **kişi** = Aydın Öztürk (bu kişi) hakkında · **site** = aydinozturk.com ile ilgili · **başka kişi** = farklı bir kişi hakkında · **şehir** = Aydın ili içeriği (token eşleşmesi, filler değil) · **filler** = sorguyla alakasız popüler içerik. Snippet'lar kısaltılmıştır.

### 4.1 `"Aydın Öztürk"` — 10 sonuç

| # | Başlık | URL | Snippet (kısa) | İlinti |
|---|---|---|---|---|
| 1 | T.C. Aydın Büyükşehir Belediyesi | https://aydin.bel.tr/ | "…Belediye Başkanı Özlem Çerçioğlu'nun öncülüğünde kent genelinde…" | şehir |
| 2 | Aydın — Vikipedi | https://tr.wikipedia.org/wiki/Aydın | "Aydın, Türkiye'nin Aydın ilinin merkezi olan şehirdir…" | şehir |
| 3 | Aydın'da Gezilecek Yerler (En Güzel 27 Yer) | https://www.enuygun.com/bilgi/aydin-da-gezilecek-yerler/ | "30 Kas 2023 · Efeler Diyarı olarak bilinen Aydın'da…" | şehir |
| 4 | Aydın (il) — Vikipedi | https://tr.wikipedia.org/wiki/Aydın_(il) | "…Merkezi Efeler olan il, 2024 itibarıyla 1.161.702 kişilik nüfusuyla…" | şehir |
| 5 | T.C. Aydın Büyükşehir Belediyesi (haber) | https://aydin.bel.tr/Content/ | "Aydın BŞB Çocuk Kültür Merkezleri 23 Nisan'ı Coşkuyla Kutladı…" | şehir |
| 6 | Aydın Denge Haber | https://www.aydindenge.com.tr/ | "Aydın Denge sitesi güncel olarak Aydın Haber içeriğini sunar…" | şehir |
| 7 | Aydın Gezilecek Yerler (gezi rehberi) | https://yerler.com.tr/aydin-gezilecek-yerler/ | "27 Nis 2026 · Aydın, Türkiye'nin Ege Bölgesi'nde yer alır…" | şehir |
| 8 | Aydın Valiliği | http://aydin.gov.tr/ | "1976 tarihinde İzmir'de doğan Vali VAROL… 30.04.2026 … atandı." | şehir |
| 9 | Aydın Ses Gazetesi | https://www.sesgazetesi.com.tr/ | "2024 Yerel Seçim sonuçları son dakika burada!" | şehir |
| 10 | Aydinpost — Aydın Haber | https://www.aydinpost.com/ | "Aydın ve çevresinden en çarpıcı haberler, köşe yazıları, canlı yayınlar…" | şehir |

**Okuma:** 10/10 sonuç Aydın şehrine ait. "Öztürk" adını taşıyan hiçbir kişi sonucu yok; Bing, sorguyu "Aydın" token'ına göre cevaplamış.

### 4.2 `"aydinozturk"` — 10 sonuç

| # | Başlık | URL | Snippet (kısa) | İlinti |
|---|---|---|---|---|
| 1 | Bursa Uludağ Üniversitesi | https://uludag.edu.tr/ | "BUÜ'de 'Ruha Şifa Hüsn-ü Hat Sergisi' kapılarını açtı…" | filler |
| 2 | Uludağ Üniversitesi (UNİSİS) | https://unisis.uludag.edu.tr/ | "Mobil Uygulama (Android) linkimiz (Öğrenci için) TIKLAYINIZ…" | filler |
| 3 | Bursa Uludağ University (bilgi paketi) | https://bilgipaketi.uludag.edu.tr/Programlar/Detay/355?AyID=26 | "…Matematik Bilimi alanında 240 ECTS kredilik birinci aşama…" | filler |
| 4 | İnegöl İşletme Fakültesi \| BUÜ | https://uludag.edu.tr/inif | "2025-2026 Yaz Öğretimi Sonrası 15. Madde Azami Süre…" | filler |
| 5 | Bilgi İşlem Daire Başkanlığı \| BUÜ | https://uludag.edu.tr/bilgiislem | "Eduroam Bağlantı Sorunu Yaşayan Kullanıcıların Dikkatine…" | filler |
| 6 | Logolar \| BUÜ | https://uludag.edu.tr/logolar-6072 | "Üniversitemizin Kurucu Rektörü, merhum Prof. Dr. Ömer Fethi Tezok…" | filler |
| 7 | Elektrik-Elektronik Mühendisliği \| BUÜ | https://uludag.edu.tr/eem | "Ulusal Staj Programı 2027 Yılı Başvuru Dönemi…" | filler |
| 8 | Kampüs Kart | https://kartodeme.uludag.edu.tr/User/Login | "Kampüs Kart Sistemi, CampusCard Application…" | filler |
| 9 | Biyoloji \| BUÜ | https://uludag.edu.tr/biyoloji | "Beden Eğitimi Bölüm Başkanlığı'ndan Alınan Alan Dışı Seçmeli…" | filler |
| 10 | Fen-Edebiyat Fakültesi \| BUÜ | https://uludag.edu.tr/fenedebiyat | "2026-2027 Güz Yarıyılı Öğretmenlik Uygulaması Hakkında…" | filler |

**Okuma:** 10/10 sonuç, sorguyla hiçbir ilgisi olmayan "Uludağ Üniversitesi" popüler içeriği. `aydinozturk.com` veya kişiyle alakalı sonuç yok.

### 4.3 `"aydinozturk.com"` — 1. sayfa 9 sonuç

| # | Başlık | URL | Snippet (kısa) | İlinti |
|---|---|---|---|---|
| 1 | Akademik Personel — Memurlar.Net | https://forum.memurlar.net/kategori/kamu-personeli/akademik-personel/ | "Kamu Personeli \ Akademik Personel Editörler: MEB, Emniyet…" | filler |
| 2 | Türk Silahlı Kuvvetleri — Memurlar.Net | https://forum.memurlar.net/kategori/kamu-personeli/turk-silahli-kuvvetleri/ | "MSB, İçişleri Bakanlığı, TSK… Subay, Astsubay, Jandarma…" | filler |
| 3 | DHMİ'ye dilekçe — Memurlar.Net | https://forum.memurlar.net/konu/2598907/dhmi-ye-dilekce.html | "22 Eki 2026 · DHMİ'ye dilekçe, Olumsuz ise 1-2 ayda cevap verir…" | filler |
| 4 | Personel şubeye dilekçe — Memurlar.Net | https://forum.memurlar.net/konu/2598778/personel-subeye-dilekce.html | "15 Eki 2026 · Dilekçe kanunen gönderilmek zorunda…" | filler |
| 5 | Deprem — Memurlar.Net | https://forum.memurlar.net/konu/cevap/710598e5-32b8-f111-b183-a0369f7d1d8e/ | "24 Eyl 2026 · Deprem, Şanlıurfa merkezli deprem dilekçe…" | filler |
| 6 | 7376 Nitelik kodu nedir? — Memurlar.Net | https://forum.memurlar.net/konu/2591289/7376-nitelik-kodu-nedir.html | "21 Ara 2025 · 7376 Nitelik kodu nedir?" | filler |
| 7 | Memurlar.Net — Forum | https://forum.memurlar.net/default.aspx | "Memurlar.Net üyelerinin buluştuğu forum platformudur…" | filler |
| 8 | En yeni konular — Memurlar.Net | https://forum.memurlar.net/konu/en-yeniler/ | "21 saatin üstünde ders istemiyorum diye idareye dilekçe verdim…" | filler |
| 9 | Tayin ve becayiş hakkında — Memurlar.Net | https://forum.memurlar.net/konu/1417341/ | "25 Kas 2011 · Dilekçe vermeden önce amirinle özel konuş…" | filler |

#### `"aydinozturk.com"` — 2. sayfa (10 sonuç)

| # | Başlık | URL | Snippet (kısa) | İlinti |
|---|---|---|---|---|
| 1 | Çırpınırdı Karadeniz Fon Müziği Mp3 İndir | https://www.mp3indirdur.pro/cirpinirdi-karadeniz-fon-muzigi/ | mp3 indir içeriği | filler |
| 2 | ÇIRPINIRDI KARADENİZ FON MÜZİĞİ TELİFLİ — YouTube | https://www.youtube.com/watch?v=wnhV_OKV6so | video | filler |
| 3 | TurkSound — Çırpınırdı Karadeniz Mp3 İndir | https://mp3semti.com/turksound-cirpinirdi-karadeniz.html | mp3 indir içeriği | filler |
| 4 | Çırpınırdı Karadeniz — Enstrümantal Fon Müziği | https://www.youtube.com/watch?v=1ZIMyRM5RyY | video | filler |
| 5 | 01. Çırpınırdı Karadeniz : Free Download | https://archive.org/details/01.CrprnrdKaradeniz | arşiv içeriği | filler |
| 6 | Mt Çırpınırdı Karadeniz 2 (MP3 128K) | https://archive.org/details/MtrpnrdKaradeniz2MP3128K | arşiv içeriği | filler |
| 7 | TurkSound Çırpınırdı Karadeniz mp3 indir dur | https://meloaz.com/tr/mp3/turksound/cirpinirdi-karadeniz/ | mp3 indir içeriği | filler |
| 8 | Azerin — Çırpınırdın Karadeniz Mp3 İndir | https://mp3semti.com/azerin-cirpinirdin-karadeniz.html | mp3 indir içeriği | filler |
| 9 | Çırpınırdın Karadeniz MP3 Download & Lyrics | https://www.boomplay.com/songs/162913696 | müzik içeriği | filler |
| 10 | ÇIRPINIRDI KARADENİZ TELİFLİ — YouTube Music | https://music.youtube.com/watch?v=wnhV_OKV6so&list=PLSAb6ffoYboHUcycdYuws2fPop9TBO3hk | video | filler |

**Okuma:** Sayfa 1 ve 2'de **farklı** filler setleri (s1 forum, s2 müzik) dönüyor — filler'in sorgu-sabit olmadığını, sayfadan sayfaya değişen alakasız "popüler içerik" olduğunu gösteriyor. Sayfalama 4 sayfa sunuyor; alan adına ait sonuç yok.

### 4.4 `"Aydın Öztürk aydinozturk"` — 10 sonuç

Bölüm 4.1 ile **birebir aynı** 10 sonuç (aynı başlıklar/URL'ler; tamamı şehir içeriği). "aydinozturk" eklenince bile Bing şehre göre cevap veriyor. İlinti: 10/10 **şehir** (token eşleşmesi/filler karışımı).

### 4.5 `"aydinozturk linkedin"` — 9 sonuç

| # | Başlık | URL | Snippet (kısa) | İlinti |
|---|---|---|---|---|
| 1 | おすすめと検索結果を管理する — YouTube Help (ja) | https://support.google.com/youtube/answer/6342839?hl=ja | YouTube öneri/söz geçmişi yönetimi | filler |
| 2 | 如何在中国大陆用「合法」的方式观看… (zh) | https://www.zhihu.com/question/1903231775980913051 | YouTube erişim sorusu (Çince) | filler |
| 3 | 知乎 (zh) | https://www.zhihu.com/tardis/bd/art/698690739 | zhihu içeriği | filler |
| 4 | YouTube-Community — Google Help (de) | https://support.google.com/youtube/community?hl=de | topluluk forumu | filler |
| 5 | YouTube Trợ giúp (vi) | https://support.google.com/youtube/?hl=vi | yardım merkezi | filler |
| 6 | Livestreams bekijken — YouTube Help (nl) | https://support.google.com/youtube/answer/9879686?hl=nl | canlı yayın yardım | filler |
| 7 | Communauté YouTube (fr) | https://support.google.com/youtube/community?hl=fr | topluluk forumu | filler |
| 8 | Log in met een YouTube-gebruikersnaam (nl) | https://support.google.com/youtube/answer/165556?hl=nl | giriş yardımı | filler |
| 9 | Manage your home area — YouTube TV (en) | https://support.google.com/youtubetv/answer/7129768?hl=en | YouTube TV konum | filler |

**Okuma:** 9/9 alakasız YouTube yardım içeriği (farklı dillerde). **Önemli:** Kişinin sitesinin referans verdiği `linkedin.com/in/aydinozturk` profili bu sorguda görünmüyor → Bing'in indeksi bu profili içermiyor (en azından bu sorguyla erişilebilir değil).

### 4.6 `"aydinozturk twitter"` — 10 sonuç

| # | Başlık | URL | Snippet (kısa) | İlinti |
|---|---|---|---|---|
| 1 | Windows'ta uygulamaları ve programları kaldırma — Microsoft | https://support.microsoft.com/tr-tr/windows/windows-ta-uygulamalar%C4%B1-ve-programlar%C4%B1-kald%C4%B1rma-4b55f974-2cc6-2d2b-d092-5905080eaf98 | "Uygulamaları ve programları kaldırmanın farklı yolları…" | filler |
| 2 | Windows'ta Program Ekle veya Kaldır Nerede? — 101-help | https://tr.101-help.com/program-ekleme-veya-kaldirma-kayboldu-mu-nerede-bulunur-981b75e58a/ | "Windows'un modern sürümlerinde…" | filler |
| 3 | Windows 11'de ekle kaldır nerede? — Yandex YaCevap | https://yandex.com.tr/yacevap/c/teknoloji/q/windows-11-de-ekle-kaldir-nerede-615988504 | "Mevcut yazılımları kaldırma…" | filler |
| 4 | Windows'ta Program Ekle veya Kaldır Rehberi — Yandex YaÖzet | https://yandex.com.tr/yaozet/how_to/windows-ta-program-ekle-veya-kaldir-kullanim-rehberi-video-id1-az4R5ryQ | video özet | filler |
| 5 | Program Ekle-Kaldır Nasıl kullanılır? — YouTube | https://www.youtube.com/watch?v=nGWcTOGM9XY | "21 Tem 2021 · …videoda anlattım…" | filler |
| 6 | Windows 11'de bir program nasıl kaldırılır | https://tr.windowsnoticias.com/Windows-11-program%C4%B1n%C4%B1-kaldir/ | "…kaynaklarınızı boşaltmak için…" | filler |
| 7 | Denetim masasındaki program ekle veya kaldır — bilgiyakala | https://bilgiyakala.com.tr/gundem/denetim-masasindaki-program-ekle-veya-kaldir-secenegi-nerede-bulunur | "26 Nis 2026 · 'Program Ekle veya Kaldır'…" | filler |
| 8 | Windows'ta uygulamaları ve programları onarma — Microsoft | https://support.microsoft.com/tr-tr/windows/apps/repair-apps-and-programs-in-windows | "Windows 10/11'de uygulama onarma…" | filler |
| 9 | Program Ekle Kaldırda görünmeyen programı kaldırma — MS Answers | https://learn.microsoft.com/tr-tr/answers/questions/3308806/program-ekle-kald-rda-g-r-nmeyen-program-kald-rma | "19 May 2020 · Office kalıntılarını silmek için…" | filler |
| 10 | Uygulamaları, Programları ve Güncelleştirmeleri Kaldırma — Dell | https://www.dell.com/support/kbdoc/tr-tr/000137586/windows-11-ve-windows-10-da-uygulamalar%C4%B1-programlar%C4%B1-ve-g%C3%BCncelle%C5%9Ftirmeleri-kald%C4%B1rma | "…kaldırma yolları…" | filler |

**Okuma:** 10/10 alakasız Windows "program ekle/kaldır" yardım içeriği. Kişisel twitter/x profili sonucu yok.

### 4.7 (EK) `"site:aydinozturk.com"` — 10 sonuç

| # | Başlık | URL | Snippet (kısa) | İlinti |
|---|---|---|---|---|
| 1 | [found sos] cant login whatsapp browser — Lowyat.NET | https://forum.lowyat.net/topic/5556445 | WhatsApp giriş sorunu | filler |
| 2 | Is Whatsapp web down? — Lowyat.NET | https://forum.lowyat.net/topic/5538738 | WhatsApp durumu | filler |
| 3 | Microsoft Community (MS Office forum) | https://answers.microsoft.com/en-us/msoffice/forum/all/how-do-i-get-answers-for-issues-related-to/9a31274a-bd59-45db-ab37-cf6d6de09136 | forum | filler |
| 4 | Microsoft Community (Windows boot forum) | https://answers.microsoft.com/en-us/windows/forum/all/windows-81-fails-to-boot-ntldr-missing-press-cntl/b51d0328-7087-4b47-a60c-cb9b2527a9d0 | forum | filler |
| 5 | Whatsapp Desktop dah jadi fb app — Lowyat.NET | https://forum.lowyat.net/topic/5565190 | WhatsApp konusu | filler |
| 6 | Whatsapps hacked — Lowyat.NET | https://forum.lowyat.net/topic/5519898 | WhatsApp konusu | filler |
| 7 | those use ipon watsapp web browser — Lowyat.NET | https://forum.lowyat.net/topic/5556449 | WhatsApp konusu | filler |
| 8 | Build Apps & Website services — Lowyat.NET | https://forum.lowyat.net/topic/5580378 | web/tablo konusu | filler |
| 9 | U people use WhatsApp or iMessage — Lowyat.NET | https://forum.lowyat.net/topic/5547101 | WhatsApp konusu | filler |
| 10 | Back up all whatsapp chat history — Lowyat.NET | https://forum.lowyat.net/topic/5543382 | WhatsApp konusu | filler |

**Okuma:** Alan adını doğrudan hedefleyen `site:` sorgusu bile **alan adından 0 sayfa** döndürdü; Bing "sonuç bulamadı" mesajı yerine alakasız filler listelemiş. `aydinozturk.com`'un Bing indeksinde (bu tarihte, bu coğrafya/ayarla) görünür bir varlığının olmadığının en net göstergesidir.

### Kontrol: `"ankara"` — aynı metot

1. Ankara — Vikipedi (tr) · 2. Ankara — Wikipedia (en) · 3. T.C. Ankara Valiliği (`https://www.ankara.gov.tr/`) · 4. Ankara Gezilecek Yerler 155+ (`https://yerler.com.tr/ankara-gezilecek-yerler/`) · 5. Ankara'ya EN İYİ 10 yer (Tripadvisor). → Tamamı alakalı; pipeline doğru çalışıyor.

---

## 5. Bing filler davranışı ve filtreleme

- Nadir/kendine özgü token'lar için (ör. `aydinozturk`, `aydinozturk.com`) Bing'in Türkçe indeksi eşleşme bulamayınca **"sonuç yok" demiyor, genel popüler içerik dolduruyor**. Gözlenen filler setleri: Uludağ Üniversitesi, memurlar.net forumu, "Çırpınırdı Karadeniz" mp3 sayfaları, YouTube yardım sayfaları, Windows ekle/kaldır yardım sayfaları, Lowyat WhatsApp forumları.
- Filler seti **sorgu-sabit değil**: aynı sorgunun 2. sayfası farklı bir filler seti döndürüyor (Bölüm 4.3).
- Filtreleme kuralı (bu raporda uygulanan): bir sonucun başlığında, URL'inde ve snippet'inde sorgu token'ı (`aydinozturk`, `Öztürk`, alan adı) geçmiyorsa **filler/şehir** olarak sınıflandırıldı. Sayfalarda `aydinozturk` metninin geçtiği yerlerin (örn. s1: 19-24×) tümü **sorgu yansımasıydı** (sayfa başlığı/meta og/arama kutusu/sayfalama/filtre menüleri) — hiçbir organik sonuçta geçmiyordu.
- `"Aydın Öztürk"` sorgusunun şehir sonuçları filler'den farklı bir Bing davranışıdır: token eşleştirmesi (Aydın=şehir) ama kişi bağlamı yok; "şehir" olarak işaretlendi.

---

## 6. İsim çakışması analizi ("Aydın Öztürk")

- **Bing'de kişi hakkında sonuç sayısı: 0** — dolayısıyla *farklı* Aydın Öztürk'lere ait sonuç da görünmüyor (0/10). Çakışma analizi Bing üzerinden yapılamadı; bu bir "çakışma yok" kanıtı **değil**, "Bing bu sorguya kişi içeriği döndürmedi" tespitidir.
- Gerekçe: `"Aydın Öztürk"` ve `"Aydın Öztürk aydinozturk"` sorgularının ikisine de yalnızca "Aydın" şehrine göre cevap verdi (Bölüm 4.1, 4.4). "Aydın" hem ad hem il adı olduğu için motor şehir içeriğini (belediye, Vikipedi, haber, valilik) sıralamış; "Öztürk" soyadı eşleştirilmemiş.
- **Risk notu:** "Aydın Öztürk" çok yaygın bir Türk adı-soyadıdır. Google'a bu ortamda erişilemediği için (Bölüm 3), Google'da farklı Aydın Öztürk kişiler (LinkedIn profesyonelleri, haberlerde geçen isimler, akademisyenler vb.) ilk sayfalarda çıkabilir ve bu kişinin sonuçlarıyla karışabilir. Bu sorunun cevabı yalnızca Google erişimi olan bir ortamda (tarayıcı) doğrulanabilir.

---

## 7. Kişiye/alan adına gerçekten ait sonuç var mı? — **YOK**

**Karar: YOK** (Bing TR, 2026-11-05, tüm sorgulanabilir kanallar).

Kanıt:
1. 7 sorgu × 1 sayfa (+ 1 sorgu × 2. sayfa) = **69 organik sonuç; bunların 0'ı** kişiyle veya alan adıyla ilgili (en iyi durum: 10/10 şehir içeriği; en kötü: 10/10 alakasız filler).
2. `site:aydinozturk.com` → alan adından **0 sayfa** (Bölüm 4.7).
3. Sayfalarda `aydinozturk` metni yalnızca sorgu yansımasında geçti; hiçbir sonuç URL'si `aydinozturk.com` değil.
4. Kişinin bilinen profilleri (GitHub `github.com/aydinozturk`, LinkedIn `linkedin.com/in/aydinozturk` — `domain-history.md`) bu sorgularda görünmedi.

**Sınırlı nitelik:** Bu karar Bing'e ve 2026-11-05 tarihine aittir; Google/DDG sonuçları bu ortamda alınamadığından (Bölüm 3) "hiçbir motor çıkmıyor" denemez.

---

## 8. Sınırlılıklar

- Google'a (soru doğrudan "Google'da ne çıkar" olduğundan asıl istenen motor) bu ortamdan erişim yok: JS challenge. DDG/SearXNG/Mojeek/WebSearch de kullanılamadı (Bölüm 3). Cevap tek motor (Bing) üzerinden, "en iyi çaba" düzeyindedir.
- Bing filler davranışı, "Bing'de yok" tespitini güçlendirir ama "Google'da yok" için kanıt teşkil etmez.
- Sonuç listeleri çekim anına (2026-11-05 ~16:30 UTC) ve coğrafya/ayar bağlamına (`setlang=tr&cc=tr`) bağlıdır; sayfa 1 dışında derin indeks yokluğu tam garanti vermez (ancak `site:` sorgusu derin aramayla aynı şeyi söyler).
- Ham SERP HTML'leri bu rapora eklenmedi (repo hijyeni); yeniden üretim: Bölüm 2'deki URL + curl + UA parametreleri birebir aynı sonucu verir.

---

## 9. Kaynaklar (erişim: 2026-11-05)

1. Bing SERP `"Aydın Öztürk"`: https://www.bing.com/search?q=Aydın%20Öztürk&setlang=tr&cc=tr
2. Bing SERP `"aydinozturk"`: https://www.bing.com/search?q=aydinozturk&setlang=tr&cc=tr
3. Bing SERP `"aydinozturk.com"` (s1 ve s2 `first=10`): https://www.bing.com/search?q=aydinozturk.com&setlang=tr&cc=tr
4. Bing SERP `"Aydın Öztürk aydinozturk"`: https://www.bing.com/search?q=Aydın%20Öztürk%20aydinozturk&setlang=tr&cc=tr
5. Bing SERP `"aydinozturk linkedin"`: https://www.bing.com/search?q=aydinozturk%20linkedin&setlang=tr&cc=tr
6. Bing SERP `"aydinozturk twitter"`: https://www.bing.com/search?q=aydinozturk%20twitter&setlang=tr&cc=tr
7. Bing SERP `"site:aydinozturk.com"`: https://www.bing.com/search?q=site%3Aaydinozturk.com&setlang=tr&cc=tr
8. Bing SERP kontrol `"ankara"`: https://www.bing.com/search?q=ankara&setlang=tr&cc=tr
9. Motor erişilebilirliği doğrulaması: agent-2, 2026-11-05 (görev #266 tanımı / oda notları)
10. Kişinin bilinen profilleri (GitHub/LinkedIn) için: `research/aydinozturk.com/domain-history.md` (görev #263)
