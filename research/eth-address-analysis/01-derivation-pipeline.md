# Ethereum Adres Türetme Hattı — Teori (secp256k1 + Keccak-256)

Görev: #290 (plan #289'ün alt görevi)
Tarih: 2026-11-06
Hazırlayan: agent-3

**Yöntem:** Bu dosyadaki tüm sayısal değerler bu makinede saf Python ile yeniden üretildi
(afin double-and-add nokta çarpımı + pycryptodome keccak) ve EIP resmi vektörleriyle çapraz doğrulandı:
- **EIP-155:** imza verisi RLP'si sıfırdan yeniden üretildi (birebir eşleşme), signing hash birebir,
  EIP'nin verdiği (v, r, s) imzasından `ecrecover` ile public key türetildi ve `k·G` sonucuyla eşleşti.
- **EIP-55:** 8 resmi test vektörünün tamamı birebir (mixed-case dahil).
- **EIP-1014 (CREATE2):** 7 resmi örneğin tamamı birebir (mixed-case dahil).

Kapsam: private key → adres hattının teorisi. "Adresten private key geri kazanılabilir mi?"
sorusu #292'de, kod detayları #291'de ele alınır.

## TL;DR

- Adres, private key `k`'dan şu tek yönlü zincirle üretilir:
  `k → P = k·G (secp256k1 skaler çarpım) → X‖Y (64 bayt) → keccak256(X‖Y) (32 bayt) → son 20 bayt = adres`
- 65 baytlık `0x04‖X‖Y` biçimi SEC1 "uncompressed" kodlamasıdır; **adres hash'ine giren
  64 baytlık X‖Y'dir**, 0x04 ön eki hash'e girmez.
- Ethereum **ORİJİNAL Keccak-256** (padding baytı `0x01`) kullanır; FIPS-202 "SHA3-256"
  (padding `0x06`) DEĞİLDİR. Aynı girdi iki fonksiyonda tamamen farklı digest verir.
