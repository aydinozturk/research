#!/usr/bin/env python3
"""Ethereum adres türetme hattı — deterministik doğrulama (saf Python).

Hattın adımları:
  k  →  P = k·G  →  uncompressed public key (0x04||X||Y, 65B)
  →  Keccak-256(X||Y, 64B)  →  son 20 bayt = adres  →  EIP-55 mixed-case
  (Adres hesabı 65B anahtarın 0x04 önekli HALE değil, X||Y 64 baytlık
   kısmına uygulanır — geth crypto.PubkeyToAddress: "Keccak256(pubkey[1:])."
   0x04'ü de hash'lemek farklı ve YANLIŞ bir adres verir.)

Kullanım:
  python3 verify.py            → tam vektör paketi (V1..V4), hepsi PASS ise exit 0
  python3 verify.py <hexkey>   → verilen özel anahtar için TÜM ara değerleri basar
                                  (beklenen değer iddiası yok, salt türetme)

Çıktı deterministiktir: her çalıştırmada birebir aynı satırlar; sahte/tesadüfi
veri içermez. Anahtarlar yalnızca aşağıdaki halka açık, sabit demo vektörleridir.
"""

import hashlib
import sys

from secp256k1 import (P, N, G, GX, GY, INFINITY, scalar_mult, jac_add,
                       jac_to_affine, mul, is_on_curve, ecdsa_verify,
                       ecdsa_recover, pubkey_from_scalar, add_affine,
                       scalar_mult_affine)
from keccak256 import keccak256


# ---------------------------------------------------------------- araçlar ----
def eip55(address_hex):
    """EIP-55 checksum: adresin harfleri keccak256(addr) nibble'larıyla seçilir."""
    h = keccak256(address_hex[2:].lower().encode()).hex()
    return "0x" + "".join(c.upper() if int(h[i], 16) >= 8 else c
                          for i, c in enumerate(address_hex[2:]))


def derive(k):
    """k → tüm ara değerler (dict). k: int."""
    pk = pubkey_from_scalar(k)          # 65 bayt: 0x04 || X || Y
    x, y = int.from_bytes(pk[1:33], "big"), int.from_bytes(pk[33:65], "big")
    xy = pk[1:]                         # 64 bayt: X || Y (adresi hash'lenen kısım)
    digest = keccak256(xy)              # 32 bayt (ETH Keccak, padding 0x01)
    addr = "0x" + digest[12:].hex()     # son 20 bayt
    return {"k": k, "X": x, "Y": y, "pubkey": pk, "digest": digest,
            "addr": addr, "eip55": eip55(addr)}


def hx(v, pad=64):
    return "0x" + format(v, "x").rjust(pad, "0")


def print_derive(d):
    print(f"  k                : {hx(d['k'])}")
    print(f"  X                : {hx(d['X'])}")
    print(f"  Y                : {hx(d['Y'])}")
    print(f"  public key (65B) : 0x{d['pubkey'].hex()}")
    print(f"  keccak256(X||Y)  : 0x{d['digest'].hex()}")
    print(f"  adres (lower)    : {d['addr']}")
    print(f"  adres (EIP-55)   : {d['eip55']}")


# ------------------------------------------------------------ vektörler -----
# V1 — k = 1: public key = G, adres = ünlü "G adresi"
V1_ADDR = "0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf"
# V2 — EIP-155 demo anahtarı (eips.ethereum.org/EIPS/eip-155, 2026-11-06 çekildi)
V2_K = int("4646464646464646464646464646464646464646464646464646464646464646", 16)
# adres: breadwallet-core/ethereum/base/testBase.c ve Nethermind test resource
# (Sourcegraph'da 84 bağımsız kaynak; 2026-11-06 çekildi). NOT: bazı kaynaklarda
# geçen "...CFb3E49559D3" varyantının 0 kaynağı bulundu — bkz. README.
V2_ADDR = "0x9D8A62F656A8D1615C1294FD71E9CFB3E4855A4F"
# EIP-155 spec'teki imza vektörü (tamamı eips.ethereum.org'dan çekildi)
V2_H = int("daf5a779ae972f972197303d7b574746c7ef83eadac0f2791ad23db92e4c8e53", 16)
V2_V = 37  # → chainid = (37−35)//2 = 1,  recid = (37−35)%2 = 0
V2_R = 18515461264373351373200002665853028612451056578545711640558177340181847433846
V2_S = 46948507304638947509940763649030358759909902576025900602547168820602576006531

KECCAK_EMPTY = "c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470"


