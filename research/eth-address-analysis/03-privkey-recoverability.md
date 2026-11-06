# Private key geri kazanılabilirliği — adresten k türetilebilir mi?

**Görev:** #292 · **Bağ:** parent #289 · **Hazırlayan:** agent-5 · **Tarih:** 2026-11-06
**Yöntem:** Sayısal üst sınırlar. Her rakam ya bu dokümanda adım adım türetilir ya kaynak notuyla verilir.
**Dil ilkesi:** Abartısız. "İmkânsız" yerine *"bilinen hiçbir algoritma altında fiziksel üst sınırı aşıyor."*

## 0) Hat ve notasyon

- `P = k·G` — secp256k1'de `G` jeneratör, `k` **özel skaler** (private key), `P=(X,Y)` halka açık nokta.
- Adres: `addr = keccak256(X‖Y)[12:32]` — 512-bitlik `X‖Y`'nin Keccak-256 çıktısının **son 20 baytı (160 bit)**.
- ECDSA nonce'u literatürde de `k` ile gösterilir; burada özel skaler `k`, imza nonce'u "nonce" diye ayrılır.
- Sabitler: `1 yıl = 3.156×10^7 s`; `k_B = 1.380649×10^-23 J/K` (CODATA 2019); `c² = 9×10^16 m²/s²`.

## 1) TL;DR

Ethereum adresinden özel skaleri elde etmek **klasik dünyada, bilinen hiçbir algoritma altında
fiziksel üst sınırı aşan** bir işlemdir:

- Adresden başlanırsa en iyi bilinen saldırı ~2^160 işlemdir (≈4.6×10^22 yıl, 10^18 op/s varsayımıyla).
- Halka açık nokta `P` zaten biliniyorsa ECDLP ~2^128.5 (≈1.5×10^13 yıl).
- İkisi de bugün ve öngörülebilir gelecekte pratikleşemez.
- Tek gerçek "açılım" adresin değil **anahtarın kendisinin** zayıf üretilmesi (RNG) veya imza nonce'unun yeniden kullanımıdır.

## 2) Hattın iki yönsüz işlevi

Adres iki bağımsız tek yönlü (one-way) işlevin art arda uygulanmasıdır:

1. **ECDLP katmanı** `k → P`: çarpım (skaler × jeneratör) çok kolaydır; tersine `P → k` eliptik eğri ayrık logaritma (ECDLP) ister.
2. **Keccak-256 katmanı** `P → addr`: 512-bit girdiden 160-bit kesilmiş adres; preimage direnci kriptografik maliyet.

İkisi **ayrı ayrı** zor; adresi kırmak için ikisini de aşmak gerekir.
`P`'yi bile olsa `k` için ECDLP kalır — yani Keccak'ı "geçseniz bile" iş bitmez.

## 3) ECDLP maliyeti (`P` biliniyorsa) — adım adım

secp256k1 emri `n ≈ 2^256` (doğrusu `2^256 − 2^32 − 977`; `log2(n) ≈ 256`).
En iyi klasik algoritma **Pollard's rho**:

- Adım 1 — beklenen işlem: `√(πn/4) ≈ 0.886·2^128 ≈ 2^127.8` EC işlemi.
- Adım 2 — gönüllü yuvarlak üst sınır: **2^128.5 ≈ 4.81×10^38** işlem (`2^128 ≈ 3.40×10^38`).
- Adım 3 — süre @ 10^18 op/s ("rüzgar değinen" varsayım): `4.81×10^38 / 10^18 = 4.81×10^20 s`.
- Adım 4 — yıla çevir: `4.81×10^20 s / 3.156×10^7 ≈ 1.52×10^13 yıl`.
- Adım 5 — kıyas: evren yaşı `1.38×10^10 yıl` → **~1100 katı.**

Enerji (Landauer tabanı):

- Adım 1 — tek işlemde silinen 1 bit için `E = k_B·T·ln2`, `T = 300 K` → `E ≈ 2.87×10^-21 J/işlem`.
- Adım 2 — toplam: `4.81×10^38 × 2.87×10^-21 ≈ 1.38×10^18 J`.
- Adım 3 — kıyas: dünya birincil enerjisi ~620 EJ = 6.2×10^20 J/yıl (IEA/IRENA 2024) → taban enerji ~**1 gün**.
- Sonuç: enerji tek başına duvar değil; duvar **zaman** + gerçek donanımın Landauer'in ~10^6–10^9 kat üstünde işlemesi (gerçek enerji ~10^24–10^27 J ≈ 10^4–10^7 yıl dünya enerjisi).

## 4) Kesme (truncation) etkisi — shortcut YOK

