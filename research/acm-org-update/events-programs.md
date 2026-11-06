# acm.org — Etkinlikler, Programlar, Ödül/Teklif Haberleri

- **Araştırma tarihi:** 2026-11-06 (UTC)
- **Kapsam:** acm.org'da yakınlarda olan etkinlikler (konferans takvimi + yerel/çevrimiçi etkinlikler) ve son ~2 haftada duyurulan program / ödül / teklif (call for papers, burs, ödül) haberleri.
- **Yöntem:** acm.org doğrudan `curl` ile 403 (Cloudflare) döndürdüğü için gerçek Chrome üzerinden CDP ile gezildi (uç: `http://192.168.65.254:9222`, Chrome/156.0.8078.80). Çerez onayı her sayfada kabul edilip ham CDP (`/json/new` → `Page.navigate` → `Runtime.evaluate` → `/json/close`) kullanıldı.
- **Not (coğrafya):** Chrome'un çıkış IP'si Türkiye konut IP'si değil (daha önceki Google SERP araştırmasında çok dilli SERP başlıkları görülmüştü). Ancak acm.org içerik coğrafi kişiselleştirme yapmıyor; tüm sayfalar global olarak aynı geldi. Bu, etkinlik/ödül verilerini etkilemez.

## TL;DR

- **Bu hafta (6–12 Kas 2026) acm.org takviminde 8 büyük etkinlik var:** EAAMO '26, Koli Calling '26 (5–8), CIKM '26 (7–11), ICCAD '26 (8–12), ve 12'sine doğru MM '26 / SIGCITE / SIGCSE Virtual başlıyor.
- **En büyük etkinlik dalga 15–20 Kas 2026:** SC '26 (Supercomputing), SIGOPS ATC, CCS '26, ICAIF, HAI, VRST, HotNets aynı haftaya yığılmış.
- **Aralık 2026'da 3 dev:** SIGGRAPH Asia 2026, UCC, MUM, BDCAT, Compute '26 (ACM'nin yeni "Compute" konferansı).
- **Ödül tarafında son 2 haftada (23 Eki–6 Kas) resmi duyuru yok.** En taze ödül haberi **15 Ekim 2026**: ACM + IEEE CS, **Daniel Reed**'e **2026 Ken Kennedy Award** verdi. (Bunu doğrulayan medya merkezi basın bülteni: `2026/october/kennedy-award-2026`.)
- **Burs/teklif tarafında 2 taze "Apply" çağrısı var:** (a) **2027 ACM Asian School on HPC and AI** — başvurular **31 Ekim 2026** AoE'de kapandı (yeni kapandı), 1–5 Mart 2027 Singapur. (b) **2026 George Michael Memorial HPC Fellowship** kazananları 9 Eylül'de açıklandı, tören SC26'da (15–20 Kas).
- **Yeni yayın/program:** **ACM Transactions on Agentic AI (TAAI)** onaylanan yeni bir dergi; ilk Co-EiC'leri 25 Eylül'de duyuruldu. **PQQS 2026** (Post-Quantum and Quantum-based Security) SIGSAC'ın ilk yeni yıllık konferansı, 2–4 Kas 2026 San Jose.

---

## 1) Yaklaşan Etkinlikler (konferans takvimi)

Kaynak: `https://www.acm.org/conferences/conference-events` (aylık takvim, 1 Kas – 5 Aralık 2026 görünümü; bugün 6 Kas 2026).

### Bu hafta ve ötesi (6 Kas → 5 Ara 2026)

| Tarih | Etkinlik | Link |
|---|---|---|
| 5–8 Kas | Koli Calling '26 — 26th Koli Calling Intl. Conf. on Computing Education Research | https://www.kolicalling.fi/ |
| 7–11 Kas | CIKM '26 — 35th ACM Intl. Conf. on Information and Knowledge Management | https://cikm2026.diag.uniroma1.it/ |
| 8–12 Kas | ICCAD '26 — IEEE/ACM Intl. Conf. on Computer-Aided Design | https://iccad.com/ |
| 10–14 Kas | MM '26 — 34th ACM Intl. Conf. on Multimedia | https://2026.acmmm.org/ |
| 12–14 Kas | SIGCITE '26 — 27th Annual ACM Conf. on Cybersecurity and Information Technology Education | https://sites.google.com/view/acmsigcite2026conference/home |
| 12–15 Kas | SIGCSE Virtual 2026 — 2nd ACM Virtual Global Computing Education Conference | https://sigcsevirtual2026.acm.org/ |
| 14–17 Kas | ICAIF '26 — 7th ACM Intl. Conf. on AI in Finance | https://icaif2026.org/ |
| 15–18 Kas | SIGOPS ATC 2026 — 2026 ACM SIGOPS Annual Technical Conference | https://sigops.org/s/conferences/atc/2026/ |
| **15–20 Kas** | **SC '26 — Intl. Conf. for High Performance Computing (Supercomputing)** | http://sc26.supercomputing.org/ |
| 15–19 Kas | CCS '26 — ACM SIGSAC Conference on Computer and Communications Security | https://www.sigsac.org/ccs/CCS2026/ |
| 16–19 Kas | HAI '26 — Intl. Conf. on Human-Agent Interaction | https://hai-conference.net/hai2026/ |
| 16–18 Kas | VRST '26 — 32nd ACM Symposium on Virtual Reality Software and Technology | https://vrst.acm.org/vrst2026/ |
| 16–17 Kas | HotNets '26 — 25th ACM Workshop on Hot Topics in Networks | https://conferences.sigcomm.org/hotnets/2026/ |
| 16–18 Kas | SportsHCI'26 — 2nd Annual Conf. on Human-Computer Interaction and Sports | http://sportshci2026.com/ |
| 17–20 Kas | RACS '26 — Intl. Conf. on Resilience, AI and Cyber-Systems | https://www.sigapp.org/RACS/RACS2026/ |
| 18–20 Kas | SoCC '26 — ACM Symposium on Cloud Computing | https://acmsocc.org/ |
| 23–26 Kas | ISS '26 — Conference on Interactive Surfaces and Spaces | https://iss.acm.org/2026 |
| 23–26 Kas | MobiHoc '26 — 27th Intl. Symposium on Mobile Networks and Computing | https://www.sigmobile.org/mobihoc/2026/ |
| 29 Kas – 1 Ara | VRCAI '26 — 21st ACM SIGGRAPH Conf. on Virtual-Reality Continuum | https://vrcai.cn/ |

### Aralık 2026

| Tarih | Etkinlik | Link |
|---|---|---|
| 1–3 Ara | AINTEC '26 — Asian Internet Engineering Conference 2026 | https://interlab.ait.ac.th/aintec2026/ |
| 1–4 Ara | UCC '26 — 2026 IEEE/ACM 19th Intl. Conf. on Utility and Cloud Computing | https://ucc-conference.org/ |
| 1–4 Ara | BDCAT '26 — IEEE/ACM 13th Intl. Conf. on Big Data Computing, Applications and Technologies | https://bdcat-conference.org/ |
| 1–4 Ara | MUM '26 — Intl. Conf. on Mobile and Ubiquitous Multimedia | https://mum-conf.org/2026/ |
| **1–4 Ara** | **SIGGRAPH Asia 2026** | https://asia.siggraph.org/2026 |
| 2–5 Ara | ACI '26 — Intl. Conf. on Animal-Computer Interaction | https://www.aciconf.org/ |
| 2–5 Ara | WUWNET '26 — Intl. Conf. on Underwater Networks & Systems | https://wuwnet.acm.org/2026/ |
| 3–5 Ara | Compute '26 — ACM Compute Conference (yeni seri) | https://isigcse.acm.org/compute/2026/ |

### Önemli not — az önce kapanmış / devam eden etkinlikler (1–5 Kas)
Takvimin ilk kısmında (bugünden geriye) bu hafta kapanmış etkinlikler de görünüyor:
- **MICRO '26** — 59th IEEE/ACM International Symposium on Microarchitecture (1–4 Kas)
- **PQQS '26** — Post-Quantum and Quantum-based Security (2–4 Kas, San Jose) — SIGSAC'ın **ilk** yıllık konferansı
- **CHI PLAY '26 / UIST '26** — (2–5 Kas)
- **SIGSPATIAL '26** — 34th ACM Conf. on Geographic Information Systems (3–6 Kas)
- **EAAMO '26** — Equity and Access in Algorithms, Mechanisms, and Optimization (5–7 Kas)

## 2) Yerel / Bölgesel Etkinlikler (Chapters "Local Activities")

Kaynak: `https://www.acm.org/chapters/local-activities` (günlük yerel takvim; SIG ve öğrenci bölümü etkinlikleri).

6–8 Kas 2026 aralığında görünenler (örnek):
- **ACM GreekCHI-CYCHI Symposium 2026** — 6–7 Kas, Nikosia (Kıbrıs) + Voula (Yunanistan), hibrit — http://symposium.chigreece.gr/2026/
- **Events at CCF ChinaSoft 2026** — 6–8 Kas, Tianjin (Çin) — http://chinasoft.ccf.org.cn/2026/
- **RazorHack** (UALR ACM Öğrenci Bölümü) — 6–8 Kas, Fayetteville AR (ABD) — http://razorhack.org/
- **Computer Science Contest** (Princeton ACM Öğrenci Bölümü) — 7 Kas, Princeton NJ — http://princetonacm.github.io/
- **WISE 2026** (27th Intl. Conf. on Web Information Systems Engineering) — 2–5 Kas, Venedik (İtalya), hibrit — http://conferences.sigappfr.org/wise2026/
- **Fall 2026 ACM Banquet** (Cleveland State Univ.) — 6 Kas, Cleveland OH — http://csuohio.hosting.acm.org/

> Bu takvim çok geniş (yüzlerce bölüm etkinliği); yukarıdakiler 6–8 Kas dilimi. Tam liste sayfadaki günlük görünümde.

## 3) Call for Papers / Başvuru Deadlineleri

Kaynak: `https://www.acm.org/conferences/upcoming-submission-deadlines` (eventType=CallsForPapers, aylık görünüm). Ödül değil, **teklif/çalışma çağrısı** tarafı.

### Kasım 2026
| Deadline | Konferans | Link |
|---|---|---|
| 2 Kas | STOC '27 — 59th ACM Symposium on Theory of Computing | *(site henüz yayında değil — "not available yet")* |
| 15 Kas | PLDI '27 — ACM SIGPLAN Conf. on Programming Language Design and Implementation | https://pldi27.sigplan.org/ (henüz yayında değil) |
| 17 Kas | WSDM '27 — 20th ACM Intl. Conf. on Web Search and Data Mining | https://wsdm-conference.org/2027/ |
| 17 Kas | DAC '27 — 64th ACM/IEEE Design Automation Conference | http://www.dac.com/ |
| 23 Kas | IDC '27 — Interaction Design and Children | https://idc.acm.org/2027 |
| 26 Kas | ISCA '27 — 53rd Intl. Symposium on Computer Architecture | https://iscaconf.org/isca2027/ |

### Aralık 2026
| Deadline | Konferans | Link |
|---|---|---|
| 1 Ara | CODASPY '27 — 17th ACM Conf. on Data and Application Security and Privacy | https://www.codaspy.org/2027/ |
| 3 Ara | Middleware '27 — 28th Intl. Middleware Conference | https://middleware-conf.github.io/2027/ |
| 5 Ara | MobiSys '27 — 25th ACM Intl. Conf. on Mobile Systems, Applications and Services | https://www.sigmobile.org/mobisys/2027/ |
| 7 Ara | CODASPY '26 — 16th ACM Conf. on Data and Application Security and Privacy | https://codaspy.org/2026/ |
| 8 Ara | ICS '27 — 2027 Intl. Conference on Supercomputing | *(site "under construction")* |
| 15 Ara | WebSci '27 — 19th ACM Web Science Conference | https://websci27.webscience.org/ |

### Ocak 2027 (seçili, hacim yüksek)
| Deadline | Konferans | Link |
|---|---|---|
| 1 Oca | ICFP '27 / FCRC '27 / SOSP '27 / ETRA '27 / SPAA '27 / ASSETS '27 / DocEng '27 / EC '27 / MMSys '27 / CGO '27 / FOGA '27 / DigiPro '27 / SIGMIS-CPR '27 / PLMW@POPL '27 | (ayr ayrı; ör. SOSP https://sigops.org/s/conferences/sosp/, EC https://ec27.sigecom.org/) |
| 3 Oca | ACMSE 2027 — 2027 ACM Southeast Conference | https://acmse.net/2027/ |
| 4 Oca | SPLASH '27 — ACM SIGPLAN SPLASH | https://2027.splashcon.org/ |
| 8 Oca | I3D '27 — Symposium on Interactive 3D Graphics and Games | https://i3dsymposium.org/ |
| 11 Oca | SIGMETRICS '27 / ITiCSE '27 / DIS '27 | (ör. DIS https://dis.acm.org/2027/) |
| 14 Oca | FAccT '27 — ACM Conf. on Fairness, Accountability, and Transparency | https://facctconference.org/2027 |
| 15 Oca | ASIA CCS '27 / SW 27 (ACM Sustainability Week 2027) | (ör. https://asiaccs2027.cityu.edu.mo/) |
| 21–31 Oca | IMX '27 (21) / SIGDOC '27 (22) / CSCW '27 (24) / PEARC '27, C&C '27, GECCO '27 (25) / **SIGGRAPH '27** (28) / MobileHCI '27, ISSTA '27, UMAP '27 (29) / HPDC '27, **SIGCOMM '27** (31) | (ör. SIGGRAPH https://s2027.siggraph.org/, SIGCOMM https://www.sigcomm.org/events/sigcomm-conference) |

> Ocak 2027 "deadline" sayısı takvimde çok yüksek (14+ konferans 1 Ocak'ta). Bunlar CFP metinlerinde "submission deadline" olarak listelenen tarihler; tam liste sayfada.

## 4) Ödül Haberleri (awards.acm.org)

Kaynak: `https://awards.acm.org/` (Awards Home) + `https://www.acm.org/media-center` basın bültenleri.
**Önemli:** "Last 2 weeks" (23 Eki–6 Kas) içinde **tarihli resmi ödül duyurusu yok**. En taze olan 15 Ekim 2026 (Ken Kennedy).

### En taze (son ~3 hafta)
| Tarih | Ödül | Kazanan | Not |
|---|---|---|---|
| **15 Ekim 2026** | **2026 ACM-IEEE CS Ken Kennedy Award** | **Daniel Reed** (Univ. of Utah, emekli; eski Microsoft XCG lideri) | Paralel/yüksek performanslı hesaplama öncü katkıları. Basın bülteni: `acm.org/media-center/2026/october/kennedy-award-2026` |
| 9 Eylül 2026 | 2026 ACM-IEEE CS George Michael Memorial HPC Fellowship | **Jie Ren** (KAUST), **Amit Samanta** (Univ. of Utah), **Xuan Wu** (Oregon State); mansiyon: Yankai Jiang (Northeastern) | Tören **SC26**'da (15–20 Kas). Burs niteliği taşır. |
| 15 Eylül 2026 | (Basın bülteni) "AI Is Reshaping Open Source Software..." | — | TechBrief; ödül değil, açık kaynak+AI raporu |

### 2026 döngüsünde duyurulan ödüller (awards.acm.org "AWARDS & RECOGNITION" listesi; bunların bazılarının duyuru tarihi Eylül–Ekim 2026 arası)
| Ödül | Kazanan(ı) | Kısa özet |
|---|---|---|
| 2026 ACM-IEEE CS Eckert-Mauchly Award | **Srinivas Devadas** (MIT, Webster Prof.) | Güvenli mimariler / donanım güvenliği öncülüğü |
| ACM Doctoral Dissertation Award | **Allen Liu** (MIT) — "Learning Theoretic Foundations for Understanding Quantum Systems"; mansiyon: Gal Arnon (Weizmann), Rachit Nigam (Cornell) | Genç araştırmacı doktora tez ödülü |
| 2026–2027 ACM Athena Lecturer | **Monika Henzinger** (ISTA) | Dinamik grafik & web algoritmaları; mentorluk |
| ACM Paris Kanellakis Theory & Practice Award | **Erdal Arıkan** (Bilkent) | Kanal polarizasyonu / polar kodlar |
| ACM–AAAI Allen Newell Award | **Kevin Leyton-Brown** (UBC) | Çok-ajan sistemler, hesapsal ekonomi, oyun teorisi |
| ACM Grace Murray Hopper Award | **Ben Mildenhall** (World Labs) & **Pratul Srinivasan** (Google DeepMind) | Radyans alanı (NeRF) temsilleri, 3D jeneratif AI |
| ACM Karl V. Karlstrom Outstanding Educator Award | **Yasmin B. Kafai** (UPenn) & **Mitchel J. Resnick** (MIT) | Scratch, e-tekstileler, yaratıcı hesaplama eğitimi |
| ACM Policy Award | **Ed Felten** (Princeton) | Elektronik oy, telif, tüketici koruması, AI politikası |
| Outstanding Contribution to ACM Award | **Jodi Tims** (Northeastern, Center for Inclusive Computing) | ACM-W küresel genişlemesi, kadınların hesaplama katılımı |
| 2025 ACM Presidential Award | **Claudia Maria Bauzer Medeiros** (Univ. of Campinas) | (2025 dönemi, hâlâ listede) |

### 2025 büyük ödüller (liste üstte, ancak duyuruları 2025)
| Ödül | Kazanan(ı) |
|---|---|
| **2025 ACM A.M. Turing Award** | **Charles H. Bennett** (IBM Research) & **Gilles Brassard** (Univ. de Montréal) — Kuantum bilgi bilimi temelleri, BB84 |
| **2025 ACM Prize in Computing** | **Matei Zaharia** (UC Berkeley / Databricks CTO) — Dağıtık veri sistemleri (Spark) |

## 5) Program / Burs / Teklif (Apply) Haberleri

Kaynak: `https://www.acm.org/media-center/acm-updates` (tarihli günceller) + `https://www.acm.org/membership`.

| Tarih | Başlık | Tür | Detay |
|---|---|---|---|
| **5 Kas 2026** | "European Social Media Ban: Design, Practicality, and Consequences" — ACM Europe Tech Policy Committee webinar | **Etkinlik (webinar)** | **4 Aralık 2026**, 15:00 CET / 14:00 UTC. Çocuklar+sosyal medya kısıtlamaları (DSA). Zoom: `events.zoom.us/ev/AjkmqJxoxzddTodFzm2Fr2HCIm9H1PiD5xDmKp5EPQRe7ek5JvCW~...` |
| 2026, 2–4 Kas | **PQQS 2026** — Post-Quantum and Quantum-based Security | **Yeni konferans** | SIGSAC'ın ilk yeni yıllık konferansı; San Jose. Keynote: Charles Bennett, Renato Renner, Dan Boneh, Ryan Babbush. Site: https://acm-pqqs.github.io/pqqs2026/ |
| **31 Eki 2026 (AoE) — kapandı** | **2027 ACM Asian School on HPC and AI** (3. ACM Asya Okulu) | **Burs / başvuru** | 1–5 Mart 2027, Singapur (NSCC), SupercomputingAsia 2027 ile birlikte. Başvuru deadline'ı 31 Eki 2026 AoE — yeni kapandı. Site: https://europe.acm.org/seasonal-schools/asean/2027 |
| 25 Eki 2026 | ACM Transactions on Agentic AI (TAAI) — ilk Co-EiC'ler | **Yeni dergi** | Bang Liu (Univ. de Montréal) & Yan Liu (USC); dönem 1 Eki 2026–30 Eyl 2029. Dergi: https://dl.acm.org/journal/taai |
| 9 Eki 2026 | "Global Technology Policy at ACM" — USTPC, Europe TPC, Expanding Regions | **Etkinlik (webinar)** | 4 Kas 2026, 10:00 EDT — geçti |
| 30 Eyl 2026 | African Union Open Consultation on AI Governance — ACM Africa yanıtı | Politik | Afrikalı AI yönetişimi danışma sürecine katılım |
| 10 Eyl 2026 | TechBrief: "AI's Effects on Open Source" | Rapor | AI kod üretimi + açık kaynak güvenliği |
| 1 Eyl 2026 | Skills Bundle abonelerine tam O'Reilly kütüphanesi erişimi | Üyelik programı | Live Events, Interactive Sandboxes, O'Reilly Academies |
| (membership sayfası) | **ACM Student Research Competition** | **Program (öğrenci)** | Lisans/yüksek lisans araştırma yarışması. Site: http://src.acm.org/ |
| (membership sayfası) | Call for Proposals: ACM Books | Teklif | Kitap önerisi çağrısı. `acm.org/publications/call-for-proposals-acm-books` |

### Üyelik / yönetim (bağlam)
- **28 Tem 2026:** ACM, **Alison Derbenwick Miller**'ı CEO ve Executive Director olarak atadı (basın bülteni: `2026/july/acm-names-new-ceo-2026`).
- **30 Ağu 2026:** **Inaugural ACM AI Leadership Summit** duyuruldu (konuşmacılar arasında Turing ödüllü Yann LeCun, Andrew Barto).

## 6) Gezip kullanılan URL listesi

1. `https://www.acm.org/events` → **404** (sayfa yok; etkinlikler `conferences` altında)
2. `https://www.acm.org/` → ana sayfa (menü + son haberler)
3. `https://www.acm.org/conferences/conference-events` → aylık etkinlik takvimi
4. `https://www.acm.org/conferences/upcoming-submission-deadlines` (+ `?startDate0=20261201`, `?startDate0=20270101`) → CFP deadline takvimi
5. `https://awards.acm.org/` → Awards Home (son ödül listesi)
6. `https://awards.acm.org/kennedy`, `/about/2025-turing`, `/about/2025-acm-prize`, `/hpc-fellows`, `/eckert-mauchly`, `/doctoral-dissertation`, `/athena`, `/kanellakis` → birebir ödül sayfaları
7. `https://www.acm.org/media-center` → basın bültenleri (tarihli)
8. `https://www.acm.org/media-center/acm-updates` → tarihli günceller akışı
9. `https://www.acm.org/membership` → üyelik + program duyuruları
10. `https://acm-pqqs.github.io/pqqs2026/` → PQQS 2026 konferans sitesi
11. `https://www.acm.org/chapters/local-activities` → yerel/çevrimiçi etkinlik takvimi
12. `https://events.zoom.us/ev/...` (2 tanesi) → webinar Zoom sayfaları

## 7) Kısıtlılıklar / dürüstlük notları

- **"Son 2 hafta" penceresi dar:** 23 Eki–6 Kas 2026 arasında acm.org'da **tarihli resmi ödül duyurusu yok**. En taze ödül 15 Eki (Ken Kennedy). Ödül bölümü bu yüzden "son ~3 hafta" genişletildi ve 2026 döngüsü ödülleri tarihsiz olarak listelendi (birebir sayfalarda duyuru tarihi görünmüyor; medya merkezi tarihli bültenleri ile çapraz doğrulandı).
- **Carp deadline tarihleri:** Ocak 2027'de 14+ konferansın "1 Ocak" görünmesi, CFP takviminin bu ayda yoğun olduğu için; tam ve kesin tarihler birebir konferans sitelerinden teyit edilmeli. Bazı linkler henüz yayında değil ("not available yet", "under construction", "tba") — bu, ACM'nin kendi listelemesindeki hali.
- **Yerel etkinlikler:** Chapters Local Activities çok geniş bir günlük takvimdir; yukarıdakiler sadece 6–8 Kas diliminin örneği, tam liste sayfa içinde.
- **Cloudflare:** acm.org `curl` ile 403 verdiği için tüm veriler gerçek Chrome (CDP) üzerinden okundu; içerik coğrafi kişiselleştirme yapmadığından çıkış IP'si farklılığı sonuçları etkilemedi.