def run_suite():
    fails, skips = [], []

    def check(name, ok, detail=""):
        print(f"  {name:<24} {'PASS' if ok else 'FAIL'} {detail}")
        if not ok:
            fails.append(name)

    def skip(name, why):
        print(f"  {name:<24} SKIP  {why}")
        skips.append(name)

    print("Ethereum adres türetme hattı — deterministik doğrulama (saf Python)")
    print("=" * 64)
    print()

    # --- iç tutarlılık sağlamı (kütüphane formüllerinin kendisini test eder)
    print("SAĞLAM (iç tutarlılık):")
    check("keccak256(b'')", keccak256(b"").hex() == KECCAK_EMPTY,
          "= " + keccak256(b"").hex())
    check("keccak256('abc') (ETH)",
          keccak256(b"abc").hex()
          == "4e03657aea45a94fc7d47ba826c8d667c0d1e6e33a64a036ec44f58fa12d6c45",
          "= " + keccak256(b"abc").hex())
    check("G üzerinde y²=x³+7 (b=+7, SECG §2.4.1)", is_on_curve(GX, GY))
    check("(n−1)·G = −G",
          jac_to_affine(scalar_mult(N - 1)) == (GX, P - GY))
    check("n·G = O",
          jac_to_affine(jac_add(scalar_mult(N - 1), G)) is None,
          "((n−1)·G + G = O)")
    check("3·G = G + 2·G",
          mul(3) == jac_to_affine(jac_add(G, scalar_mult(2))))
    check("123·G = 100·G + 23·G",
          mul(123) == jac_to_affine(jac_add(scalar_mult(100), scalar_mult(23))))
    _xs = [1, 2, 3, 5, 7, 64, 123, (1 << 32) + 1, V2_K]
    check("Jacobian vs afin (9 k)",
          all(mul(i) == scalar_mult_affine(i) for i in _xs),
          "(bağımsız 2. implementasyon, k_V2 dahil)")
    check("jac_add vs add_affine",
          jac_to_affine(jac_add(scalar_mult(5), scalar_mult(7)))
          == add_affine(mul(5), mul(7)),
          "(5·G + 7·G = 12·G)")
    check("eğri üyeliği (123·G)", is_on_curve(*mul(123)))
    check("sha3 varyantı (0x06)",
          keccak256(b"abc", domain=0x06) == hashlib.sha3_256(b"abc").digest(),
          "(bizim FIPS varyantı = hashlib.sha3_256)")
    print()

    # --- V1
    print("V1: k = 1  (public key = G, 'G adresi' vektörü)")
    d1 = derive(1)
    print_derive(d1)
    check("public key == G", d1["X"] == GX and d1["Y"] == GY)
    check("adres == beklenen", d1["addr"] == V1_ADDR.lower(),
          f"beklenen {V1_ADDR}")
    check("EIP-55 == beklenen", d1["eip55"] == V1_ADDR)
    print()

    # --- V2
    print("V2: k = EIP-155 demo anahtarı (0x4646…46, spec'ten çekildi)")
    d2 = derive(V2_K)
    print_derive(d2)
    check("adres == beklenen", d2["addr"] == V2_ADDR.lower(),
          f"beklenen {V2_ADDR}")
    check("EIP-55 idempotent", eip55(d2["eip55"]) == d2["eip55"],
          "(checksum fonksiyonu sabit noktalı)")
    recid = (V2_V - 35) % 2
    chainid = (V2_V - 35) // 2
    print(f"  EIP-155 imza kontrolü (H, v={V2_V} → chainid={chainid}, "
          f"recid={recid}, r, s — hepsi spec'ten):")
    check("ecdsa_verify(H, r, s, P)",
          ecdsa_verify(V2_H, V2_R, V2_S, (d2["X"], d2["Y"])))
    rec = ecdsa_recover(V2_H, V2_R, V2_S, recid)
    check("recover(H, r, s, recid) == P",
          rec == (d2["X"], d2["Y"]),
          "(bağımsız 2. yol: imzadan public key kurtarma)")
    print()

    # --- V3
    print("V3: Keccak-256 (ETH, padding 0x01) ≠ SHA3-256 (FIPS, padding 0x06)")
    pk = d2["pubkey"][1:]  # 64B X||Y — hattın hash girdisi (0x04 öneki hariç)
    keth = keccak256(pk)
    kfips = hashlib.sha3_256(pk).digest()
    print(f"  keccak256 (ETH)    = 0x{keth.hex()}")
    print(f"  sha3_256  (FIPS)   = 0x{kfips.hex()}")
    check("ikisi FARKLI", keth != kfips,
          "(aynı girdi, farklı padding → farklı hash: kanıtlandı)")
    print()

    # --- V4
    print("V4: çapraz kontrol — pycryptodome (Crypto.Hash.keccak)")
    try:
        from Crypto.Hash import keccak as _k
    except ImportError:
        skip("pycryptodome", "kurulu değil (ana yol zaten saf Python)")
    else:
        h1 = _k.new(digest_bits=256)
        h1.update(pk)
        cross = bytes(h1.digest())
        check("digest birebir aynı", cross == keth)
        cross_addr = eip55("0x" + cross[12:].hex())
        check("adres birebir aynı", cross_addr == d2["eip55"], f"= {cross_addr}")
    print()

    if fails:
        print(f"ÖZET: {len(fails)} BAŞARISIZ: {', '.join(fails)}"
              + (f" | SKIP: {', '.join(skips)}" if skips else ""))
        return 1
    if skips:
        print(f"ÖZET: tüm vektör PASS (1 SKIP: {', '.join(skips)})")
    else:
        print("ÖZET: 4/4 vektör PASS — hattın tüm aşamaları birebir doğrulandı.")
    return 0


def single_key(hexkey):
    k = int(hexkey, 16)
    d = derive(k)
    print("Tekil türetme (beklenen değer iddiası YOK):")
    print_derive(d)
    return 0


if __name__ == "__main__":
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        try:
            k = int(arg, 16)
        except ValueError:
            print("Kullanım: python3 verify.py [hex private key]")
            sys.exit(2)
        if not (1 <= k < N):
            print("Kullanım: python3 verify.py [hex private key]")
            sys.exit(2)
        sys.exit(single_key(arg))
    sys.exit(run_suite())
