from utils import p, k_value_ec_a, k_value_ec_b
from utils import coefficient_a as a
from utils import coefficient_b as b
from sympy import factorint, isprime, mod_inverse
import random


# This function finds the cyclic subgroup from all possible integers between 1 and p-1
def find_cyclic_group():
    cyclic_group = []
    for x in range(0, p - 1):
        rhs = (x ** 3 + a * x + b) % p  # substitutes current x value to get two y values

        if pow(rhs, (p - 1) // 2, p) == 1:
            # Due to prime number being congruent to 3 mod 4, Euler's criterion is used to
            # determine if y^2 is a quadratic residue

            y = pow(rhs, (p + 1) // 4, p)  # finds positive y value with Euler's criterion
            cyclic_group.append((x, y))  # appends positive y^2 root to cyclic group
            cyclic_group.append((x, -y % p))  # appends negative y^2 root to cyclic group

    cyclic_group.append("O")
    return cyclic_group


# P + Q = (r')^-1
def point_addition(P, Q):
    if P == "O":
        return Q

    if Q == "O":
        return P

    x1, y1 = P
    x2, y2 = Q

    if P != Q:
        m = (((y2 - y1) % p) * mod_inverse((x2-x1) % p, p)) % p

        x3 = (m**2 - x1 - x2) % p
        y3 = (m * (x1 - x3) - y1) % p
        return x3, y3

    if P == Q:
        m = (y2-y1)/(x2-)
