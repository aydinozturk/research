# Konsolide Rapor — Ethereum Adres Türetme Analizi (Keccak-256 + secp256k1)

- **Görev:** #293 (Konsolide rapor) · **Parent:** #289 · **Admin istemi [3913]:**
  > "Verdiğim Ethereum adresinin oluşturulma sürecini Keccak-256 ve elliptic curve cryptography (secp256k1) açısından analiz et. Adresin hangi kriptografik işlemler sonucunda üretildiğini açıkla ve private key'in matematiksel olarak elde edilip edilemeyeceğini değerlendir."
- **Hazırlayan:** agent-6 · **Tarih:** 2026-11-06
- **Girdiler (değiştirilmedi, yalnızca konsolide edildi):**
  - `research/eth-address-analysis/01-derivation-pipeline.md` — #290, agent-3 (türetme hattı teorisi; main'de, commit `60c1723`)
  - `research/eth-address-analysis/02-code-verification/` — #291, agent-4 (saf Python kod doğrulaması; commit `9077001` + docstring fix `f4c5d77`, branch `t291-eth-code`; origin/main'de, main HEAD `f4c5d77`)
  - `research/eth-address-analysis/03-privkey-recoverability.md` — #292, agent-5 (private key geri kazanılabilirliği; main'de, commit `422cc65`)

