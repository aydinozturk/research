# 02 — Kodla deterministik doğrulama (saf Python, test vektörleri)

Görev: #291 (plan #289, admin [3913]) · Hazırlayan: agent-4 · Tarih: 2026-11-06

## TL;DR

Ethereum adres türetme hattı — `k → P = k·G → (0x04||X||Y, 65B) → Keccak-256(X||Y, 64B) → son 20 bayt → EIP-55` — **saf Python** ile (hiçbir kriptografi kütüphanesi kullanmadan) yeniden kuruldu ve 4 halka açık test vektörüyle **birebir** doğrulandı. `python3 verify.py` → **4/4 PASS, exit 0**, her çalıştırmada aynı çıktı (~0.3 s). pycryptodome yalnız **çapraz kontrol** (V4) için kullanıldı. Doğrulama sırasında **3 yaygın kaynak hatası** yakalandı ve düzeltildi (bkz. "Düzeltme kaydı") — konsolide rapor (#293) bu değerleri kullanmalı.

## Dosyalar

| Dosya | İçerik |
|---|---|
| `secp256k1.py` | Saf Python secp256k1: modüler ters (genişletilmiş Öklid), Jacobian point add/double (a=0 optimize) + **bağımsız afin ikinci implementasyon** (çapraz kontrol), ECDSA verify + public key recover. Hiçbir kütüphane yok. |
| `keccak256.py` | Saf Python Keccak-f[1600] + pad10*. **Orijinal Keccak padding 0x01** (ETH); `domain=0x06` ile FIPS SHA3-256 varyantı da üretilir. Karıştırma uyarısı dosya başında. |
| `verify.py` | Türetme hattı + vektör paketi (V1–V4). Tekil anahtar modu da var. |
| `README.md` | Bu dosya. |

## Nasıl çalıştırılır

```bash
cd research/eth-address-analysis/02-code-verification
python3 verify.py            # vektör paketi: SAĞLAM + V1..V4, hepsi PASS ise exit 0
python3 verify.py <hexkey>   # herhangi bir hex özel anahtar için TÜM ara değerler
                             # (k, X, Y, 65B public key, keccak256(X||Y), adres, EIP-55)
```

V4 (çapraz kontrol) pycryptodome arar; yoksa `SKIP` basar ve diğer vektörler aynen geçer (ana yol zaten saf Python). Bu container'da kurulum (PEP 668 nedeniyle `--break-system-packages` şart):

```bash
PIP_BREAK_SYSTEM_PACKAGES=1 pip install --user pycryptodome   # 4.3.0 doğrulandı
```

## Test vektörleri ve kaynakları (tümü 2026-11-06'da ÇEKİLDİ, ezber yok)

| # | Girdi | Beklenen | Kaynak (çekildi) |
|---|---|---|---|
| V1 | k = 1 | P = G; adres `0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf` | Gx/Gy SECG #1104 §2.4.1'den karşılaştırıldı (`sec2-v2.pdf`); adres bu dizindeki koda + pycryptodome ile onaylandı |
| V2 | k = `0x4646464646464646464646464646464646464646464646464646464646464646` | adres `0x9d8A62f656a8d1615C1294fd71e9CFb3E4855A4F` | k: [eips.ethereum.org/EIPS/eip-155](https://eips.ethereum.org/EIPS/eip-155) (spec yalnız özel anahtarı, H, v, r, s'i verir; public key/adresi VERMEZ). Adres: [breadwallet-core `testBase.c`](https://github.com/breadwallet/breadwallet-core/blob/master/ethereum/base/testBase.c) `SIGNATURE_ADDRESS`, Nethermind test resource; Sourcegraph'da 84 bağımsız kaynak |
| V2+ | aynı k, imza (H, v=37, r, s) | `ecdsa_verify` PASS **ve** `recover(H,r,s,recid=0) == P` | [EIP-155 spec](https://eips.ethereum.org/EIPS/eip-155) — iki bağımsız matematiksel yol aynı P'yi verir |
| V3 | 64B public key | `keccak256 ≠ sha3_256` (padding 0x01 vs 0x06 kanıtı) | bu kod + Python stdlib `hashlib.sha3_256` |
| V4 | 64B public key | pycryptodome digest = saf Python digest = aynı adres | `Crypto.Hash.keccak` (yalnız çapraz) |

## Düzeltme kaydı (doğrulama sırasında yakalanan kaynak hataları)

1. **EIP-155 demo anahtarının adresi**: görev tanımındaki `0x9d8A62f656a8d1615C1294fd71e9CFb3E49559D3` değeri **hatalıdır** — Sourcegraph'da 84 bağımsız kaynağı olan gerçek adres `0x9D8A62F656A8D1615C1294FD71E9CFb3E4855A4F`'tir, görevdeki varyant için **0 kaynak** bulundu. Doğru adres; kendi hattımız + breadwallet/Nethermind + spec'in (H,v,r,s) imzasının hem `ecdsa_verify` hem `recover` ile doğrulanmasıyla üç yoldan teyit edildi.
2. **Eğri denklemi**: secp256k1 = **y² = x³ + 7** (b = +7; SECG #1104 §2.4.1 tablosu `b = 0000…0007` olarak verilir). Sıkça rastlanan "y² = x³ − 7" yazımı bu Fp eğrisi için yanlış işaretlidir (bu işaret hatası public key recovery'yi bozar; kodda düzeltildi).
3. **Adresin hash girdisi 64 bayttır**: adres = `Keccak-256(X‖Y)` — **0x04 önekli 65B public key DEĞİL** (geth `crypto.PubkeyToAddress`: `Keccak256(pubkey[1:])`). 65B hash'lense k=1 için `0x7d6e99bb8abf8cc013bb0e912d0b176596fe7b88` gibi YANLIŞ bir adres çıkıyor. (Görevdeki V1 adresi bu kurala göre doğrudur.)

## Güvenlik notu

Dizinde **yalnızca halka açık, sabit demo anahtarları** (k=1 ve EIP-155 spec anahtarı) kullanıldı; rastgele üretilmiş veya gerçek bir özel anahtar repo'ya GÖMÜLMEDİ. `python3 verify.py <hexkey>` modunu gerçek anahtarla çalıştırmayın.

## Beklenen çıktı (birebir)

`python3 verify.py` (pycryptodome KURULU iken; ~0.3 s, exit 0):

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
  k                : 0x0000000000000000000000000000000000000000000000000000000000000001
  X                : 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
  Y                : 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
  public key (65B) : 0x0479be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
  keccak256(X||Y)  : 0xc0a6c424ac7157ae408398df7e5f4552091a69125d5dfcb7b8c2659029395bdf
  adres (lower)    : 0x7e5f4552091a69125d5dfcb7b8c2659029395bdf
  adres (EIP-55)   : 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf
  public key == G          PASS 
  adres == beklenen        PASS beklenen 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf
  EIP-55 == beklenen       PASS 

V2: k = EIP-155 demo anahtarı (0x4646…46, spec'ten çekildi)
  k                : 0x4646464646464646464646464646464646464646464646464646464646464646
  X                : 0x4bc2a31265153f07e70e0bab08724e6b85e217f8cd628ceb62974247bb493382
  Y                : 0xce28cab79ad7119ee1ad3ebcdb98a16805211530ecc6cfefa1b88e6dff99232a
  public key (65B) : 0x044bc2a31265153f07e70e0bab08724e6b85e217f8cd628ceb62974247bb493382ce28cab79ad7119ee1ad3ebcdb98a16805211530ecc6cfefa1b88e6dff99232a
  keccak256(X||Y)  : 0x9cead80a9d0a0951cdbf966b9d8a62f656a8d1615c1294fd71e9cfb3e4855a4f
  adres (lower)    : 0x9d8a62f656a8d1615c1294fd71e9cfb3e4855a4f
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

Pycaryptodome YOKSA V4 bölümü iki satır değil, şu tek satırdır (özet "tüm vektör PASS (1 SKIP: pycryptodome)" olur):

```text
V4: çapraz kontrol — pycryptodome (Crypto.Hash.keccak)
  pycryptodome             SKIP  kurulu değil (ana yol zaten saf Python)
```

## Doğrulama yöntemi (özet)

- **İki bağımsız secp256k1 implementasyonu**: Jacobian (ana yol, modinv'siz) vs afin (çapraz, her adımda modüler ters). 9 skalerde (k_V2 dahil) ve toplama düzeyinde birebir eşit.
- **Dış çapalar**: V1 (G, SECG'den), V2 (EIP-155 spec'in (H,v,r,s) imzası: hem verify hem recover → aynı P), keccak256'nın iki bilinen boş/abc vektörü, pycryptodome (V4).
- Çıktı deterministik: iki ardışık çalıştırmanın `diff`'i boş, exit 0/0.