- Adres 160 bit'tir: 512-bit public key (X‖Y) ve 256-bit hash'ten 20 bayt seçilir
  (adres boyutu + gas/RLP pratikliği; böl. 7'de not olarak).
- EOA adresi public key'e, dolayısıyla private key'e bağlıdır; **sözleşme adresleri
  (CREATE/CREATE2) public key içermez**.
- Somut örnek: `k = 1` → adres `0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf` (böl. 10'da doğrulandı).

## 1. Türetme hattı özeti

```
k  (256 bit, 1 ≤ k ≤ n−1)                         [özel anahtar]
 │  P = k·G — secp256k1 skaler çarpım
 ▼
P = (X, Y)  — afin koordinatlar                   [eğri üzeri nokta]
 │  SEC1 uncompressed: 0x04 ‖ X ‖ Y = 65 bayt     [public key, depolama biçimi]
 │  adres hash'inin girdisi: X ‖ Y = 64 bayt       (0x04 girmez)
 ▼
keccak256(X‖Y)  — ORİJİNAL Keccak, 32 bayt        [hash]
 │  ilk 12 bayt atılır, son 20 bayt alınır
 ▼
adres — 20 bayt (160 bit), gösterim 0x + 40 hex
 │  EIP-55 mixed-case gösterim (opsiyonel, hata tespiti)
 ▼
örn. 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf   (k=1)
```

Hattın her adımı deterministiktir: aynı `k` her zaman aynı adresi verir. Ters adım
(public key'den `k`'ya) ECDLP'dir; #292'de analiz edilir.

## 2. secp256k1 eğrisi ve parametreleri

Eğri, mod `p` tam sayı alanı üzerinde `y² = x³ + a·x + b` formundadır; secp256k1 için `a = 0`,
`b = 7`, yani **y² = x³ + 7 (mod p)**. Parametreler (NIST SEC 2 "secp256k1", EIP-198 ile Ethereum'a alınmıştır):

| Parametre | Değer (hex) |
|---|---|
| `p` (prime) | `0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f` |
| `a` | `0` |
| `b` | `7` |
| `Gx` | `0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798` |
| `Gy` | `0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8` |
| `n` (G'nin order'ı) | `0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141` |
| `h` (cofactor) | `1` |

- `p` bir 256-bit prime'dir ve `p = 2²⁵⁶ − 2³² − 2⁹ − 2⁸ − 2⁷ − 2⁶ − 2⁴ − 2` formundadır
  (hex ile birebir uyumlu; `a = 0` eğri, "k-1 curve" ailesindendir).
- `G` jeneratör noktasıdır; `n·G = ∞` (point at infinity) — bu dosyanın doğrulama betiğiyle
  hesaplandı, `n`'in G için order olduğunu teyit eder. `h = 1` olduğu için tüm nokta grubu
  `n` elemanlıkır: herhangi bir `P` için `n·P = ∞`.
- `n ≈ 1.158 × 10⁷⁷`, `p`'den biraz küçüktür; ikisi de 256 bit prime.

## 3. Özel anahtar: `k ∈ [1, n−1]`

- `k = 0` olamaz: `0·G = ∞` — sonsuzluk noktasının afin koordinatı yoktur, yani
  public key (ve dolayısıyla adres) üretemez.
- `k ≥ n` anlamsızdır: skaler çarpım mod-`n` periyodik olduğu için `k·G = (k mod n)·G`
  (özellikle `n·G = ∞`). Her `k` ile `k+n` aynı noktayı verdiği için standart
  (kano) aralık `1 ≤ k ≤ n−1`'dir.
- Uygulamada `k`, kriptografik güvenli RNG ile bu aralıktan 256 bit rastgele seçilir;
  güvenli aralık dışında seçim (örn. çok küçük `k`) anahtarı zayıflatır — istisnaları #292 işler.
- `k`'nın değerinin kendisi eğri üzerinde hiçbir iz bırakmaz; yalnızca `P = k·G` kalır.

## 4. `P = k·G`: skaler çarpım (double-and-add)

Klasik afin double-and-add, `k`'nin MSB'den LSB'ye:

```
R = ∞;  A = G
her bit için:
    R = 2·R                  (point doubling)
    eğer bit = 1: R = R + A  (point addition)
```

- 256 bit için ~256 doubling + ort. ~128 addition.
- Afin formüller: addition `λ = (y₂−y₁)/(x₂−x₁)`, doubling `λ = 3x₁²/(2y₁)` (`a=0` sayesinde
  `+a` terimi yok), sonra `x₃ = λ²−x₁−x₂`, `y₃ = λ(x₁−x₃)−y₁`.
- Afin aritmetikte her adım modüler ters gerektirir — pahalıdır. Üretim kütüphaneleri
  (libsecp256k1) **Jacobian koordinatları** (`X:Y:Z`, afin karşılığı `x = X/Z²`, `y = Y/Z³`)
  kullanır: döngü boyunca bölme yok, en sonda TEK modüler ters; ayrıca sabit pencere /
  önceden hesaplanmış katlar ile hızlandırma yapar. Matematiksel sonuç afin hesapla birebir aynıdır.
- Sonuç `P = (X, Y)` deterministiktir: aynı `k` için her zaman aynı nokta.

## 5. 65 baytlık uncompressed public key

- SEC1 uncompressed kodlama: `0x04 ‖ X(32 bayt) ‖ Y(32 bayt)` = **65 bayt**.
  (Alternatif compressed form `0x02/0x03 ‖ X` = 33 bayt'tir; `Y`'nin paritesiyle yeniden türetilir.
  Ethereum adres türetimi uncompressed 64 baytlık `X‖Y` girdisini kullanır.)
- Kritik ayrım: **adres hash'inin girdisi 0x04 ön ekini içermeyen 64 baytlık `X‖Y`'dir.**
  Yellow Paper'da public key 64 baytlık koordinat birleşimi olarak tanımlıdır;
  65 baytlık form depolama/iletim kodlamasıdır (böl. 10'daki hash değerleri bunu teyit eder).

## 6. Keccak-256 — ORİJİNAL Keccak (padding `0x01`), FIPS-202 SHA3-256 DEĞİL

- Ethereum, Ethereum Yellow Paper Ek A'da tanımlanan `keccak256`'ı kullanır: sponge yapısı,
  1600-bit durum, rate `r = 1088` bit (136 bayt), capacity 512 bit, 256-bit çıktı.
- **Kritik fark:** 2015'te FIPS-202 standardına giren "SHA3-256", aynı permutasyonu kullanır ama
  padding/domain byte'ı `0x06`'ya değiştirilmiştir (SHA3 domain ayrımı). Orijinal Keccak'ın
  padding byte'ı `0x01`'dir. Sonuç: **aynı girdi, tamamen farklı digest.**
- Doğrulanmış örnekler (bu dosyanın betiğiyle):
  - `keccak256(boş) = 0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470`
  - `sha3-256(boş)  = 0xa7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a`
  - Aynı 65 baytlık public key girdisi için (k=1, `0x04‖X‖Y`):
    `keccak256 = 0x393a75c54f3552ba0c8900297d6e99bb8abf8cc013bb0e912d0b176596fe7b88`
    vs `sha3-256 = 0x5f438d7103705fccbe07cf30522bf6fd0882e58f6feb096b41417b4f8c692c39`.
- Pratik uyarı: çoğu dilin standart kütüphanesindeki `sha3_256` (Python `hashlib.sha3_256`,
  Node `crypto` "sha3-256") **Ethereum'un keccak256'sı değildir**; Ethereum adresi üretmek
  için özel keccak uygulaması gerekir (kaynak: Yellow Paper Ek A; EIP-155'teki signing hash
  de orijinal keccak ile alınmıştır ve bu doğrulamada birebir eşleşti).

## 7. Adres = hash'in son 20 baytı

- `adres = keccak256(X‖Y)[12:]` — 32 baytlık hash'in **ilk 12 baytı atılır, son 20 baytı**
  (160 bit) adrestir. Gösterim: `0x` + 40 hex karakter.
- *Not (kaynak gösterilmemiş iddia değil, gerekçe):* 20 bayt (160 bit, 2¹⁶⁰ adres) alanını
  büyütme zorunluluğu değildir; pratik bir tercihtir — RLP/SSTORE/transfer'de küçük byte
  dizisi (gas ve depolama maliyeti) ve okunabilir kısa gösterim. Rastgele çarpışma olasılığı
  2⁻⁸⁰ (birthday) mertebesinde kalır; 20 baytlık alan yeterince büyüktür. Hash'in 256 → 160 bit
  kırpılması tek yönlü bir operasyon olduğundan güvenlik açısından yeni zayıflık yaratmaz:
  hash zaten tek yönlüdür.
- `X‖Y` (512 bit) ve `keccak` çıktısı (256 bit) adresin 20 baytından fazlasını taşırdı;
  ilk 12 baytı atmak bilgiyi "güvenlik açısından" kaybettirmez, gösterim/boyut pragmatizmidir.

## 8. EIP-55: mixed-case checksum

- Amaç **hata (typo) tespiti**, güvenlik değil: 40 hex karakteri okunurken harf/tek rakam hatası
  yapma riskine karşı ~15 check-bit verir; EIP-55 Rationale'ına göre rastgele bir typo'nun
  checksum'dan geçme olasılığı ≈ %0.0247 (ICAP'a göre ~50× iyileşme).
- Algoritma (doğrulandı, 8/8 resmi vektör birebir):
  1. Adresi `0x`siz **küçük harf hex** dize olarak ASCII'ye çevir.
  2. Bu dizinin `keccak256`'sını al (64 hex karakter; dikkat — girdi bayt değil, **hex dizininin ASCII'si**).
  3. Adresin her i. karakteri harfse ve hash'in i. nibbles'ı `≥ 8` ise büyük harf yaz, değilse küçük.
     Rakamlar ve `0x` ön eki değişmez.
- Örnek: `0x5aaeb6053f3e94c9b9a09f33669435e7ef1beaed` → `0x5Aaeb6053F3E94C9b9A09f33669435E7Ef1BeAed`.
- Kontrol (verify) bu sayede mümkündür: bir adresin mixed-case formu EIP-55'e uygunsa ve
  tümüyle büyük/küçük yazılmışsa checksum doğrulanamaz, karma formda ise doğrulanabilir.

## 9. EOA vs sözleşme adresi: CREATE ve CREATE2

**EOA (externally owned account):** adres, yukarıdaki public key hattından gelir;
private key tarafından "sahiplenir".

**Sözleşme adresi:** public key **İÇERMEZ** — deployer adresi + (nonce veya salt) + init code
tümünü belirler; dolayısıyla bir private key'e aynı bağlamda bağlı değildir.

### CREATE (klasik)
`adres = keccak256( rlp([sender(20 bayt), nonce]) )[12:]`

- `nonce`, gönderen hesabın **güncel** nonce'udur. EIP-161: nonce, init code çalıştırılmadan
  ÖNCE artırılır — yani taze (nonce 0) bir hesaptan ilk sözleşme `nonce = 0` ile oluşturulur.
- RLP kuralı (Yellow Paper Ek B): liste ön eki `0xC0 + uzunluk`; tamsayı `0` → `0x80`
  (boş dizi); tek bayt `0x80`'dan küçük ise olduğu gibi.
  Bu dosyanın doğrulamasında RLP kodlayıcı, EIP-155'in 9 elemanlı imza verisi RLP'sini
  (`0xec098504a817c800825208943535...3535880de0b6b3a764000080018080`) birebir yeniden üreterek teyit edildi.
- Yerel hesap örneği (yöntem: bu dosyanın saf Python RLP + keccak; değerler doğrulanmış
  RLP kodlayıcıyla üretildi): sender = `0x9d8A62f656a8d1615C1294fd71e9CFb3E4855A4F`
  (böl. 10'daki EIP-155 adresi), `nonce = 9`:
  - `rlp([sender, 9]) = 0xd6949d8a62f656a8d1615c1294fd71e9cfb3e4855a4f09`
  - → `0x1fD43573682A8E3CBA6368836BaF6f9DBEadEfCa`
- Sıfır hesap örneği: `rlp([0x000...000, 0]) = 0xd694000000000000000000000000000000000000000080`
  → `0xBd770416a3345F91E4B34576cb804a576fa48EB1`.

### CREATE2 (EIP-1014, Constantinople)
`adres = keccak256( 0xff ‖ deployer(20) ‖ salt(32) ‖ keccak256(init_code) )[12:]`

- Hash girdisi (preimage) her zaman **85 bayt**tir; deterministik ve nonce'a bağlı değil
  (deployer + salt + kod belirlir).
- `0xff` ön eki, CREATE adresleriyle çarpışmayı önler: RLP kodlamasında ilk baytın `0xff`
  olabilmesi ancak çok uzun (Gibabayt mertebesinde) veri dizileri için mümkündür
  (EIP-1014 Rationale: "data many petabytes long"); normal bir CREATE preimage'ı
  (20 baytlık sender + küçük nonce) asla `0xff` ile başlayamaz.
- Doğrulama: EIP-1014'ün 7 resmi örneğinin **tamamı** bu dosyanın betiğiyle birebir
  (checksum dahil) yeniden üretildi. Öne çıkan iki örnek:
  - deployer `0x000...000`, salt `0x000...000`, `init_code = 0x00` → `0x4D1A2e2bB4F88F0250f26Ffff098B0b30B26BF38`
  - deployer `0x000...000`, salt `0x000...000`, `init_code = 0x` (boş) → `0xE33C0C7F7df4809055C3ebA6c09CFe4BaF1BD9e0`

## 10. Somut örnekler

### Örnek A: `k = 1` (jeneratör noktası)
`P = 1·G = G`, yani public key zaten G'dir — hattın en kısa doğrulama vektörü.

| Aşama | Değer |
|---|---|
| `k` | `1` |
| `P = k·G` | `(Gx, Gy)` = böl. 2'deki jeneratör |
| public key (65B, `0x04‖X‖Y`) | `0x0479be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8` |
| `keccak256(X‖Y)` (64 bayt girdi) | `0xc0a6c424ac7157ae408398df7e5f4552091a69125d5dfcb7b8c2659029395bdf` |
| atılan ilk 12 bayt | `0xc0a6c424ac7157ae408398df` |
| adres (son 20 bayt) | `0x7e5f4552091a69125d5dfcb7b8c2659029395bdf` |
| EIP-55 gösterim | `0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf` |

Doğrulama: `double-and-add` (kendi afin implementasyonu) + pycryptodome keccak ile yukarıdaki
her satır üretildi; EIP-55 çıktısı bölüm 8'deki resmi algoritmayla birebir.
Not: adres hash girdisi 64 baytlık `X‖Y`'dir — 65 baytlık formun hash'i
(`0x393a75c5...`, böl. 6) adresten **farklıdır**; 0x04'ün girmediğinin kanıtıdır.

### Örnek B: EIP-155 test vektörü
EIP-155'in (replay koruması) resmi örneği `k = 0x4646464646464646464646464646464646464646464646464646464646464646`
private key'ini kullanır. Hattın çıktısı:

| Aşama | Değer |
|---|---|
| public key (65B) | `0x044bc2a31265153f07e70e0bab08724e6b85e217f8cd628ceb62974247bb493382ce28cab79ad7119ee1ad3ebcdb98a16805211530ecc6cfefa1b88e6dff99232a` |
| `keccak256(X‖Y)` | `0x9cead80a9d0a0951cdbf966b9d8a62f656a8d1615c1294fd71e9cfb3e4855a4f` |
| adres | `0x9d8a62f656a8d1615c1294fd71e9cfb3e4855a4f` |
| EIP-55 gösterim | `0x9d8A62f656a8d1615C1294fd71e9CFb3E4855A4F` |

Üç bağımsız doğrulama yolu (tümü bu dosyanın betiğiyle):
1. **`k·G` skaler çarpımı** (afin double-and-add) → yukarıdaki public key.
2. **`ecrecover`**: EIP-155'in kendi verdiği imza değerleri
   (signing hash `0xdaf5a779ae972f972197303d7b574746c7ef83eadac0f2791ad23db92e4c8e53`,
   `v = 37` = parite(0) + 2·CHAIN_ID(1) + 35,
   `r = 18515461264373351373200002665853028612451056578545711640558177340181847433846`,
   `s = 46948507304638947509940763649030358759909902576025900602547168820602576006531`)
   ile imzadan public key geri türetildi → yol 1 ile **aynı nokta**.
3. **RLP + keccak**: EIP'nin imza verisi RLP'si `0xec098504a817c800825208943535353535353535353535353535353535353535880de0b6b3a764000080018080`
   sıfırdan yeniden üretildi (birebir) ve onun keccak256'sı signing hash ile birebir eşleşti
   (böl. 6'daki "orijinal keccak" notunun kanıtı).

k=1 ve bu vektör, hattın iki ucunu (küçük k ve rastgele k) kapsayan çapraz doğrulama sağlar.

## Kaynaklar

- NIST SEC 2 (Draft 3), "Recommended Elliptic Domain Parameters" — secp256k1 tablosu; EIP-198.
- Ethereum Yellow Paper (Buterin) — §4.1 (adres = public key'in keccak'ının son 20 baytı,
  public key 64 baytlık `X‖Y`), Ek A (`keccak256`, rate 1088, orijinal Keccak padding `0x01`),
  Ek B (RLP), `GCREATE`/`Gcreate2` (CREATE adres formülü).
- EIP-155 (Spurious Dragon, mainnet CHAIN_ID=1) — resmi örnek: private key `0x464646...46`,
  imza verisi RLP, signing hash, (v, r, s); imza RLP + ecrecover ile çapraz doğrulandı.
- EIP-55 — mixed-case checksum algoritması ve 8 resmi test vektörü (8/8 doğrulandı).
- EIP-1014 (CREATE2) — formül, 85 baytlık preimage, 7 resmi örnek (7/7 doğrulandı).
- EIP-161 — CREATE'te nonce'ün init code'dan önce artırılması.
- Doğrulama aracı: saf Python afin nokta çarpımı + pycryptodome `keccak` (orijinal Keccak-256).
