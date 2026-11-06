"""secp256k1 — saf Python (üçüncü parti kütüphane YOK).

Eğri:  y² = x³ + a·x + b   (F_p üzerinde),  a = 0,  b = 7
  (SECG Sertifika #1104 / SEC 2 §2.4.1: "b = 0000…0007". Sıkça rastlanan
  "y² = x³ − 7" yazımı bu eğri için YANLIŞTIR — bu dosyada b = +7 ve
  is_on_curve / ecdsa_recover buna göre hesaplar.)
  p = 2^256 − 2^32 − 977
  G = (GX, GY)  (grup üreteci)
  n = eğrinin mertebesi (G'nin order'ı),  cofactor h = 1

Nokta aritmeti Jacobian koordinatlarında yapılır: (X, Y, Z),  Z = 0 → sonsuzluk.
Jacobian → afin dönüşümü:  x = X·Z⁻²,  y = Y·Z⁻³  (mod p).

Bu dosyadaki formüller "a = 0" için optimize edilmiş standart Jacobian
formülleri (HAC Algoritma 3.23 / SECG J-2002-l çarpım ve J-2007-bl toplama)
dir; doğrulama verify.py içinde yapılır (V1/V2 + n·G = O + eğri üyeliği).
"""

P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
A = 0
B = 7
GX = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
GY = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

INFINITY = (0, 1, 0)  # Jacobian sonsuzluk: Z = 0
G = (GX, GY, 1)


def modinv(a, m):
    """a'nın m modüler tersi — genişletilmiş Öklid (a, m aralarında asal)."""
    a %= m
    if a == 0:
        raise ValueError("0'ın modüler tersi yok")
    old_r, r = a, m
    old_s, s = 1, 0
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    if old_r != 1:
        raise ValueError("ters alınamaz")
    return old_s % m


def is_on_curve(x, y):
    """Afin noktanın y² = x³ − 7 üzerinde olup olmadığı."""
    return (y * y - x * x * x - A * x - B) % P == 0


def jac_double(pt):
    """Jacobian 2·P (a = 0 için optimize)."""
    if pt[2] == 0:
        return INFINITY
    X1, Y1, Z1 = pt
    X1 %= P; Y1 %= P; Z1 %= P
    if Y1 == 0:
        return INFINITY
    # A=X1², B=Y1², C=B², D=2((X1+B)²−A−C), E=3A, F=E²
    A_ = X1 * X1 % P
    B_ = Y1 * Y1 % P
    C_ = B_ * B_ % P
    D = 2 * ((X1 + B_) ** 2 - A_ - C_) % P
    E = 3 * A_ % P
    F = E * E % P
    X3 = (F - 2 * D) % P
    Y3 = (E * (D - X3) - 8 * C_) % P
    Z3 = (2 * Y1 * Z1) % P
    return (X3, Y3, Z3)


def jac_add(p1, p2):
    """Jacobian P1 + P2 (a = 0, w = 2·H·Z1·Z2 ölçekli sonuç).

    U1=X1·Z2², U2=X2·Z1², S1=Y1·Z2³, S2=Y2·Z1³, H=U2−U1, Δ=S2−S1
      X3 = 4Δ² − 4H²(U1+U2)
      Y3 = 8Δ·H²·(2U1+U2) − 8Δ³ − 8S1·H³
      Z3 = 2·H·Z1·Z2
    Afin (Z1=Z2=1) halde λ=Δ/H ile x3=λ²−x1−x2, y3=λ(2x1+x2)−λ³−y1
    formüllerine birebir indirgenir (verify.py'de afin implementasyonla
    çapraz doğrulanır).
    """
    if p1[2] == 0:
        return p2
    if p2[2] == 0:
        return p1
    X1, Y1, Z1 = (v % P for v in p1)
    X2, Y2, Z2 = (v % P for v in p2)
    Z1sq = Z1 * Z1 % P
    Z2sq = Z2 * Z2 % P
    U1 = X1 * Z2sq % P
    U2 = X2 * Z1sq % P
    S1 = Y1 * Z2sq % P * Z2 % P
    S2 = Y2 * Z1sq % P * Z1 % P
    if U1 == U2:
        if S1 != S2:
            return INFINITY
        return jac_double(p1)
    H = (U2 - U1) % P
    d = (S2 - S1) % P
    H2 = H * H % P
    X3 = (4 * d * d - 4 * H2 * (U1 + U2)) % P
    Y3 = (8 * d * H2 * (2 * U1 + U2) - 8 * d * d * d - 8 * S1 * H2 * H) % P
    Z3 = (2 * H * Z1 * Z2) % P
    return (X3, Y3, Z3)


