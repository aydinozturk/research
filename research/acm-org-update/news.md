# acm.org — Haberler ve Duyurular

**Görev:** #284 · **Araştırma aralığı:** 2026-10-23 → 2026-11-06 (son ~2 hafta)
**Yöntem:** Doğrudan `curl` acm.org'a Cloudflare 403 verdiği için gerçek Chrome tarayıcısı üzerinden gezildi (CDP `http://192.168.65.254:9222`, Chrome/156.0.8078.80). Kendi sekmem açıldı, consent kabul edildi, DOM okundu, bitince sekme kapatıldı. Admin'ın sekmelerine (özellikle caddyserver) dokunulmadı.

## TL;DR

acm.org'da `https://www.acm.org/news` adresi artık **`https://www.acm.org/media-center`**'a (Medya Merkezi) yönlendiriyor; tarihli duyurular **ACM Updates** alt sayfasında toplanıyor. İstenen **2 haftalık pencerede (23 Ekim–6 Kasım) yalnızca 1 maddenin tarihi net olarak düşüyor** (5 Kasım ETPC Webinar'ı) + 1 tarih belirtilmemiş madde (PQQS 2026, 2–4 Kasım konferansı). Sitede bu pencere gerçekten az maddeli; bu yüzden hemen öncesindeki erken-orta Ekim duyuruları da bağlam olarak eklendi. En taze **medya haberi** (ACM in the News) 25 Eylül 2026'da — pencere dışında.

## ✅ Pencere içinde (2026-10-23 → 2026-11-06)

### 1. ETPC Webinar'ı: "European Social Media Ban: Design, Practicality, and Consequences"
- **Tarih:** 5 Kasım 2026 *(sitede yazım hatası: "Novmber 5, 2026")*
- **Kaynak:** https://www.acm.org/media-center/acm-updates
- **Özet:** Avrupa'da hükümetlerin çocukların sosyal medyaya erişimini kısıtlamaya yönelik adımları ve Digital Services Act çerçevesinde bu sınırların nasıl uygulanacağı tartışılırken, ACM Europe Technology Policy Committee (ETPC) konuyla ilgili bir webinar düzenliyor. Panel, sivil toplum, çocuk hakları savunuculuğu ve dijital haklar örgütlerinden sesleri bir araya getiriyor. Webinar'ın kendisi **4 Aralık 2026**'da (3 pm CET / 2 pm UTC) yapılacak.
- **Kayıt/link:** https://events.zoom.us/ev/AjkmqJxoxzddTodFzm2Fr2HCIm9H1PiD5xDmKp5EPQRe7ek5JvCW~AmbfQae9ofcyRwSX59a37-XMpAg7tC1kFPf6gy__7Ap3s91PzJLvc-fO5w

### 2. PQQS 2026 — İlk Post-Quantum ve Quantum-based Security Konferansı (2–4 Kasım)
- **Tarih:** *listelenen maddede açık tarih satırı YOK.* Listede en-yeni-ilk sırasına göre 5 Kasım ETPC maddesinin hemen altında, 9 Ekim maddesinin üstünde yer alıyor → duyuru muhtemelen ekim sonu/kasım başına denk düşer (pencereye sınırdır).
- **Kaynak:** https://www.acm.org/media-center/acm-updates
- **Özet:** ACM SIGSAC, ilk "ACM Conference on Post-Quantum and Quantum-based Security" (PQQS) konferansını duyurdu. Siber güvenlik, post-kuantum kriptografisi, kuantum kriptografisi ve kuantum bilişim sistemleri/altyapısı kesişiminde araştırma odağında yeni bir yıllık platform. Konuşmacılar arasında Turing ödüllüsü **Charles H. Bennett (IBM)**, Renato Renner (ETH Zürich), Dan Boneh (Stanford) ve Ryan Babbush (Google Quantum AI) var. Konum: **San Jose, Kaliforniya, 2–4 Kasım 2026.**
- **Link:** https://acm-pqqs.github.io/pqqs2026/

> Not: Bu iki madde dışında net bir tarihe sahip olan başka duyuru, 23 Ekim–6 Kasım aralığına **düşmüyor** (bkz. alttaki bağlam bölümü). Yani acm.org duyuru akışında bu 2 haftalık pencere gerçekten sınırlı miktarda içerik üretiyor.

## 📅 Bağlam: hemen öncesindeki duyurular (pencere dışı, erken–orta Ekim)

Bu maddeler istenen 2 haftadan biraz daha eski ama "acm.org'da ne yenisi var?" sorusunu tam cevaplamak için eklendi:

| Tarih | Başlık | Özet | Link |
|---|---|---|---|
| 9 Eki 2026 | **Global Technology Policy at ACM** (webinar) | ACM'nin bölgesel politika komiteleri (USTPC, Europe TPC, Expanding Regions) liderleri "dünyada politikada neler oluyor" webinar'ında bir yıl dolan bölgesel genişlemeyi ve gelecek öncelikleri ele alıyor. **4 Kasım 2026** 10:00–11:30 EDT. | https://events.zoom.us/ev/AqBzmaVW-DARLHw1LPLNm-yuuQ06KtelUTH-I3xTk6q3rjmQZgQ0~Akl7_Zign9dy6qIJQdjhup_47IK-1JBSQsRknfI5x93qSegqZw708argHg |
| 1 Eki 2026 | **TOMACS yeni Co-EiC'ler** | ACM Transactions on Modeling and Computer Simulation; yeni eş editörler Jason Liu (Florida International University) ve Steffen Strassburger (Ilmenau University of Technology, DE). | https://dl.acm.org/journal/tomacs |
| 30 Eyl 2026 | **African Union AI Yönetişimi Açık Danışması** | ACM Africa Subcommittee, Afrikada AI yönetişimi/düzenlemesi için Afrik Birliği'nin açık danışmasına yanıt veriyor; hem etik hem kapsayıcı bir yaklaşımı destekliyor. | https://www.acm.org/public-policy/er-tpc/african-open-consultation-ai-governance-regulation-10052026 |
| 25 Eyl 2026 | **TAAI yeni Co-EiC'ler** | Yeni onaylanan dergi ACM Transactions on Agentic AI (TAAI) — ajan (agentic) zekâ araştırması — yeni eş editörlerini karşılıyor. | https://dl.acm.org/journal/taai |

*(Listedede ayrıca 19 Eyl "2027 ACM Asian School on HPC and AI" başvuru duyurusu ve 13 Eyl "2026 Heidelberg Laureate Forum" özeti var.)*

## 📰 ACM in the News (medyada ACM) — en taze

En yakın medya haberi **25 Eylül 2026**; pencere dışı:
- **"AI's Open Source Surge Recasts IT Services"** — *Channel Dive*, 25 Eyl 2026. "ACM TechBrief: AI's Effects on Open Source" yazarlarından Shrinivass AB, yapay zekâ kodlama artışında süreklı izleme ve tedarik zinciri görünürlüğü gereğine işaret ediyor.
- Öncekiler: "ACM Report Highlights Generative AI's Impact on Programming Education" (*Library Learning Space*, 27 Tem 2026); "SIGGRAPH 2026 Computer Animation Festival…" (*Yahoo Finance*, 19 Haz 2026).
- Kaynak sayfa: https://www.acm.org/media-center/acm-in-the-news

## Gezi̇len URL'ler

1. `https://www.acm.org/news` → 301/redirect `https://www.acm.org/media-center` (Medya Merkezi)
2. `https://www.acm.org/media-center` (ana sayfa — "News and Resources for Journalists")
3. `https://www.acm.org/media-center/acm-updates` (**ana haber kaynağı**, tarihli duyuru listesi)
4. `https://www.acm.org/media-center/acm-in-the-news` (medya haberleri)

*(Görev tanımındaki `/blogs` ve `/podcasts` opsiyonel sayfaları bu görevde incelenmedi; haber/duyuru içeriği Media Center > ACM Updates'te toplanmış durumda.)*

## Sınırlamalar / dürüstlük notları

- **Tarih:** PQQS 2026 maddesi listelenen sayfada açık tarih satırı taşımıyor; tarih, listenin en-yeni-ilk sıralamasından çıkarıldı (5 Kasım ve 9 Ekim arasında).
- **Sitede yazım hatası:** ETPC maddesinde tarih "Novmber 5, 2026" olarak yazılmış (doğrusu November).
- Pencere (23 Eki–6 Kas) gerçekten az içerik üretiyor; bu yüzden bağlam maddeleri (erken–orta Ekim) ayrıca sınıflandırıldı.
- Google SERP çapraz kontrolü ayrı bir görevde (#287, agent-6) yürütülüyor; bu rapor yalnızca acm.org sitesinin kendi duyuru akışına dayanıyor.
