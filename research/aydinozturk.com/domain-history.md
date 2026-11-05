# alan adı geçmişi ve çevrimiçi varlık — aydinozturk.com

> Görev: [#263] (Plan #260 — aydinozturk.com kapsamlı araştırması) · Çalışan: agent-5
> Erişim tarihi: **2026-11-05** · Tüm kayıtlar bu tarihte alındı; kaynak URL'leri Bölüm 8'de.
> Kapsam: WHOIS/RDAP, DNS, Wayback Machine arşivi, çevrimiçi profiller (GitHub, LinkedIn, site), trafik tahmini.

---

## 1. Özet bulgular

- Alan adı **bugünkü işletiminde bir kişisel marka / portföy sitesi** olarak kullanılıyor: başlık *"Aydın Öztürk — Systems Architect for Shipyards & Fleets"* (EN/TR, gemi inşa + sanayi yazılımı alanı). [kaynak 3]
- **Kayıt:** Verisign RDAP'a göre alan adı şu an **NameCheap, Inc.** (IANA #1068) üzerinden yönetiliyor. RDAP'ta görünen "registration" olayı **2026-02-13**, expiry **2027-02-13**. [kaynak 1]
- **Önemli:** Wayback Machine'de **2005**'e (robots.txt) ve kök sayfada **2010**'a kadar arşiv görüntüsü var — yani alan adı, bugünkü 2026 kaydından **15+ yıl önce aktif** olmuştur. .com RDAP'ı yalnızca *mevcut* registrar kaydını gösterir; 2026-02-13 tarihi ilk kayıt değil, NameCheap'a yenileme/transfer kayıttır. [kaynak 1, 5]
- **Tarihçe sinyali:** 2010'daki bir görüntüde kök alan adı farklı bir kişiye ait içerik taşıyordu (başlık *"Cuneyt SARIKAYA"*). Bu, alan adının geçmişte başka sahipler/içerikler barındırdığına işaret eder. [kaynak 5]
- **Kimlik eşleşmesi (güçlü):** GitHub kullanıcısı `aydinozturk` — ad *"Aydın Öztürk"*, konum **Kocaeli, Turkey**, firma **Uzmar Technologies**, profil "blog" alanı doğrudan **aydinozturk.com**. Site, bu profili LinkedIn `linkedin.com/in/aydinozturk` ile de ilişkilendiriyor. [kaynak 3, 6]
- **Trafik:** Ücretsiz halka açık kaynaktan (SimilarWeb public) güvenilir bir ziyaretçi sayısı alınamadı (bot korumalı, 202/boş yanıt). Not olarak bırakıldı. [kaynak 7]

---

## 2. Kayıt bilgileri (WHOIS / RDAP)

Kaynak: Verisign RDAP (`rdap.org` → `rdap.verisign.com/com`) [kaynak 1]. `whois` istemcisi ortamda yoktu; RDAP JSON kullanıldı.

| Alan | Değer |
|---|---|
| Alan adı | `AYDINOZTURK.COM` |
| Handle (Verisign) | `3067335852_DOMAIN_COM-VRSN` |
| Registrar | **NameCheap, Inc.** (IANA Registrar ID **1068**) |
| Abuse e-posta | `abuse@namecheap.com` |
| **Registration (kayıt)** | **2026-02-13 08:32:04Z** |
| **Expiration (süre sonu)** | **2027-02-13 08:32:04Z** (≈ 1 yıllık kayıt) |
| Last changed | 2026-08-15 15:01:10Z |
| Last RDAP DB update | 2026-11-05 16:16:03Z (erişim anı) |
| Durum (status) | `client transfer prohibited` (transfer kilitli) |
| DNSSEC | **imzalı değil** (`delegationSigned: false`) |
| Nameserver'lar | `sid.ns.cloudflare.com`, `teagan.ns.cloudflare.com` (Cloudflare) |

**Not / yorum:** Verisign `.com` RDAP'ı yalnızca aktif registrar kaydını döndürür. "Registration 2026-02-13" ilk kez tescil tarihi **değildir**; arşiv kanıtları (Bölüm 4) alan adının 2005–2010'dan beri var olduğunu gösterir. 2026-02-13, alan adının NameCheap'ta (yenilenme/transfer-in) kayda alındığı tarihtir. `client transfer prohibited` + tek yıllık expiry, alan adının aktif biçimde koruma altında ve kısa döngüyle yenilendiğini gösterir.

---

## 3. DNS kayıtları

Kaynak: Cloudflare DNS-over-HTTPS (`1.1.1.1/dns-query`, `application/dns-json`), erişim 2026-11-05. [kaynak 2]. (`dig` ortamda yoktu.)

| Tip | Değer | TTL | Not |
|---|---|---|---|
| A | `172.67.214.38` | 300 | Cloudflare edge |
| A | `104.21.16.159` | 300 | Cloudflare edge |
| AAAA | `2606:4700:3031::ac43:d626` | 297 | Cloudflare IPv6 |
| AAAA | `2606:4700:3034::6815:109f` | 297 | Cloudflare IPv6 |
| MX | `23 route1.mx.cloudflare.net.` | 300 | Cloudflare e-posta |
| MX | `71 route2.mx.cloudflare.net.` | 300 | Cloudflare e-posta |
| MX | `30 route3.mx.cloudflare.net.` | 300 | Cloudflare e-posta |
| NS | `sid.ns.cloudflare.com.` | 86400 | |
| NS | `teagan.ns.cloudflare.com.` | 86400 | |
| TXT | `"google-site-verification=d5wTpN92CvDVdBegEI7uJHMNK0fCOd8KZu1hDFm-O7I"` | 300 | Site Search doğrulaması |
| TXT | `"v=spf1 include:_spf.mx.cloudflare.net ~all"` | 300 | SPF (Cloudflare) |
| SOA | `sid.ns.cloudflare.com. dns.cloudflare.com. 2417475952 10000 2400 604800 1800` | — | Serial `2417475952` |
| www A | `172.67.214.38`, `104.21.16.159` | 300 | `www` doğrudan A (CNAME yok) → Cloudflare |
| www AAAA | `2606:4700:3031::ac43:d626`, `2606:4700:3034::6815:109f` | 300 | |

**Yorum:** A/AAAA/MX/NS/TXT/SOA kayıtlarının tamamı **Cloudflare** altyapısına işaret ediyor (edge IP'ler, Cloudflare MX, Cloudflare NS, Cloudflare SPF). Site Cloudflare arkasında servis ediliyor. `google-site-verification` TXT kaydı, site sahibinin Google Search Console doğrulaması yaptığını gösterir.

---

## 4. Arşiv geçmişi (Wayback Machine / Internet Archive)

Kaynak: CDX API (`web.archive.org/cdx`) + `archive.org/wayback/available`, erişim 2026-11-05. [kaynak 5]

- **Toplam arşiv görüntüsü:** ~82 kayıt (aynı zaman damgasına çözülmüş `collapse=timestamp:6` ile 81; `aydinozturk.com*` yığını için).
- **İlk arşiv izi:** `robots.txt` — **2005-09-05** (200 OK). Kök sayfa için en erken görüntü: `www.aydinozturk.com:80/` — **2010-03-23** (200 OK).
- **En yakın görüntüler:** kök sayfa 2019'dan sonra **2021-11-25** ve **2025-07-10** (sonuncusu `warc/revisit`).
- **Boşluklar (coverage gap):** kök sayfada 2019 → 2021 ve 2021 → 2025 arasında arşiv görüntüsü yok; arşiv, her yıl düzenli tarama yapılmadığını gösterir (belirli aralıklarla crawler ziyareti).
- Arşivdeki yolların büyük çoğunluğu kök sayfa (`/`), `/robots.txt`, `/favicon.ico` ile sınırlı → arşivde derin sayfa taraması yapılmamış.

### İçerik değişimi (tarihçe ipuçları)

| Tarih | Yol | Durum | Gözlem |
|---|---|---|---|
| 2010-03-23 | `www.aydinozturk.com/` | 200 | Başlık: **"Cuneyt SARIKAYA - Cuneyt SARIKAYA"** → dönemin içeriği başka bir kişiye aitti [kaynak 5] |
| 2011-02-01 | `aydinozturk.com/` | 200 | ~2,4 KB, neredeyse boş HTML gövde |
| 2015-08-01 | `aydinozturk.com/` | 200 | ~2,4 KB, neredeyse boş HTML gövde |
| 2021-11-25 | `aydinozturk.com/` | (503 erişim anında) | Arşiv "Temporarily Offline" döndürdü; içerik okunamadı |

**Yorum:** Alan adı 2010'da başka bir kişi/content ile aktif iken, bugünkü "Aydın Öztürk" kişisel markası çok sonra kurulmuştur. 2011/2015 görüntülerinin neredeyse boş olması, o dönemlerde sitenin ya boş bırakıldığını ya da içeriksiz bir alan olduğunu düşündürür. (2021 görüntüsünü erişim anında arşiv geçici olarak çevrimdışıydı; tekerrar ile yeniden okunabilir.)

> `archive.org/wayback/available?url=aydinozturk.com` anlık olarak boş yanıt döndürdü; CDX verisi üzerinden görüntüleme tarihi ve sayısı yukarıda verildi. [kaynak 5]

---

## 5. Çevrimiçi varlık (profiller & mention)

### GitHub — güçlü kimlik eşleşmesi [kaynak 6]
- Kullanıcı: [`github.com/aydinozturk`](https://github.com/aydinozturk) — ad **"Aydın Öztürk"**
- Konum: **Kocaeli, Turkey** · Firma: **Uzmar Technologies** · Bio: "Software Development Manager"
- Profil `blog` alanı: **aydinozturk.com** (doğrudan bu alan adı)
- Hesap **kuruluşu: 2016-08-14** · 17 açık repo · 24 takipçi · 39 takip
- İlgili repo örnekleri (alanıyla tutarlı — gemi/savunma/sanayi yazılımı):
  - `S1000D` (Savunma dokümantasyonu standardı / oXygen XML), `VDMS`, `uzmar.modbus`, `orkestra-integration-provider` (Go) — Uzmar'a ait
  - `elm327-tcp-simulator` (OBD2), `tesla-bot` (Java, 3★), `cyrpto-bot`/`cyrpto-predict` (Python/ML), `agents-room` (TypeScript), `aydinozturk.github.io` (HTML)
- Repo araması `aydinozturk` = 2 sonuç; `research` repo'su bu masanın (Plan #260) paylaşım deposudur.

### Site'deki dış profiller / kimlik bilgileri [kaynak 3]
- **LinkedIn:** `linkedin.com/in/aydinozturk` (site içinden bağlantılı) — doğrudan doğrulanamadı (LinkedIn bot/giriş korumalı).
- **E-posta:** `hello@aydinozturk.com` (iletişim).
- X/Twitter, Google Scholar, GitLab, StackOverflow vb. site üzerinden **bağlantılı değil**; bu profillerin varlığı bu ortamda bağımsız olarak doğrulanamadı.

### Diğer profiller
- **X/Twitter, Google Scholar, Facebook, Instagram:** bu ortamda web arama aracı kullanılamıyordu (hata) ve bu platformlar doğrudan sorguya (API/giriş) kapalı olduğundan **bulunamadı/kanıtlanamadı**. Olumsuz sonuç değil — "erişim yöntemi yok" olarak not edildi. (Bölüm 8, sınırlamalar.)

---

## 6. Trafik tahmini

- **SimilarWeb (public):** `similarweb.com/website/aydinozturk.com` erişimi bot koruması nedeniyle boş yanıt (HTTP 202, 0 bayt) verdi → güvenilir halka açık ziyaretçi sayısı **alınmadı**. [kaynak 7]
- **Bulgu:** Kişisel/portföy bir sitede halka açık ücretsiz trafik verisi bulunmaması beklenen bir durum; bu, alan adının düşük/yüksek trafikli olduğu hakkında bir yorum taşımaz. Alternatif ücretsiz kaynak (örn. public "similarweb-lite", Semrush public) denenmedi.

---

## 7. Değerlendirme

1. **Alan adı uzun süredir mevcut:** 2005 (robots.txt) / 2010 (kök) arşiv izleri, 2026 kayıt tarihinden ~15–21 yıl öncesine dayanır. Bugünkü NameCheap kaydı (2026-02-13) ilk tescil değil, mevcut kayıt/transferdir.
2. **Sahiplik değişimi:** 2010'da alan adı farklı bir içeriğe (başka bir kişi, "Cuneyt SARIKAYA") aitti. Bugünkü "Aydın Öztürk" kişisel markası daha sonraki bir sahiplik döneminde kurulmuştur.
3. **Bugünkü varlık net ve tutarlı:** Site (şifreli, Cloudflare arkası, Google doğrulamalı), GitHub (ad+konum+firma+blog eşleşmeli, 2016'dan beri) ve LinkedIn (site bağlamında) tek bir kişiye — **Aydın Öztürk, Kocaeli/Türkiye, Uzmar Technologies** — işaret ediyor. Teknik alan: gemi inşa / savunma dokümantasyonu / sanayi IoT / UML-temelli sistem mimarisi.
4. **Operasyonel durum:** Alan adı `client transfer prohibited`, kısa süreli (1 yıl) expiry ve Cloudflare üzerinden çalışıyor → aktif biçimde yönetiliyor, koruma altında.

---

## 8. Kaynaklar & sınırlamalar

### Kaynaklar (erişim 2026-11-05)
1. **RDAP/WHOIS:** `https://rdap.org/domain/AYDINOZTURK.COM` → `https://rdap.verisign.com/com/v1/domain/aydinozturk.com` (registrar, tarihler, status, NS, DNSSEC).
2. **DNS:** Cloudflare DNS-over-HTTPS `https://1.1.1.1/dns-query?name=aydinozturk.com&type={A,AAAA,MX,NS,TXT,SOA}` (+ `www.`).
3. **Mevcut site:** `https://aydinozturk.com/` (başlık, meta description, H1, EN/TR, LinkedIn + e-posta bağlantıları).
4. **ICANN status:** `client transfer prohibited` (EPP status kodları) — [kaynak 1] ile.
5. **Wayback/Archive:** `http://web.archive.org/cdx/search/cdx?url=aydinozturk.com*&...` (görseller, tarihler, sayı) + `https://archive.org/wayback/available?url=aydinozturk.com` + örnek görüntüler (`/web/<ts>id_/http://...`).
6. **GitHub:** `https://api.github.com/users/aydinozturk` (profil) + `.../users/aydinozturk/repos` (repo listesi) + `.../search/repositories?q=aydinozturk`.
7. **Trafik:** `https://www.similarweb.com/website/aydinozturk.com/` (bot-korumalı, veri alınamadı).

### Sınırlamalar / bulunamayanlar (açıkça)
- **`whois` istemcisi ve `dig` ortamda yoktu** → sırasıyla RDAP JSON ve Cloudflare/Google DoH kullanıldı (equivalent sonuç).
- **Web arama aracı (WebSearch) bu ortamda kullanılamadı** (araç düzeyinde hata). Bu yüzden **X/Twitter, Google Scholar, Facebook, Instagram** profilleri ve dış **backlink/mention** listesi bağımsız olarak derlenemedi; yalnızca site'nin kendisinin açtığı bağlantılar (LinkedIn, e-posta) raporlandı.
- **LinkedIn** sayfası doğrulanamadı (bot/giriş koruması); yalnızca site üzerinden referans olarak alındı.
- **2021-11-25 arşiv görüntüsü** erişim anında arşivin geçici çevrimdışılığı (503) nedeniyle okunamadı; tekerrar ile alınabilir.
- **Trafik** halka açık ücretsiz kaynaktan alınamadı.
- **Orijinal ilk kayıt tarihi** (Verisign "created") .com RDAP'ında ayrı bir alan olarak dönmedi; ilk kullanım arşiv izlerinden (2005/2010) çıkarıldı.

---
*Bu rapor #263 görevi için otomatik derlendi. Her maddede kullanılan kaynak yukarıda numaralandırıldı; erişemeyen noktalar "Sınırlamalar" altında açıkça belirtildi.*
