# Teknik Site Analizi: aydinozturk.com

- **Analiz tarihi:** 2026-11-05 (UTC, saat ~16:16–16:20)
- **Analiz eden:** agent-3 (curl + openssl üzerinden; kaynak IP/edge: Cloudflare SOF/IST ray'leri görüldü)
- **Yöntem:** Tüm bulgular `curl` (başlık + gövde indirme) ve `openssl s_client` çıktılarıyla doğrulandı. Her bulgunun yanında kaynak URL ve gözlenen çıktı değeri verilir.

## 1. Özet

| Alan | Durum | Kısa not |
|---|---|---|
| Erişilebilirlik | ✅ Sağlam | HTTP/2, tüm sitemap URL'leri 200, özel 404 sayfası |
| Performans | ✅ İyi | TTFB ~160–190 ms, ana sayfa 6,7 KB (brotli), minimal asset |
| Mobil uyum | ✅ Mevcut | `viewport` meta tüm sayfalarda; CSS'te 1 `@media` sorgusu |
| Güvenlik başlıkları | ⚠️ Eksik | HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy yok |
| HTTPS zorlaması | ⚠️ Eksik | `http://` 301 yerine 200 döndürüyor (Always Use HTTPS kapalı) |
| Teknoloji | ℹ️ | Statik **Astro** site, Cloudflare CDN arkasında |

## 2. Altyapı ve CDN

| Bulgu | Kaynak / Kanıt |
|---|---|
| Cloudflare arkasında | `GET https://aydinozturk.com/` → `server: cloudflare`, `cf-ray: a55d29645d2fd0d3-SOF`, `cf-cache-status: HIT` |
| HTTP/2 aktif | `curl --http2 -I https://aydinozturk.com/` → `HTTP/2 200` |
| HTTP/3 reklam ediliyor (doğrulama kısıtlı) | Başlıklarda `alt-svc: h3=":443"; ma=86400`. **Not:** bu ortamda curl/libcurl HTTP/3 desteği taşımadığı için (`curl: option --http3: the installed libcurl version doesn't support this`) gerçek QUIC/h3 yanıtı doğrulanamadı — yalnızca sunucunun reklam ettiği kabul edilir. |
| TLS sertifikası | `openssl s_client -connect aydinozturk.com:443` → issuer `C=US, O=Google Trust Services, CN=WE1`, subject `CN=aydinozturk.com`, SAN `DNS:aydinozturk.com, DNS:*.aydinozturk.com`, geçerlilik **2026-10-13 → 2027-01-11** (analiz gününde geçerli, ~2 ay önce yenilenmiş) |
| Kenar önbelleği aktif | Ana sayfa, CSS ve diğer URL'lerde `cf-cache-status: HIT` (Cloudflare kenarında önbellekleniyor) |

## 3. Sayfa Yapısı ve Alt Sayfalar

Sitemap (`https://aydinozturk.com/sitemap-index.xml` → tek alt sitemap `sitemap-0.xml`, 1999 B) **17 URL** içerir; tümü `curl` ile kontrol edildi, **hepsi 200** döndürdü:

| Grup | URL | Durum (kod, brotli boyut) |
|---|---|---|
| Ana sayfa (EN) | `https://aydinozturk.com/` | 200, 6.706 B |
| Ana sayfa (TR) | `https://aydinozturk.com/tr/` | 200, 7.382 B |
| Vaka çalışması (EN) | `/case-studies/camera-based-production-tracking/` | 200 (sitemap'te listeli) |
| Vaka çalışması (EN) | `/case-studies/llm-agents-on-a-legacy-erp/` | 200 |
| Vaka çalışması (EN) | `/case-studies/rebuild-or-integrate/` | 200 |
| Vaka çalışması (EN) | `/case-studies/shipyard-erp-turnaround/` | 200 |
| Vaka çalışması (EN) | `/case-studies/talking-to-an-erp/` | 200 |
| Vaka çalışması (EN) | `/case-studies/vessel-telemetry-platform/` | 200, 2.532 B |
| Vaka çalışması (TR) | `/tr/projeler/erp-ile-konusmak/`, `/tr/projeler/gemi-telemetri-platformu/`, `/tr/projeler/kamera-tabanli-uretim-takibi/`, `/tr/projeler/llm-agentlari-ve-eski-kod/`, `/tr/projeler/tersane-erp-donusumu/`, `/tr/projeler/yeniden-yazmak-mi-entegre-olmak-mi/` | 200 (sitemap'te listeli) |
| Gizlilik sayfaları | `/driveinsight/privacy/` (200, 2.565 B), `/zapp/privacy/` (200, 2.141 B), `/tr/driveinsight/gizlilik/` (200, 2.826 B), `/tr/zapp/gizlilik/` (200, 2.386 B) | 200 — **ana sayfadan linki olmayan (orphan) sayfa gibi görünüyor**; yalnızca sitemap ve kendi iç yapılarından ulaşılıyor. Muhtemelen eski/ticari (DriveInsight, Zapp) ürünlerin artıkları. |

Diğer yapısal gözlemler:

- **404 davranışı doğru:** `GET https://aydinozturk.com/nonexistent-page-12345/` → `404` (1.258 B brotli), özel 404 sayfası (`<title>404 — Aydın Öztürk</title>`). Kaynak: aynı curl çıktısı.
- Ana sayfa **tek sayfa (one-page)** düzeninde: bölüm linkleri `/#work`, `/#expertise`, `/#about`, `/#contact` (home HTML içindeki `href` taraması).
- **Dil eşleştirmesi (hreflang) kurulu:** ana sayfada `<link rel="alternate" hreflang="en|tr|x-default">`; vaka sayfasında EN↔TR karşılığı doğru eşleştirilmiş (örn. `vessel-telemetry-platform` ↔ `tr/projeler/gemi-telemetri-platformu`). `lang` attribute'ları da doğru: EN sayfalarda `<html lang="en">`, TR'da `<html lang="tr">`.
- **Canonical link'ler var** ve apexe işaret ediyor (örn. `<link rel="canonical" href="https://aydinozturk.com/tr/">`).
- Dış bağlantılar: `mailto:hello@aydinozturk.com` ve `https://www.linkedin.com/in/aydinozturk` (home HTML taraması).

## 4. Teknoloji Yığını (HTML işaretlerinden)

| Bulgu | Kanıt |
|---|---|
| **Astro** (statik site jeneratörü) | CSS/JS asset yolları `/_astro/Base.DEmIqWG6.css`, `/_astro/BlockFigure.astro_astro_type_script_index_0_lang.DfH24cVg.js` — `._astro/` + hash'li adlandırma Astro imzası; `.astro_astro_type_script` dosya adı Astro derlemesinin doğrudan izi |
| Minimal istemci JS | Ana sayfada yalnızca 1 harici JS modülü (2.146 B, `type="module"`) + 2 `<script>` etiketi; framework runtime'ına (React/Vue vb.) işaret eden hiçbir asset yok |
| CSS tek dosya | `/_astro/Base.DEmIqWG6.css` (9.722 B) |
| Görsel kaynaklar | `og.png` (65.463 B, `image/png`), `favicon.svg` (204 B, `image/svg+xml`). Ana sayfa HTML'inde `<img>` etiketi **bulunamadı** (içerik ağırlıklı metin tabanlı) |
| Harici (3. parti) kaynak | Ana sayfada tek harici host: `www.linkedin.com` (profil linki). Takipçi/analitik script izi HTML'de yok — **not:** HTML taramasında görünenler; gizli beacon'lar bu analizle doğrulanamaz |

## 5. Performans Sinyalleri

| Metrik | Değer | Kaynak |
|---|---|---|
| TTFB (ana sayfa, 3 numune) | 0,190 s / 0,165 s / 0,157 s | `curl -w 'time_starttransfer'` ×3, `https://aydinozturk.com/` |
| TTFB (TR sayfa) | 0,183 s | aynı yöntem |
| Ana sayfa HTML boyutu | 23.746 B ham / **6.706 B brotli** | `curl -w 'size_download'`, `Accept-Encoding: gzip, br` |
| Sıkıştırma | **Brotli aktif** (istek üzerine `content-encoding: br`) | `curl -H 'Accept-Encoding: gzip, br' -D -` çıktısı |
| CSS / JS | 9.722 B / 2.146 B | `curl` boyut ölçümü, ilgili URL'ler |
| Sayfa ağırlığı (genel) | Ana sayfa toplamında ~78 KB (HTML + CSS + JS + og.png); vaka sayfaları ~2,5 KB brotli | toplam yukarıdaki değerlerden |

Sonuç: çok hafif bir statik site; tek belirgin "ağırlık" 65 KB'lık `og.png` (yalnızca sosyal paylaşım önizlemesi için yüklenmez, normal gezinmede etkisi yok).

## 6. Güvenlik Başlıkları

`GET https://aydinozturk.com/` tam başlık taraması (grep: `strict-transport | content-security | x-frame | x-content-type | referrer-policy | permissions-policy | set-cookie`):

| Başlık | Durum |
|---|---|
| `Strict-Transport-Security` (HSTS) | ❌ Yok |
| `Content-Security-Policy` | ❌ Yok |
| `X-Frame-Options` / `frame-ancestors` | ❌ Yok (sayfa çerçeveye alınabilir → clickjacking için teknik pencere açık) |
| `X-Content-Type-Options: nosniff` | ❌ Yok |
| `Referrer-Policy` | ❌ Yok |
| `Permissions-Policy` | ❌ Yok |
| `Set-Cookie` | Yok (çerez yok — artı) |
| `.well-known/security.txt` | ❌ 404 |

### ⚠️ Önemli bulgu: HTTP → HTTPS yönlendirmesi yok

`curl http://aydinozturk.com/` (takip olmadan) → **`HTTP/1.1 200 OK`, `redirects=0`**. Site düz HTTP üzerinden de tam içeriği sunuyor; Cloudflare "Always Use HTTPS" açık değil. HSTS başlığının da olmamasıyla birlikte, ilk ziyaret HTTP ile yapıldıysa içerik şifresiz aktarılabilir. Öneri: Cloudflare'de **Always Use HTTPS** + **HSTS başlığı** (önce `max-age` düşük, sonra artırımlı) etkinleştirmek.

### ✅ Pozitif güvenlik izleri

- Sadece 443/200 ile çalışır, TLS sertifikanın yayıncısı CA (Google Trust Services / Cloudflare ekosistemi), wildcard kapsamı doğru.
- `robots.txt` Cloudflare yönetimli **AI-training blok listesi** içeriyor (`Content-Signal: search=yes,ai-train=no,use=reference` + GPTBot, ClaudeBot, CCBot, Amazonbot vb. `Disallow: /`). Kaynak: `GET https://aydinozturk.com/robots.txt` (2.751 B, 200). Bu, içerik sahipliğinde bilinçli bir ayar (koruma niyeti).
- Hata sayfalarında sunucu/sürüm bilgisi sızdırılmıyor; 404 özel sayfa.

## 7. Mobil Uyum

| Bulgu | Kanıt |
|---|---|
| Viewport meta tüm sayfalarda | `<meta name="viewport" content="width=device-width, initial-scale=1">` — ana sayfa, vaka sayfası ve TR sayfası HTML taraması |
| Responsive CSS | `/_astro/Base.DEmIqWG6.css` içinde **1 adet `@media` sorgusu** (az ama mevcut; sayfa ağırlıklı metin olduğundan sınırlı kırılım yeterli görünüyor) |
| `lang` attribute'ları | `<html lang="en">` / `<html lang="tr">` (ekran okuyucu/dil doğru) |

## 8. Notlar ve Eksik Veriler (şeffaflık)

1. **HTTP/3 doğrulanamadı:** ortamın libcurl sürümü QUIC desteklemiyor; yalnızca `alt-svc` reklamı görüldü.
2. **Gerçek tarayıcı metrikleri (LCP, CLS, TBT, tam sayfa yüklenme) yok:** bu analiz sunucu tarafı (curl) sinyalleridir; PageSpeed Insights / Lighthouse koşularıyla desteklenmesi önerilir.
3. **JS ağ istekleri** (runtime'da yüklenen gizli kaynaklar) statik HTML taramasıyla görülemez.
4. **Orphan gizlilik sayfaları** (`/driveinsight/privacy/`, `/zapp/privacy/` + TR karşılıkları) ana sayfadan linklenmiyor; içerik sahipliği ve niyeti bilinmiyor (muhtemelen eski ürün artığı).
5. `www.aydinozturk.com` da 200 dönüyor (redirect yok); canonical tag apex'e işaret ettiği için SEO'da çifte içerik riski düşük, ama tek bir kanonik hosta 301 yönlendirmek iyi uygulama olur.

## 9. Kaynak Komutları (tekrarlanabilirlik)

```bash
curl -sS -I --http2 https://aydinozturk.com/                    # HTTP/2 + başlıklar
curl -sS -D - -o /dev/null http://aydinozturk.com/              # HTTP davranışı (200, redirect yok)
curl -sS -H 'Accept-Encoding: gzip, br' -D - -o /dev/null https://aydinozturk.com/   # brotli + boyut
curl -sS https://aydinozturk.com/sitemap-index.xml              # sitemap endeksi
curl -sS https://aydinozturk.com/sitemap-0.xml                  # 17 URL
curl -sS https://aydinozturk.com/robots.txt                     # AI-training blokları
echo | openssl s_client -connect aydinozturk.com:443 -servername aydinozturk.com \
  | openssl x509 -noout -issuer -subject -dates -ext subjectAltName   # TLS
curl -sS -w 'TTFB=%{time_starttransfer}\n' -o /dev/null https://aydinozturk.com/   # TTFB
```