def jac_to_affine(pt):
    """Jacobian → afin (x, y); sonsuzluk için None."""
    if pt[2] == 0:
        return None
    X, Y, Z = (v % P for v in pt)
    Zi = modinv(Z, P)
    Zi2 = Zi * Zi % P
    Zi3 = Zi2 * Zi % P
    return (X * Zi2 % P, Y * Zi3 % P)


def scalar_mult(k, pt=None):
    """k·P — çiftle-yarala (double-and-add), MSB'den LSB'ye."""
    if pt is None:
        pt = G
    k %= N
    result = INFINITY
    addend = pt
    while k:
        if k & 1:
            result = jac_add(result, addend)
        addend = jac_double(addend)
        k >>= 1
    return result


def mul(k):
    """k·G (afin; k = 0 için None)."""
    return jac_to_affine(scalar_mult(k, G))


# ------------------------------------------------ afin (çapraz kontrol) -----
# Bağımsız ikinci implementasyon: her adımda afin koordinat + 1 modüler ters.
# Jacobian yolunu verify.py'de doğrulamak için kullanılır (farklı formül,
# farklı kod yolu). Performans amaçlı DEĞİLDİR; doğrulama amaçlıdır.

def add_affine(p1, p2):
    """Afin P1 + P2;  p1/p2: (x, y) veya None (sonsuzluk). a = 0."""
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        if (y1 + y2) % P == 0:
            return None                    # zıt noktalar → O
        lam = 3 * x1 * x1 * modinv(2 * y1, P) % P   # çiftleme
    else:
        lam = (y2 - y1) * modinv(x2 - x1, P) % P
    x3 = (lam * lam - x1 - x2) % P
    y3 = (lam * (x1 - x3) - y1) % P
    return (x3, y3)


def scalar_mult_affine(k, pt=None):
    """k·P afin yol (double-and-add). pt=None ise G."""
    if pt is None:
        pt = (GX, GY)
    k %= N
    result = None
    addend = pt
    while k:
        if k & 1:
            result = add_affine(result, addend)
        addend = add_affine(addend, addend)
        k >>= 1
    return result


def pubkey_from_scalar(k):
    """P = k·G → 65 baytlık uncompressed public key (0x04 || X || Y)."""
    if not (1 <= k < N):
        raise ValueError("k, [1, n−1] aralığında olmalı")
    x, y = mul(k)
    return b"\x04" + x.to_bytes(32, "big") + y.to_bytes(32, "big")


def ecdsa_verify(h_int, r, s, Q):
    """Standart ECDSA doğrulama: Q afin public key, h_int = H mod n."""
    if not (1 <= r < N and 1 <= s < N):
        return False
    e = h_int % N
    w = modinv(s, N)
    u1 = e * w % N
    u2 = r * w % N
    X = jac_add(scalar_mult(u1, G), scalar_mult(u2, (Q[0], Q[1], 1)))
    if X[2] == 0:
        return False
    x3 = jac_to_affine(X)[0]
    return x3 == r


def ecdsa_recover(h_int, r, s, recid):
    """(H, r, s, recid) → afin public key (Ethereum compact-signature recovery)."""
    if not (1 <= r < N and 1 <= s < N):
        raise ValueError("r veya s geçersiz")
    if not (0 <= recid <= 3):
        raise ValueError("recid geçersiz")
    x = r + (recid // 2) * N
    if x >= P:
        raise ValueError("x koordinatı p'den büyük")
    # y² = x³ + 7 (b = +7);  p ≡ 3 (mod 4)  →  y = t^((p+1)/4)
    t = (x * x * x + B) % P
    y = pow(t, (P + 1) // 4, P)
    if (y * y - t) % P != 0:
        raise ValueError("x² kökü yok")
    if y % 2 != recid % 2:
        y = P - y
    R = (x, y, 1)
    e = h_int % N
    ri = modinv(r, N)
    # Q = r⁻¹ · (s·R − e·G)
    X = jac_add(scalar_mult(s, R), scalar_mult((N - e % N) % N, G))
    Q = jac_to_affine(scalar_mult(ri, X))
    if Q is None:
        raise ValueError("kurtarma sonsuzluk verdi")
    return Q
