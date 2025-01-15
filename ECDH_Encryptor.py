import random
import math
from sympy import isprime, mod_inverse, legendre_symbol

# point P, point Q, y^2 = x^3 + ax + b (mod p)

a = 2
b = 2
p = 10007

P = (2, 10**(1/3))
Q = (3, 35**(1/3))


def point_addition(P, Q, a, b, p):
    if P == "O":
        return Q
    if Q == "O":
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and y1 != y2:
        return "O"

    s = (y2 - y1) / (x2 - x1) % p
    Rx = s ** 2 - x1 - x2 % p
    Ry = s * (x1 - x2) - y1 % p
    return (Rx, Ry)


def point_mulitplication():
    pass


def point_inverse():
    pass


print(point_addition(P, Q, a, b, p))