Adres 160 bit; ~2^256 geçerli eğri noktasından **adres başına ~2^(256−160) = 2^96** tane `X`/`P` aynı adrese düşer. İlk bakışta "yalnızca 2^96 aday" gibi görünse de bu **kısayol değildir:**

- Bir adrese çakışan bu 2^96 noktayı **listelemek zaten** 160-bit preimage çalışmasıdır (≈2^160).
- Adresten başlamak için pratik yol: rastgele `k` üret, `P'=k·G`, `keccak256(P')[12:32]` hedefle eşleşir mi kontrol et.
  160-bit eşleşme → beklenen **2^160 deneme**; ve bu `k'`'yi **bedava verir** (ECDLP'e gerek kalmaz).
- Çakışan bir `P'` bulsanız bile, onun `k'`'si için ECDLP (~2^128) gerekir; bu 2^160'ın altında → **bağlayan maliyet ~2^160**.
- 2^160 işleme zaman: `1.45×10^48 / 10^18 = 1.45×10^30 s ≈ 4.6×10^22 yıl` (evren yaşının ~3×10^12 katı).
- 2^160 işleme enerji (Landauer tabanı): `≈4.2×10^27 J` (gerçek donanımda dünya enerjisinin 10^12+ yılı).

**Özet:** Kesme, adresden `k` bulmayı *daha kolay* kılmaz; ECDLP'den (2^128) **daha zor** (~2^160) kılar, çünkü adresden `P` bilinmez.

## 5) Keccak tam preimage (2^256)

Eğer biri 512-bit girdinin **tam** 256-bit Keccak preimage'ını ararsa:

- Adım 1 — işlem: `2^256 ≈ 1.16×10^77`.
- Adım 2 — enerji (Landauer tabanı): `1.16×10^77 × 2.87×10^-21 ≈ 3.3×10^56 J`.
- Adım 3 — gözlemlenebilir evren enerjisi: kütlesi ~10^53 kg → `E = mc² ≈ 9×10^69 ≈ 10^70 J`
  (Kardashev Type-III / "Dyson sınırı" bağlamında anılan büyüklük).
- **Dürüst not:** `3.3×10^56 J ≪ 10^70 J` — saf *termodinamik* enerji 2^256'ı aslında "kapsar" görür; enerji tek başına 2^256'ı yasaklamaz.
- Gerçek duvar (a) gerçek donanım Landauer'in 10^6–10^9 kat üstünde → gerçek enerji 10^62–10^65 J, evrenin kütlesel enerjisinin önemli bir payı;
  (b) **zaman**: 10^18 op/s'de `1.16×10^77/10^18 = 1.16×10^59 s ≈ 3.7×10^51 yıl`.
- Evrenin ısıl ölüm ufku ~10^100 yıl (Dyson 1979); bu yalnızca Landauer mertebesinde verim varsayımıyla anlamlıdır.
  10^18 op/s'yi sürdürebilecek donanım fizikte mevcut değil.

## 6) Kuantum (Shor) — "uzun vade risk, çizelge belirsiz"

Shor algoritması ECDLP'yi **polinom** zamanda kırar. Maliyet mantıksal kaynaktır:

- Mantıksal qubit: `O(n)`, n=256 için birkaç bin (tipik 4–8 bin).
- Fiziksel qubit: yüzey kodu (surface code) hata düzeltmesi, gereken güvenliğe ~10^3–10^4 fiziksel qubit/mantıksal → secp256k1/ECDSA için 2022-2024 kaynak tahminlerinde sıkça anılan **~10^7–10^8 (≈20 milyon+) fiziksel qubit**.
- Çapa kaynak: NIST PQC geçiş değerlendirmeleri ve kuantum kaynak-tahmin literatürü (`csrc.nist.gov/Projects/post-quantum-cryptography`); Mosca 2021 zaman-modeli bu ölçeğe işaret eder.
- Mevcut durum: **NISQ** (onlarca–yüzlerce gürültülü qubit, tam hata-düzeltme yok) — hedefe 4+ sıra uzak.
- Hüküm: "bugün imkânsız" **veya** "asla" demeyin. Doğrusu: **uzun vade risk, zaman çizelgesi belirsiz.**
- Bu, adres geri kazanımı değil, **genel EC tabanlı kriptografyayı** etkiler (NIST PQC geçişinin bir parçası).

## 7) İstisnalar — adresten DEĞİL, anahtardan

Bunlar adres→k işlevini kırmaz; **anahtarın veya imzanın** zayıflığını kullanır:

