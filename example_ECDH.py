import random
import math
from sympy import isprime, mod_inverse, legendre_symbol
from hashlib import sha256


def find_cyclic_group(a, b, p):
    cyclic_group = []
    for x in range(p):
        rhs = (x ** 3 + a * x + b) % p
        if legendre_symbol(rhs, p) == 1:
            y = pow(rhs, (p + 1) // 4, p)
            cyclic_group.append((x, y))
            if y != 0:
                cyclic_group.append((x, p - y))
    cyclic_group.append("O")
    return cyclic_group


def point_addition(P, Q, a, b, p):
    if P == "O":
        return Q
    if Q == "O":
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and y1 != y2:
        return "O"
    if P == Q:
        m = (3 * x1 ** 2 + a) * mod_inverse(2 * y1, p) % p
    else:
        m = (y2 - y1) * mod_inverse(x2 - x1, p) % p
    x3 = (m ** 2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)


def is_generator(point, cyclic_group, p, order):
    if point == "O":
        return False
    seen = set()
    current = point
    for _ in range(order):
        seen.add(current)
        current = point_addition(current, point, a, b, p)
        if current == "O":
            break
    return len(seen) == order


def point_mulitplication(k, P, a, b, p):
    result = "O"
    addend = P

    while k > 0:
        if k % 2 == 1:
            result = point_addition(result, addend, a, b, p)
        addend = point_addition(addend, addend, a, b, p)
        k //= 2
    return result


def bsgs(G, P, a, b, p, n):
    print(f"Starting BSGS on curve: y^2 = x^3 + {a}x + {b} (mod {p})")
    print(f"Generator point: G = {G}")
    print(f"Target point: P = {P}")
    print(f"Group order (n): {n}")

    m = math.isqrt(n) + 1
    print(f"m (sqrt of order): {m}")

    baby_steps = {}
    current = "O"

    print("\nComputing baby steps:")
    for i in range(m):
        baby_steps[current] = i
        print(f"i = {i}, Point = {current}")
        current = point_addition(current, G, a, b, p)

    print("\nFinished computing baby steps.")
    print(f"Baby steps dictionary: {baby_steps}")

    mG = point_mulitplication(m, G, a, b, p)
    current = P
    print(f"\nComputed mG = {m} * G: {mG}")

    for j in range(m):
        print(f"j = {j}, Current Point = {current}")
        if current in baby_steps:
            i = baby_steps[current]
            print(f"Match found! i = {i}, j = {j}")
            print(f"Discrete logarithm k = j * m + i = {j} * {m} + {i}")
            return j * m + i
        current = point_addition(current, (-mG[0], -mG[1] % p), a, b, p)


def get_key(shared_point):
    x, _ = shared_point
    return sha256(str(x).encode()).hexdigest()


# y^3 = x^2 + ax + b (mod p)
p = 99901
a = 79
b = 109
k = 41

print(f"Curve: y^3 = x^2 + {a}x + {b} (mod {p})")
cyclic_group = find_cyclic_group(a, b, p)
print(f"Points on curve: {cyclic_group}")
order = len(cyclic_group)
print(f"Order of the elliptic curve group: {order}")

while True:
    G = random.choice(cyclic_group)
    if G != "O" and is_generator(G, cyclic_group, p, order):
        print(f"Random generator: {G}")
        break

priv_num1 = random.randint(0, order)
pub_num1 = point_mulitplication(priv_num1, G, a, b, p)
print(f"Person 1's public key: {pub_num1}")

priv_num2 = random.randint(0, order)
pub_num2 = point_mulitplication(priv_num2, G, a, b, p)
print(f"Person 2's public key: {pub_num2}")

shared_secret_1 = point_mulitplication(priv_num1, pub_num2, a, b, p)
shared_secret_2 = point_mulitplication(priv_num2, pub_num1, a, b, p)
print(f"Final calculated point: {shared_secret_1}")

shared_key = get_key(shared_secret_1)
print(f"Symmetric key: {shared_key}")

P = point_mulitplication(k, G, a, b, p)
print(f"Computed point P: {P}")

solved_k = bsgs(G, P, a, b, p, order)
print(f"Recovered k: {solved_k}")
