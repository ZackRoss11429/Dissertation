from finite_field import A_shared_key as FF_shared_key
from finite_field import g as FF_g

from elliptic_curves import A_shared_key as EC_shared_key
from elliptic_curves import g as EC_g
from elliptic_curves import cyclic_group
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
    print(f"Generator: {EC_g}")
    print(f"Order of group: {n}")

    m = math.ceil(n**0.5)
    baby_steps = {}
    current = "O"

    for i in range(m):
        current = point_multiply(i, P)
        baby_steps[current] = i

    mP = point_multiply(m, P)
    mP_neg = (mP[0], -mP[1])

    current = Q
    for j in range(m):
        if current in baby_steps:
            return j * m + baby_steps[current]
        current = point_addition(current, mP_neg)


k = EC_BSGS(cyclic_group, EC_g, EC_shared_key)
print(f"Discrete Logarithm Found: k = {k}")
print(f"Reconstructed Shared Secret: {point_multiply(k, EC_g)}")




