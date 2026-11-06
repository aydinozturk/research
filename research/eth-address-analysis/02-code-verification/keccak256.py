"""Keccak-256 — saf Python (üçüncü parti kütüphane YOK).

Keccak-f[1600] permutasyonu + "pad10*" süngeri.

UYARI (görevde istenen ayırım):
  - ETH "Keccak-256" = Orijinal Keccak,  padding byte = 0x01  (bu dosyanın varsayılanı)
  - FIPS 202 "SHA3-256" (hashlib.sha3_256) = padding byte = 0x06
  İkisinden Keccak-f[1600] çekirdeği aynıdır; AYNI girdi FARKLI hash üretir.
  `keccak256(data, domain=0x06)` ile FIPS varyantı da üretilir (karşılaştırma için).

256-bit çıktı için rate = 1088 bit = 136 bayt. Squeeze: 4 lane (32 bayt, little-endian).

Doğrulama (verify.py V3/V4):  keccak256(b'') =
  c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470
  ve pycryptodome (Crypto.Hash.keccak) ile birebir eşitlik.
"""

MASK64 = 0xFFFFFFFFFFFFFFFF

# Keccak-f[1600] tur sabitleri (RC[0..23])
_RC = (
    0x0000000000000001, 0x0000000000008082, 0x800000000000808A, 0x8000000080008000,
    0x000000000000808B, 0x0000000080000001, 0x8000000080008081, 0x8000000000008009,
    0x000000000000008A, 0x0000000000000088, 0x0000000080008009, 0x000000008000000A,
    0x000000008000808B, 0x800000000000008B, 0x8000000000008089, 0x8000000000008003,
    0x8000000000008002, 0x8000000000000080, 0x000000000000800A, 0x800000008000000A,
    0x8000000080008081, 0x8000000000008080, 0x0000000080000001, 0x8000000080008008,
)

# ρ adımının döndürme ofsetleri, ROT[x][y]  (lane indeksi i = x + 5y)
_ROT = (
    (0, 36, 3, 41, 18),
    (1, 44, 10, 45, 2),
    (62, 6, 43, 15, 61),
    (28, 55, 25, 21, 56),
    (27, 20, 39, 8, 14),
)


def _rotl64(v, n):
    n %= 64
    return ((v << n) | (v >> (64 - n))) & MASK64 if n else v


def keccak_f(state):
    """Keccak-f[1600]: 24 tur.  state = 25 adet 64-bit lane, i = x + 5y. Yerinde."""
    for rc in _RC:
        # θ
        C = [state[x] ^ state[x + 5] ^ state[x + 10] ^ state[x + 15] ^ state[x + 20]
             for x in range(5)]
        D = [C[(x - 1) % 5] ^ _rotl64(C[(x + 1) % 5], 1) for x in range(5)]
        for x in range(5):
            for y in range(5):
                state[x + 5 * y] ^= D[x]
        # ρ + π
        B = [0] * 25
        for x in range(5):
            for y in range(5):
                B[y + 5 * ((2 * x + 3 * y) % 5)] = _rotl64(state[x + 5 * y], _ROT[x][y])
        # χ
        for x in range(5):
            for y in range(5):
                state[x + 5 * y] = B[x + 5 * y] ^ (
                    (~B[(x + 1) % 5 + 5 * y] & MASK64) & B[(x + 2) % 5 + 5 * y])
        # ι
        state[0] ^= rc
    return state


def keccak256(data, domain=0x01):
    """Keccak-256 (domain=0x01, ETH) veya SHA3-256 varyantı (domain=0x06)."""
    RATE = 136  # byte
    st = [0] * 25
    padded = bytearray(data)
    padded.append(domain)                      # pad10*: 0x01 (orijinal) / 0x06 (FIPS)
    while len(padded) % RATE != 0:
        padded.append(0x00)
    padded[-1] |= 0x80
    for off in range(0, len(padded), RATE):    # absorb (little-endian lane'lar)
        for i in range(RATE // 8):
            st[i] ^= int.from_bytes(padded[off + 8 * i: off + 8 * i + 8], "little")
        keccak_f(st)
    return b"".join(st[i].to_bytes(8, "little") for i in range(4))  # squeeze 32 byte
