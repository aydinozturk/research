# acm.org — Yayınlar: CACM ve Dergi Güncellemeleri

**Görev:** #285 (plan #283 — admin [3877]: "acm.org a bak bakalım yeni ne var?")
**Kapsam:** 2026-10-23 → 2026-11-06 (~son 2 hafta). CACM en son sayı + içerik, diğer dergi/magazine güncellemeleri.
**Yöntem:** acm.org doğrudan curl'e 403 (Cloudflare) → gerçek Chrome (CDP `http://192.168.65.254:9222`, Chrome/156.0.8078.80) üzerinden ham CDP ile gezildi: sekme aç → `Page.navigate` → `Runtime.evaluate` (DOM metni + linkler) → sekme kapat. CAPTCHA/consent duvarına takılan sayfa yok; cookie banner'ları DOM metninde gözüktü ama içeriği engellemedi.
**Kapsam dışı:** `dl.acm.org` (farklı alan adı; yalnızca acm.org ve acm.org alt alan adları gezildi).

---

## 1. CACM — En Son Sayı: Kasım 2026 (Vol. 69 No. 11)

- **Sayfa:** <https://cacm.acm.org/issue/november-2026/> — "November 2026 – Vol. 69 No. 11"
- CACM ana sayfasındaki "Latest Issue" ve "Table of Contents" bağlantıları bu sayıya işaret ediyor. Sayı, kasım ayının başında (1 Kasım dolaylarında) yayımlanmış; önceki sayı Ekim 2026 (Vol. 69 No. 10).
- **Dikkat:** CACM'in gerçek sitesi `cacm.acm.org` (alt alan adı). Görev tanımındaki `communica.acm.org` / `www.communica.acm.org` adresleri **DNS'te çözülmüyor** (NXDOMAIN) — eski CACM alan adı artık yok.
- Sayı sayfasında açık bir "kapak makalesi" işareti yok; aşağıdaki liste, sayfanın "Features" bölümündeki sırayla aynı.

### Kasım 2026 sayısındaki öne çıkan makaleler (Features)