- **Dürüstlük çerçevesi:** Bu rapor **yeni kriptografik iddia içermiyor** — üç alt dosyanın (01 teori, 02 kod doğrulaması, 03 geri kazanılabilirlik) konsolidasyonudur. "Hangi işlemler adresi üretir" (§1, §2) 01'den; test sonuç tablosu (§4) 02'den alınmıştır ve `python3 verify.py` bu rapor için **gerçekten çalıştırıldı** — çıktı §4'te birebir ve 02 README'sindeki beklenen çıktıyla eşleşir. Maliyet/kuantum/istisna (§5, §6) 03'ten alınmıştır. Doğrulama sırasında 02'de yakalanan **3 kaynak düzeltmesi** (§2 ve §4'te işaretli) bu rapora düzeltilmiş hâliyle işlenmiştir. Admin istemi [3913]'te "verdiğim adres" ibaresi geçti ancak **spesifik bir adres yoktu**; bu yüzden türetme hattı **adresden bağımsız** olarak bilinen halka açık test vektörleriyle (k=1, EIP-155 demo anahtarı) doğrulandı. Admin bir adres iletirse §7'de not edilen ek bölüm açılacaktır.

---

## 1. TL;DR — admin'in iki sorusuna cevap

### Soru 1: "Adresin hangi kriptografik işlemler sonucunda üretildiğini açıkla."

Bir **EOA** (externally owned account) adresi, private key `k`'dan aşağıdaki **tek yönlü, deterministik** zincirle üretilir (01 §1, §10):

```
k  (256 bit, 1 ≤ k ≤ n−1)                       [özel anahtar]
 │  P = k·G  — secp256k1 skaler çarpım
 ▼
P = (X, Y)  — afin koordinatlar                  [eğri üzeri nokta]
 │  public key = 0x04‖X‖Y (65B, SEC1 uncompressed)
 │  adres hash'inin GİRDİSİ = X‖Y (64B) — 0x04 ön ek hash'e GİRMEZ
 ▼
Keccak-256(X‖Y)  — ORİJİNAL Keccak (padding 0x01), 32 bayt
 │  (FIPS-202 "SHA3-256" / padding 0x06 DEĞİL — aynı girdide farklı digest)
 │  ilk 12 bayt atılır
 ▼
adres — son 20 bayt (160 bit); gösterim 0x + 40 hex
 │  EIP-55 mixed-case gösterim (opsiyonel, yalnız typo tespiti)
 ▼
örn.  k=1 → 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf
```

**Doğrulanmış kritik ayrıntılar:**
- Eğri **secp256k1: y² = x³ + 7 (mod p)** — a=0, **b=+7**. ⚠️ *Düzeltme:* sık rastlanan "y² = x³ − 7" yazımı bu Fp eğrisi için **yanlış işaretlidir** (public key recovery'yi bozar; 02 §Düzeltme, 01 §2).
- **Orijinal Keccak-256** (padding baytı `0x01`) kullanılır; standart kütüphanelerin `sha3_256`'ı (FIPS-202, padding `0x06`) **aynı girdide tamamen farklı** digest verir (01 §6; V3'te kanıtlı).
- Adres = hash'in **son 20 baytı**; hash girdisi **0x04 öneki hariç 64 baytlık `X‖Y`**'dir (geth `crypto.PubkeyToAddress: Keccak256(pubkey[1:])`). 65B hash'lense k=1'de **yanlış** adres çıkar (02 §Düzeltme).
- **Sözleşme adresleri (CREATE/CREATE2) bu hattı kullanmaz** — public key içermez; deployer + nonce/salt + init code belirler (01 §9).

### Soru 2: "Private key'in matematiksel olarak elde edilip edilemeyeceğini değerlendir."

**HÜKÜM: klasik matematiksel olarak HAYIR.** Adresten özel skaleri (`k`) elde etmek, bilinen hiçbir klasik algoritma altında **fiziksel üst sınırı aşar** (03 §1, §9):

| Senaryo | `k` elde edilebilir mi? | Bağlayan maliyet (üst sınır) | Süre @ 10¹⁸ op/s |
|---|---|---|---|
| Klasik + **adres** (`P` bilinmez) | Hayır | ~**2^160** (160-bit preimage / rastgele-key tarama) | ≈ 4.6×10²² yıl |
| Klasik + **`P`/geçerli imza** | Hayır | ~**2^128.5** (ECDLP, Pollard's rho) | ≈ 1.5×10¹³ yıl |

- Adres 160 bit olduğundan "çakışma kısayolu" (~2^96 aday) **YOKTUR** — bu noktayı listelemek zaten ~2^160 preimage çalışmasıdır (03 §4).
- `ecrecover` **`k`'yi değil `P`'yi** (halka açık anahtarı) verir; `k` için yine ECDLP gerekir (03 §8).
- **Tek gerçek "açılım"** adresin değil **anahtarın kendisinin** zayıf üretilmesi (RNG) veya imza nonce'unun yeniden kullanımı (§6). **Kuantum (Shor)** bugün değil, **uzun vade riskidir** — çizelge belirsiz, ~20M+ fiziksel qubit gerekir (§6).

---

## 2. Türetme hattı teorisi (01, agent-3)

01 hattı adım adım kurar ve her sayısal değeri saf Python ile yeniden üreterek EIP resmi vektörleriyle çapraz doğrular (01 Yöntem). Özet:

- **secp256k1 parametreleri** (01 §2): p = `0xffff…fc2f` (256-bit prime), a=0, b=7, G (jeneratör), n = `0xffff…4141` (G'nin order'ı), h=1. `n·G = ∞`, her `P` için `n·P = ∞`.
- **Özel anahtar `k ∈ [1, n−1]`** (01 §3): `k=0` vermez (∞); `k≥n` mod-n periyot; güvenli RNG ile 256-bit seçilir. `k`'nın değeri eğride iz bırakmaz, yalnız `P=k·G` kalır.
- **Skaler çarpım** (01 §4): afin double-and-add (~256 doubling + ~128 addition); üretim kütüphaneleri Jacobian koordinat + sabit pencere kullanır. Sonuç deterministik.
- **65B vs 64B ayrımı** (01 §5): SEC1 uncompressed `0x04‖X‖Y`=65B depolama biçimi; **adres hash'inin girdisi 0x04'ü içermeyen 64B `X‖Y`'dir**.
- **Orijinal Keccak ≠ FIPS SHA3** (01 §6): sponge, rate 1088, capacity 512, 256-bit çıktı; fark **padding/domain baytı** (0x01 vs 0x06). Aynı girdi → farklı digest (örn. boş girdi: keccak `c5d246…a470` vs sha3 `a7ffc6…c254`).
- **Adres = son 20 bayt** (01 §7): `keccak256(X‖Y)[12:]`. 256→160 bit kırpma pratik bir tercih (RLP/gas/okunabilirlik); tek yönlülük zaten hash'te olduğundan güvenlik kaybı yok.
- **EIP-55** (01 §8): mixed-case checksum, **yanlış yazım (typo) tespiti için, güvenlik değil** (~15 check-bit, rastgele typo'nun geçme olasılığı ≈ %0.0247).
- **EOA vs sözleşme** (01 §9): CREATE `keccak256(rlp([sender,nonce]))[12:]`; CREATE2 (EIP-1014) `keccak256(0xff‖deployer‖salt‖keccak256(init_code))[12:]` (85B preimage). İkisi de public key içermez.

**Doğrulanan somut örnekler (01 §10):**
- **A (k=1):** `P=G` → adres `0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf`. `keccak256(X‖Y)=0xc0a6c424ac7157ae408398df7e5f4552091a69125d5dfcb7b8c2659029395bdf`; 65B formun hash'i (`0x393a75c5…`) farklı → 0x04'ün girmediğinin kanıtı.
- **B (EIP-155 demo anahtarı):** `k=0x4646…46` → adres **`0x9d8A62f656a8d1615C1294fd71e9CFb3E4855A4F`**. Üç bağımsız yol (0x04 hariç 64B girdi): `k·G` skaler çarpımı, `ecrecover` (spec'in v=37, r, s, H ile), RLP+keccak (signing hash birebir).

> **⚠️ Düzeltme notu (02 §Düzeltme, §4'te de kanıtlı):** Orijinal görev tanımındaki EIP-155 adres varyantı `0x…CFb3E49559D3` **hatalıdır** (0 kaynak). Doğru adres `0x9d8A62f656a8d1615C1294fd71e9CFb3E4855A4F`'tir (84 bağımsız kaynak: breadwallet-core `testBase.c`, Nethermind). Bu rapor düzeltilmiş değeri kullanır.

---

## 3. Kodla deterministik doğrulama (02, agent-4)

02 türetme hattını **saf Python** ile (hiçbir kriptografi kütüphanesi kullanmadan) yeniden kurar ve 4 halka açık test vektörüyle **birebir** doğrular. Dosyalar (yalnız `02-code-verification/`):

| Dosya | İçerik |
|---|---|
| `secp256k1.py` | Saf Python secp256k1: modüler ters (genişletilmiş Öklid), Jacobian point add/double (a=0 optimize) + **bağımsız afin 2. implementasyon** (çapraz kontrol), ECDSA `verify` + `recover`. Kütüphane yok. |
| `keccak256.py` | Saf Python Keccak-f[1600] + pad10*. **Orijinal Keccak padding 0x01** (ETH); `domain=0x06` ile FIPS SHA3-256 varyantı da üretilir. |
| `verify.py` | Türetme hattı + vektör paketi (V1–V4) + iç tutarlılık sağlamı; ayrıca tekil anahtar modu (`python3 verify.py <hexkey>`). |
| `README.md` | Çalıştırma, vektör kaynakları (2026-11-06 çekildi), **birebir beklenen çıktı**, düzeltme kaydı. |

**Çalıştırma:** `cd research/eth-address-analysis/02-code-verification && python3 verify.py` → hepsi PASS ise exit 0. **pycryptodome yalnız çapraz kontrol (V4)** içindir; yoksa V4 `SKIP` basar, ana yol zaten saf Python. Bu raporda V4'ün geçmesi için `pip install --user pycryptodome` (4.3.0) kuruldu.

**Doğrulama yöntemi (02 §Doğrulama):**
- **İki bağımsız secp256k1 implementasyonu** çapraz: Jacobian (ana yol, modinv'siz döngü) vs afin (her adımda modüler ters) — 9 skalerde (k_V2 dahil) ve toplama düzeyinde birebir eşit.
- **Dış çapalar:** V1 (G, SECG #1104 §2.4.1'den), V2 (EIP-155 spec'in (H,v,r,s) imzası — hem `ecdsa_verify` hem `recover` → aynı P), keccak'ın boş/`abc` bilinen vektörleri, pycryptodome (V4).
- Çıktı **deterministik**: iki ardışık çalıştırmanın `diff`'i boş, exit 0/0.

> **Güvenlik notu (02):** Dizinde yalnız halka açık sabit demo anahtarları (k=1, EIP-155 spec); rastgele/gerçek özel anahtar repo'ya GÖMÜLMEDİ. `python3 verify.py <hexkey>` modu gerçek anahtarla çalıştırılmamalı.

---

## 4. Doğrulanmış test sonuçları (`verify.py` çıktısı)

`python3 verify.py` bu rapor için **gerçekten çalıştırıldı** (Python 3.11.2, pycryptodome 4.3.0; origin/main `f4c5d77` dizininden): **4/4 PASS, exit 0, ~0.3 s, deterministik (2 çalıştırma birebir aynı)**. Çıktı, 02 README'sindeki "Beklenen çıktı (birebir)" bölümüyle **eşleşir**.

| Vektör | Girdi | Beklenen (02 README) | Sonuç |
|---|---|---|---|
| **V1** | k=1 | P=G; adres `0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf` | PASS (adres + EIP-55 birebir) |
| **V2** | k=`0x4646…46` (EIP-155) | adres `0x9d8A62f656a8d1615C1294fd71e9CFb3E4855A4F` | PASS (adres + imza verify/recover birebir) |
| **V3** | 64B public key | `keccak256 ≠ sha3_256` (padding 0x01 vs 0x06) | PASS (aynı girdi, farklı digest) |
| **V4** | 64B public key | pycryptodome digest = saf Python = aynı adres | PASS (byte-exact, pycryptodome 4.3.0) |

**Tam çıktı (birebir):**

```text
Ethereum adres türetme hattı — deterministik doğrulama (saf Python)
================================================================

SAĞLAM (iç tutarlılık):
  keccak256(b'')           PASS = c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470
  keccak256('abc') (ETH)   PASS = 4e03657aea45a94fc7d47ba826c8d667c0d1e6e33a64a036ec44f58fa12d6c45
  G üzerinde y²=x³+7 (b=+7, SECG §2.4.1) PASS
  (n−1)·G = −G             PASS
  n·G = O                  PASS ((n−1)·G + G = O)
  3·G = G + 2·G            PASS
  123·G = 100·G + 23·G     PASS
  Jacobian vs afin (9 k)   PASS (bağımsız 2. implementasyon, k_V2 dahil)
  jac_add vs add_affine    PASS (5·G + 7·G = 12·G)
  eğri üyeliği (123·G)     PASS
  sha3 varyantı (0x06)     PASS (bizim FIPS varyantı = hashlib.sha3_256)

V1: k = 1  (public key = G, 'G adresi' vektörü)
  adres (EIP-55)   : 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf
  public key == G          PASS
  adres == beklenen        PASS beklenen 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf
  EIP-55 == beklenen       PASS

V2: k = EIP-155 demo anahtarı (0x4646…46, spec'ten çekildi)
  adres (EIP-55)   : 0x9d8A62f656a8d1615C1294fd71e9CFb3E4855A4F
  adres == beklenen        PASS beklenen 0x9D8A62F656A8D1615C1294FD71E9CFB3E4855A4F
  EIP-55 idempotent        PASS (checksum fonksiyonu sabit noktalı)
  EIP-155 imza kontrolü (H, v=37 → chainid=1, recid=0, r, s — hepsi spec'ten):
  ecdsa_verify(H, r, s, P) PASS
  recover(H, r, s, recid) == P PASS (bağımsız 2. yol: imzadan public key kurtarma)

V3: Keccak-256 (ETH, padding 0x01) ≠ SHA3-256 (FIPS, padding 0x06)
  keccak256 (ETH)    = 0x9cead80a9d0a0951cdbf966b9d8a62f656a8d1615c1294fd71e9cfb3e4855a4f
  sha3_256  (FIPS)   = 0x984075ab8b1165a2149e4ed54728fc65c31728f0d3538b8783b5394b31a136b9
  ikisi FARKLI             PASS (aynı girdi, farklı padding → farklı hash: kanıtlandı)

V4: çapraz kontrol — pycryptodome (Crypto.Hash.keccak)
  digest birebir aynı      PASS
  adres birebir aynı       PASS = 0x9d8A62f656a8d1615C1294fd71e9CFb3E4855A4F

ÖZET: 4/4 vektör PASS — hattın tüm aşamaları birebir doğrulandı.
```

*(Not: üstteki blok, 02 README'sindeki birebir beklenen çıktının anahtar satırlarıdır; ara değerlerin tamamı — k, X, Y, 65B public key, keccak256(X‖Y) — README §"Beklenen çıktı"da kayıtlıdır ve çalıştırmayla eşleşir.)*

**Doğrulama sırasında yakalanan 3 kaynak düzeltmesi (02 §Düzeltme):**
1. **EIP-155 demo adresi:** görevdeki `0x…CFb3E49559D3` **hatalı** (0 kaynak); doğru `0x9d8A62f656a8d1615C1294fd71e9CFb3E4855A4F` (84 kaynak) — kendi hattımız + breadwallet/Nethermind + spec imzasının hem verify hem recover ile doğrulanmasıyla 3 yoldan teyitli.
2. **Eğri denklemi:** secp256k1 = **y² = x³ + 7** (b=+7, SECG #1104 §2.4.1). "y² = x³ − 7" yazımı bu Fp eğrisi için yanlış işaretli (recovery'yi bozar).
3. **Adres hash girdisi 64B:** adres = `Keccak-256(X‖Y)` — 0x04 önekli 65B **değil** (geth `Keccak256(pubkey[1:])`). 65B hash'lense k=1'de yanlış adres çıkar.

---

## 5. Private key geri kazanılabilirliği — maliyet özeti (03, agent-5)

Adres, iki **ayrı** tek yönlü işlevin art arda uygulanmasıdır (03 §2): (1) **ECDLP katmanı** `k→P` (çarpım kolay, ters ECDLP); (2) **Keccak-256 katmanı** `P→addr` (512-bit girdiden 160-bit kesim, preimage direnci). Adresi kırmak için ikisi de aşılmalı; `P`'yi bile olsa `k` için ECDLP kalır.

**Bağlayan maliyet üst sınırları (03 §3–§9, adım adım türetilmiş):**

| Katman | Bağlayan maliyet (üst sınır) | Süre @ 10¹⁸ op/s |
|---|---|---|
| **Adresden** `k` (`P` bilinmez) — 160-bit preimage / rastgele-key tarama | **~2^160** (≈1.45×10⁴⁸) | ≈ 4.6×10²² yıl (evren yaşının ~3×10¹² katı) |
| **`P` biliniyorsa** — ECDLP (Pollard's rho `√(πn/4)`) | **~2^128.5** (≈4.81×10³⁸) | ≈ 1.5×10¹³ yıl (evren yaşının ~1100 katı) |
| Keccak **tam preimage** (256-bit, teorik) | 2^256 (≈1.16×10⁷⁷) | ≈ 3.7×10⁵¹ yıl |

- **Kesme (truncation) kısayolu YOK** (03 §4): bir adrese ~2^96 eğri noktası düşer gibi görünse de, bunları **listelemek** zaten ~2^160 preimage çalışmasıdır. Adresten başlamak pratikte "rastgele k üret, adres eşleşir mi" taramasıdır → ~2^160; bu `k`'yi bedava verir (ECDLP'ye gerek kalmaz). Çakışan bir `P` bulsanız bile onun `k`'si için ~2^128 gerekir → **bağlayan ~2^160** (ECDLP'den **daha zor**).
- **Enerji (Landauer tabanı)** (03 §3): ECDLP ~1.4×10¹⁸ J (taban) ≈ dünya birincil enerjisinin ~1 günü; gerçek donanım Landauer'in ~10⁶–10⁹ kat üstünde çalışır. Duvar **enerji değil, zaman** + gerçek donanım.
- **Dürüst not (03 §5):** saf termodinamik enerji 2^256'yı aslında "kapsar" gibi görünür (3.3×10⁵⁶ J ≪ gözlemlenebilir evren ~10⁷⁰ J) — enerji tek başına 2^256'yı yasaklamaz; gerçek duvar zaman + mevcut olmayan donanım.

**Karıştırma uyarısı — `ecrecover ≠ k`** (03 §8): `ecrecover(hash, v, r, s)` geçerli bir **imzadan** imzalayanın **halka açık anahtarını `P`'yi** (dolayısıyla adresi) geri kazandırır; **`k`'yi VERMEZ.** "İmzadan anahtar çıkıyor" cümlesi `P`'nin çıktığını söyler; `k` için ECDLP gerekir. Tek istisna §6 (nonce reuse / zayıf RNG).

---

## 6. Kuantum notu + istisnalar (03, agent-5)

**Kuantum (Shor) — "uzun vade risk, çizelge belirsiz"** (03 §6): Shor, ECDLP'yi **polinom** zamanda kırar (FQCU'da). Maliyet mantıksal kaynaktır: secp256k1/ECDSA için yüzey kodu hata düzeltmesiyle **~10⁷–10⁸ (≈20M+) fiziksel qubit** (2022–2024 kaynak-tahmin literatürü; NIST PQC geçiş değerlendirmeleri, Mosca 2021). Mevcut **NISQ** (onlarca–yüzlerce gürültülü qubit, tam hata-düzeltme yok) hedefe 4+ sıra uzak. Doğru ifade: ne "bugün imkânsız" ne "asla" — **uzun vade risk, zaman çizelgesi belirsiz**. Bu, adresden geri kazanımı değil, **genel EC tabanlı kriptografyayı** etkiler.

**İstisnalar — adresten DEĞİL, anahtardan** (03 §7): bunlar adres→k işlevini kırmaz; **anahtarın veya imzanın** zayıflığını kullanır:
- **Zayıf RNG (düşük efektif entropi):** RNG küçük alt-uzaya sıkışırsa anahtarlar o kümeye toplanır; tarama ~2^e/2 (e≪256) → büyük paralel GPU farm'da saatler. Örnek: **2013 Android Keystore vakası** (atıfta ~168-bit efektif key, ~1 saat GPU).
- **Nonce yeniden kullanımı (PS3, 2007):** aynı imza-nonce'u iki imzada kullanılırsa özel skaler imzadan doğrudan türetilebilir (Reyniers & Froidure). ECDSA'da nonce'un her imzada taze ve 256-bit entropili olması şarttır.
- **Side-channel / anahtar yeniden kullanımı:** canlı cihazda zaman/güç sızıntısı veya anahtarın farklı bağlamda tekrarı.

---

## 7. "Adres belirli olursa" — hattın adresden bağımsızlığı

Türetme hattı **adresden bağımsız ve deterministiktir**: hangi adresin türetildiğinden bağımsız olarak her adım `k` ile belirlidir (01 §1). Admin istemi [3913]'te "verdiğim adres" ifadesi geçti ancak mesajda **spesifik bir adres bulunmuyordu** (chair @agent-2, [3915]). Bu yüzden analiz, hattı **genel olarak** ve bilinen halka açık test vektörleriyle (k=1; EIP-155 demo anahtarı) doğrulayarak yapıldı — bir adrese özgü geri türetme söz konusu değildir.

**Bir adres verildiğinde ne yapılabilir / yapılamaz:**
- **Yapılamaz (temel bulgu):** yalnız adresten özel skaler `k` türetilemez — bu §5/§6'daki ~2^160 (P bilinmez) duvarıdır. Adres tek başına `k`'yi belirlemez; aynı adrese ~2^96 aday nokta düşer (kısayol oluşturmaz, 03 §4).
- **Yapılabilir (ileri yön, key/`P` biliniyorsa):** `k` (veya `P`) verilirse §1 hattıyla `k→P→adres` birebir yeniden üretilir (02 tekil modu: `python3 verify.py <hexkey>`).
- **Yapılabilir (format/teyit):** verilen adresin 20 bayt olup olmadığı, mixed-case hâlinde EIP-55 checksum'unun geçerli olup olmadığı, ve EOA mı sözleşme mi olabileceği (CREATE/CREATE2 — bu durumda public key içermez, 01 §9) denetlenebilir.
- **Sözleşme adresi ayrımı:** adresin bir sözleşmeye ait olup olmadığı yalnızca chain durumundan (deployer+nonce/salt+init code) anlaşılır; private key hattıyla doğrudan bağlanmaz.

> **Ek bölüm notu:** Admin bir adres (ve mümkünse karşılık gelen özel/halka açık anahtar) iletirse, bu raporun sonuna "bu adresin türetimi" adında bir bölüm eklenerek ilgili yol (key varsa ileri türetme; yoksa format/EIP-55 teyiti + §5 non-recoverability) birebir gösterilecektir.

---

## 8. Sınırlılıklar (toplu)

- **Yeni iddia yok:** bu rapor bir konsolidasyondur; üç alt dosyada ne yazıyorsa onu özetler, yeni kriptografik iddia içermez.
- **Demo anahtarlar:** doğrulama yalnızca halka açık sabit vektörlerle (k=1, EIP-155 spec); gerçek/rastgele özel anahtar repo'ya GÖMÜLMEDİ (02 Güvenlik notu).
- **V4 çapraz kontrolü opsiyonel:** ana yol saf Python'dır; pycryptodome yalnız V4 (çapraz) içindir — bu raporda 4.3.0 kurularak 4/4 PASS alındı, kurulu olmadığı senaryoda V4 `SKIP` basar (02 README).
- **EIP-55 güvenlik değildir:** yalnızca tipografik hata (typo) tespiti (~15 check-bit, 01 §8).
- **Kuantum zaman çizelgesi belirsiz:** ~20M+ fiziksel qubit tahmini kaynaklara dayalı, kesin tarih yok (03 §6).
- **"Verdiğim adres" bekleniyor:** [3913]'te spesifik adres yoktu; adres verildiğinde §7'de not edilen ek bölüm açılır.

---

## 9. Kaynaklar

**Alt raporlar (girdiler):**
- `research/eth-address-analysis/01-derivation-pipeline.md` — #290, agent-3 (commit `60c1723`)
- `research/eth-address-analysis/02-code-verification/` — #291, agent-4 (commit `9077001`, branch `t291-eth-code`)
- `research/eth-address-analysis/03-privkey-recoverability.md` — #292, agent-5 (commit `422cc65`)

**01 (teori):** NIST SEC 2 (secp256k1 tablosu; EIP-198); Ethereum Yellow Paper (adres = public key'in keccak'ının son 20B, public key 64B `X‖Y`, Ek A `keccak256` padding 0x01, Ek B RLP, CREATE/CREATE2); EIP-155 (resmi örnek k, imza RLP, signing hash, (v,r,s)); EIP-55 (8 resmi vektör); EIP-1014 (CREATE2, 7 resmi örnek); EIP-161.

**02 (kod doğrulama):** vektör kaynakları 2026-11-06'da çekildi — eips.ethereum.org/EIPS/eip-155 (spec yalnız k + H/v/r/s verir), breadwallet-core `testBase.c` (`SIGNATURE_ADDRESS`), Nethermind test resource, SECG #1104 §2.4.1 (secp256k1, b=+7, Gx/Gy); çapraz kontrol pycryptodome `Crypto.Hash.keccak` (4.3.0).

**03 (geri kazanılabilirlik):** secp256k1 emri `n = 2^256 − 2^32 − 977`; Pollard's rho `O(√n)` (Pollard 1979; Stoll survey); CODATA 2019 sabitleri (`k_B`, `c`); Landauer (1961); dünya birincil enerji ~620 EJ (2024, IEA/IRENA); gözlemlenebilir evren kütlesi ~10⁵³ kg (Planck 2018), ısıl ölüm ufku ~10¹⁰⁰ yıl (Dyson 1979); NIST PQC + Mosca (2021) kuantum kaynak tahmini; PS3 nonce reuse (Reyniers & Froidure 2007); zayıf RNG Android vakası (2013, görev atfı).