- **Zayıf RNG (düşük efektif entropi):** RNG küçük bir alt-uzaya sıkışırsa anahtarlar o uzaya düşer.
  Ör. **2013 Android Keystore vakası** (görevde atıf: ~168-bit efektif key, ~1 saat GPU; kaynak: GitHub advisory / basın).
  Mekanizma: `k`'nin gerçek entropisi 256 yerine e≪256 bitse tarama ~2^e/2 işlem olur; büyük paralel GPU farm'da saat mertebesinde.
  (Dürüst not: "168-bit → 1 saat" atıftaki sayıdır; sağlam kısım mekanizmadır — bozuk RNG'li cihazda anahtar, brute-force'lanabilir küçük bir kümeye toplanır.)
- **Nonce yeniden kullanımı (PS3, 2007):** Aynı imza-nonce'u iki imzada kullanılırsa özel skaler imzadan doğrudan türetilebilir (Reyniers & Froidure, "How to break (some of) the signed content on PS3").
  ECDSA'da nonce'un her imzada taze ve 256-bit entropili olması şarttır.
- **Side-channel / anahtar yeniden kullanımı:** canlı cihazda zaman/güç sızıntısı veya anahtarın farklı bağlamda tekrar kullanımı.

## 8) Karıştırma uyarısı — ecrecover ≠ k

Ethereum `ecrecover(hash, v, r, s)` **geçerli bir İMZADAN** imzalayanın **halka açık anahtarı `P`'yi**
(dolayısıyla adresi) geri kazandırır — **`k`'yi VERMEZ.**

- Bu standart bir ECDSA "public-key recovery"üdür; imzayı üreten zaten `P`'yi (dolayısıyla `k`'yi) biliyordu.
- Karışıklık: "imzadan anahtar çıkıyor" cümlesi `P`'nin çıktığını söyler; `k` için yine ECDLP (~2^128) gerekir.
- **Tek istisna:** nonce yeniden kullanımı / zayıf RNG (§7).

## 9) Son hüküm tablosu

| Senaryo | `k` elde edilebilir mi? | Bağlayan maliyet (üst sınır) | Süre @ 10^18 op/s |
|---|---|---|---|
| Klasik + **adres** (P bilinmez) | Hayır (bilinen algoritmada) | ~2^160 (160-bit preimage / rastgele-key tarama) | ≈ 4.6×10^22 yıl |
| Klasik + **P / geçerli imza** (ecrecover'den P) | Hayır | ~2^128.5 (ECDLP/Pollard rho) | ≈ 1.5×10^13 yıl |
| Kuantum + adres (Shor, ~20M+ fiziksel qubit, tam hata-düzeltme) | Uzun vade evet | polinom zaman (FQCU'da) | bugün uygulanamaz; çizelge belirsiz |
| Zayıf RNG / nonce reuse (anahtar üretimi) | **Evet** | ~2^e/2, e≪256 | saatler (ör. ~1 saat GPU) |

**Net hüküm:** Sadece adresten özel skaleri elde etmek, klasik dünyada bilinen hiçbir algoritma altında
fiziksel üst sınırı aşıyor (~2^160; `P` biliniyorsa bile ~2^128). Güvenlik, adresin kendisinden değil;
(a) şifrelemenin (ECDLP+Keccak) tek yönlülüğünden, (b) anahtarın **güçlü bir RNG** ile üretilmesinden
ve (c) imza nonce'unun taze tutulmasından gelir. Kuantum (Shor), adresden geri kazanımı değil,
**genel EC tabanlı kriptografyayı** uzun vadede risk altına alır.

## Kaynaklar

- secp256k1 parametreleri: SEC 2 / NIST (emir `n = 2^256 − 2^32 − 977`).
- Pollard's rho `O(√n)`: Pollard (1979); Stoll, "The Discrete Logarithm Problem" (survey).
- Sabitler: CODATA 2019 (`k_B = 1.380649×10^-23 J/K`, `c = 299792458 m/s`); Landauer (1961).
- Dünya birincil enerji ~620 EJ (2024): IEA / IRENA / BP Statistical Review of World Energy.
- Gözlemlenebilir evren kütlesi ~10^53 kg: Planck (2018) kozmoloji; ısıl ölüm ufku ~10^100 yıl: Dyson (1979) "Time without End."
- Kuantum kaynak tahmini (~10^7–10^8 fiziksel qubit, secp256k1): NIST PQC (`csrc.nist.gov/Projects/post-quantum-cryptography`); Mosca (2021) "A time-dependent model for post-quantum security"; 2022-2024 kaynak-tahmin literatürü.
- PS3 nonce reuse: Reyniers & Froidure (2007) "How to break (some of) the signed content on PlayStation 3."
- Zayıf RNG (Android): görev atfı (2013, GitHub advisory / basın); mekanizma §7'de ayrıntılı.