| Makale | Yazar(lar) | Bölüm | Yayın tarihi | Link |
|---|---|---|---|---|
| AI and Communications of the ACM | James Larus | Opinion | 16 Eki 2026 | <https://cacm.acm.org/opinion/ai-and-communications-of-the-acm/> |
| The Techlash Is Back | Moshe Y. Vardi | Opinion | 30 Eki 2026 | <https://cacm.acm.org/opinion/the-techlash-is-back/> |
| When Will AI Cross the Human-Independence Threshold? | Shaoshan Liu | Opinion | 19 Eki 2026 | <https://cacm.acm.org/opinion/when-will-ai-cross-the-human-independence-threshold/> |
| Is Recursive Self-Improvement Really Here? | Logan Kugler | News | 16 Eki 2026 | <https://cacm.acm.org/news/is-recursive-self-improvement-really-here/> |
| Agency as a New Organizing Abstraction for Computer Science | Ian Foster | Opinion | 21 Eki 2026 | <https://cacm.acm.org/opinion/agency-as-a-new-organizing-abstraction-for-computer-science/> |
| A New Era for Inside Risks | Nancy Leveson | Opinion | 20 Eki 2026 | <https://cacm.acm.org/opinion/a-new-era-for-inside-risks/> |
| Web Scraping as Illegal Circumvention? | Pamela Samuelson | Opinion | 14 Eki 2026 | <https://cacm.acm.org/opinion/web-scraping-as-illegal-circumvention/> |
| The 'Coloniality Problem' in AI and the Call for 'Decoloniality' | Damian Eke | Opinion | 21 Eki 2026 | <https://cacm.acm.org/opinion/the-coloniality-problem-in-ai-and-the-call-for-decoloniality/> |
| 'MVPs Considered Harmful' Considered Harmful | Maximilian Speicher | Opinion | 8 Eki 2026 | <https://cacm.acm.org/opinion/mvps-considered-harmful-considered-harmful/> |
| Working on AI and Technology Policy in the U.S. Senate | Cynthia Bailey, Serena Booth, Soribel Feliz, Eoghan Stafford, Rebecca L. Voglewede, Kiri Wagstaff | Opinion | 7 Eki 2026 | <https://cacm.acm.org/opinion/working-on-ai-and-technology-policy-in-the-u-s-senate/> |
| Can VIBE Drive Development? Threats and Opportunities | Mayukh Mukhopadhyay | Opinion | 30 Eki 2026 | <https://cacm.acm.org/opinion/can-vibe-drive-development-threats-and-opportunities/> |
| Teaching Novice Computing and Programming in the Agentic AI Era | Kathi Fisler, Shriram Krishnamurthi, Michael Littman | Opinion | 19 Eki 2026 | <https://cacm.acm.org/opinion/teaching-novice-computing-and-programming-in-the-agentic-ai-era/> |
| Scalable and Personalized Oral Assessments Using Voice AI | Panos Ipeirotis, Konstantinos Rizakos | Practice | 13 Eki 2026 | <https://cacm.acm.org/practice/scalable-and-personized-oral-assessments-using-voice-ai/> |
| How Immigration and Federal Funding Sustain American AI Leadership | Nur Ahmed, Mehedi Mahmud Kaushik | Research and Advances | 20 Eki 2026 | <https://cacm.acm.org/research/how-immigration-and-federal-funding-sustain-american-ai-leadership/> |
| A Research Agenda for the Economics of Transformative AI | Erik Brynjolfsson, Anton Korinek, Ajay Agrawal | Research and Advances | 21 Eki 2026 | <https://cacm.acm.org/research/a-research-agenda-for-the-economics-of-transformative-ai/> |
| Toward a Theory of Data Ecology | Raul Castro Fernandez | Research and Advances | 2 Eki 2026 | <https://cacm.acm.org/research/toward-a-theory-of-data-ecology/> |
| Tailoring Elective Courses to Enhance Women's Participation in Computing | Naaz Sibia, Steven Bradley, Miranda Parker, Jack Parkinson, Rukiye Altin, Sara Hooshangi | Research and Advances | 15 Eki 2026 | <https://cacm.acm.org/research/tailoring-elective-courses-to-enhance-womens-participation-in-computing/> |
| Une Vie En Rose | J.I. Rime | Future Tense | 30 Eki 2026 | (sayı TOC'sünde; bağlantısı sayfa üzerinden) |

**Sayının genel damgası:** ağırlıklı olarak yapay zeka — AI bağımsızlık eşiği, rekürsif öz-iyileştirme, AI güvenliği (inside risks), AI politikası, vibe coding, AI'ın işgücü/ekonomi etkisi.

### Son 2 haftada (10-23 → 11-06) CACM'de çıkan yeni makaleler (sayı dışı + içinde)

| Makale | Yazar | Bölüm | Tarih | Link |
|---|---|---|---|---|
| AI Abundance or Luddite Revolution? | Peter J. Denning, Ted G. Lewis, Erol Gelenbe | Opinion | 5 Kas 2026 | <https://cacm.acm.org/opinion/ai-abundance-or-luddite-revolution/> |
| Why Enterprise AI Agents Need Transaction-Level Auditing | Rajeshkumar Rajaseakaran Nair | BLOG@CACM | 5 Kas 2026 | <https://cacm.acm.org/blogcacm/why-enterprise-ai-agents-need-transaction-level-auditing/> |
| The Real Cost of AI Code Shows Up 30 Days Later | Shubham Kumbhalkar | BLOG@CACM | 4 Kas 2026 | <https://cacm.acm.org/blogcacm/the-real-cost-of-ai-code-shows-up-30-days-later/> |
| Fix the Dropdown Before You Deploy the Model | Venkata Krishna Sai Neelisetti | BLOG@CACM | 4 Kas 2026 | <https://cacm.acm.org/blogcacm/fix-the-dropdown-before-you-deploy-the-model/> |
| The Septuagint Effect | Carlos Baquero | BLOG@CACM | 3 Kas 2026 | <https://cacm.acm.org/blogcacm/the-septuagint-effect/> |
| Every Autonomous AI Chip Needs a Safety Control Unit | Shaoshan Liu | BLOG@CACM | 3 Kas 2026 | <https://cacm.acm.org/blogcacm/every-autonomous-ai-chip-needs-a-safety-control-unit/> |
| The Techlash Is Back | Moshe Y. Vardi | Opinion | 30 Eki 2026 | <https://cacm.acm.org/opinion/the-techlash-is-back/> |
| Can VIBE Drive Development? Threats and Opportunities | Mayukh Mukhopadhyay | Opinion | 30 Eki 2026 | <https://cacm.acm.org/opinion/can-vibe-drive-development-threats-and-opportunities/> |

---

## 2. Diğer Dergi/Magazine Güncellemeleri

### Queue (ACM Queue) — son sayıdan makaleler
Queue ana sayfası <https://queue.acm.org/>. En yeni "featured" makaleler (DOI üzerinden):

| Makale | Yazar | Tarih | Link |
|---|---|---|---|
| Out of My Other Mind (AI bilinci) | Jim Waldo | 5 Eki 2026 | <https://queue.acm.org/doi/10.1145/3856383> |
| How Does Generative AI Change the Algorithmic Fairness Problem? | Maria De-Arteaga | 19 Eki 2026 | <https://queue.acm.org/doi/10.1145/3856382> |
| A Valid Tool Call Can Still Be an Invalid Effect | Scott Lee | 28 Eyl 2026 | <https://queue.acm.org/doi/10.1145/3839117> |
| CAFE(S): Your Agent Is Only As Good As Its Context | Brian Houck, Max Kanat-Alexander, Eirini Kalliamvakou, Margaret-Anne Storey, Nicole Forsgren | 24 Eyl 2026 | <https://queue.acm.org/doi/10.1145/3847288> |
| Finding the Real Bottleneck in Large-Scale ML Training | Ankit Sinha | 21 Eyl 2026 | <https://queue.acm.org/doi/10.1145/3839112> |
| Too Many DevEx Metrics, Too Little Guidance (Long Read) | — | — | <https://queue.acm.org/doi/10.1145/3831360> |
| How CHERIoT Provides Strong and Usable Isolation Without an MMU | David Chisnall | 9 Eyl 2026 | <https://queue.acm.org/doi/10.1145/3831361> |

Kapsamdaki (10-23 → 11-06) tek Queue makalesi: **Maria De-Arteaga, "How Does Generative AI Change the Algorithmic Fairness Problem?" (19 Eki 2026)** — 19 Ekim, kapsağın hemen öncesinde; sayı sonbahar sayısında.

### Dergi editörlük atamaları ("ACM Welcomes New EICs", www.acm.org/publications)
Kapsamdaki (10-23 → 11-06) tek yeni atama ilanı:

- **28 Eki 2026 — ACM Transactions on Quantum Computing (TQC):** yeni Editör Min-Hsiu Hsieh (Hon Hai/Foxconn Quantum Computing Research Center, Taipei, Tayvan). Görev süresi 1 Kas 2026 → 31 Eki 2029.

Hemen önceki (bağlam, kapsam dışı ama taze):
- **1 Eki 2026 — ACM Transactions on Modeling and Computer Simulation (TOMACS):** yeni Ko-Editörler Jason Liu (FIU), Steffen Strassburger (Ilmenau U.), Claudia Szabo (Adelaide U.). Görev 1 Eki 2026 → 30 Eyl 2029.
- **25 Eyl 2026 — ACM Transactions on Agentic AI (TAAI):** yeni onaylanmış derginin ilk Ko-Editörleri Bang Liu (Montréal U.) ve Yan Liu (USC). Görev 1 Eki 2026 → 30 Eyl 2029.

### Yeni ACM dergileri (www.acm.org/publications/new-journals)
Sayfadaki en taze kayıt:
- **ACM AI Letters (AILET):** ilk sayı **27 Mar 2026**'da yayımlandı (hızlı-yayın AI mecrası). Sayfa üzerindeki diğer yeni dergi kayıtları (TAISAP, TAIS, TOPML, PACMNET, PACMSE, JRC, JATS, ACM/IMS Journal of Data Science) tarih göstermiyor — 2 hafta kapsamına doğrudan giren yeni bir "ilk sayı" ilanı bu sayfadaki tarihler arasında görünmedi.

### Açık Erişim (OA) geçişi — bağlam
- **1 Oca 2026'dan itibaren tüm ACM dergileri Open Access** (www.acm.org/publications/journals). Aynı tarihten itibaren tüm ACM yayınları (magazinler dahil) OA olarak ücretsiz okunabilir/paylaşılabilir (www.acm.org/publications/magazines).
- Başkan Elisa Bertino'nun OA geçişi mesajı 11 Kas 2025 tarihli (www.acm.org/publications/message-to-the-community).

### Dijital Kütüphane + LLM tartışması (yayın politikası, taze)
- Başkan Elisa Bertino, ACM Dijital Kütüphanesi'nin LLM eğitimine açılması olasılığı hakkında topluluk görüşü topluyor (anket açık). Mesaj **23 Tem 2026** tarihli: <https://www.acm.org/about-acm/acm-pres-on-llms-and-the-dl>. "ACM Welcomes New EICs" bloğunun hemen üstünde, publications ana sayfasında hâlâ öne çıkarılmış durumda. Karar verilmiş değil; CACM'deki bir opinion makalesi bu tartışmayı tetikledi.

---

## 3. Gezilip veri çekilen URL'ler

- <https://www.acm.org/publications> — ana yayınlar sayfası (hub) + "ACM Welcomes New EICs" + LLM/OA blokları
- <https://www.acm.org/publications/journals> — dergi listesi + OA ilanı
- <https://www.acm.org/publications/magazines> — magazine listesi + OA ilanı
- <https://www.acm.org/publications/new-journals> — yeni dergiler
- <https://www.acm.org/publications/message-to-the-community> — OA geçiş mesajı (11 Kas 2025)
- <https://www.acm.org/about-acm/acm-pres-on-llms-and-the-dl> — LLM/DL mesajı (23 Tem 2026)
- <https://cacm.acm.org/> — CACM ana sayfa (son makaleler)
- <https://cacm.acm.org/issue/november-2026/> — **Kasım 2026 (Vol. 69 No. 11) TOC**
- <https://queue.acm.org/> — Queue ana sayfa (son makaleler, DOI linkleri)
- <https://www.communica.acm.org> / <https://communica.acm.org> — DNS NXDOMAIN (çözüm yok, eski alan adı)
- <https://www.acm.org/cacm> — CACM kısayolu (→ cacm.acm.org)

**Kaynak notu:** Tüm tarihler ve makale listeleri, gerçek Chrome/CDP ile sayfaların DOM metninden okundu; hiçbir içerik uydurulmadı. CACM'de kapak makalesi işareti sayfa üzerinde yok — yukarıdaki Features sıralaması sayfanın kendi sırasındadır.
