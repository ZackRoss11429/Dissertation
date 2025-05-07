from elliptic_curves import point_multiply
from elliptic_curves import point_addition

from utils import p
from utils import coefficient_a as a
from utils import coefficient_b as b

import math
from sympy import mod_inverse


# Q = kP
def EC_BSGS(cyclic_group, P, Q):
    n = len(cyclic_group)

    print(f"Starting BSGS on curve: y^2 = x^3 + {a}x + {b} (mod {p})")
    print(f"Generator: {P}")
    print(f"Order of group: {n}")

    m = math.ceil(n ** 0.5)
    baby_steps = {}
    current = "O"
    # calculates m which is the square root of the order of the group

    for j in range(m):
        if j % (m // 10) == 0:
            print(f"Baby Step Progress: {int(j / m * 100)}%")
        current = point_multiply(j, P)
        baby_steps[current] = j
        # every iteration, it point multiplies the generator by j and logs it as baby steps

    # This calculates the
    mP = point_multiply(m, P)
    mP_neg = (mP[0], -mP[1])


    current = Q
    for i in range(m):
        if i % (m // 10) == 0:
            print(f"Giant Step Progress: {int(i / m * 100)}%")
        if current in baby_steps:
            return i * m + baby_steps[current]
        current = point_addition(current, mP_neg)


def FF_BSGS(h, g):
    print(f"Starting BSGS on GF({p})")
    print(f"Generator: {g}")
    print(f"Order of group: {p - 1}")

    # how many steps
    m = math.ceil(p ** 0.5)

    baby_steps = {}

    # solving for a^mi mod p for each step
    for j in range(m):
        if j % (m // 10) == 0:
            print(f"Baby Step Progress: {int(j / m * 100)}%")
        baby_steps[(g ** j) % p] = j

    for i in range(m):
        if i % (m // 10) == 0:
            print(f"Giant Step Progress: {int(i / m * 100)}%")
        giant_step = (h * mod_inverse(pow(g, i*m, p), p)) % p

        if giant_step in baby_steps:
            j = baby_steps[giant_step]
            return (i * m + j) % p





