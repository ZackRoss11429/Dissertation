from utils import p, k_value_ec_a, k_value_ec_b
from utils import coefficient_a as a
from utils import coefficient_b as b
from sympy import factorint, mod_inverse
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
    x1, y1 = P
    x2, y2 = Q

    # if P = O, then P + Q = Q
    if P == "O":
        return Q

    # if Q = O, then P + Q = P
    if Q == "O":
        return P

    # P + (-P) = O
    if x1 == x2 and y1 != y2:
        return "O"

    # if P = Q, and y1 != 0
    if P == Q and y1 != 0:
        m = ((3 * x1 ** 2 + a) * mod_inverse(2 * y1, p)) % p
        x3 = (m ** 2 - 2 * x1) % p
        y3 = (m * (x1 - x3) - y1) % p

    # if P != Q --> (x1 != x2)
    else:
        m = (y2 - y1) * mod_inverse(x2 - x1, p) % p
        x3 = (m ** 2 - x1 - x2) % p
        y3 = (m * (x1 - x3) - y1) % p

    # a / b mod p = a * b^-1 mod p

    return x3, y3


def point_multiply(k, P):
    # multiplying k by P as is can be inefficient
    # instead, using previously calculated multiplications of P is more efficient
    # The windowed method: window size w is chosen to calculate 2^w values of dP
    # for d = 0, 1, 2, ... 2^w -1.
    # d = d0 + 2^w * d1 + 2^2w * d2 + ... 2^mw * dm

    w = 8  # larger window size means more computations but fewer operations
    precomputed_values = [P]
    result = None

    for i in range(2, 2 ** w):  # compute all values from P to (2^w -1) * P
        precomputed_values.append(point_addition(precomputed_values[-1], P))

    # convert k-value to binary and store in a list in chunks of size w
    # value should be divisible by w, if not then it is padded with 0s
    k_binary_bin = format(k, "08b")
    while len(k_binary_bin) % w != 0:
        k_binary_bin = '0' + k_binary_bin

    windows = [int(k_binary_bin[i: i + w], 2) for i in range(0, len(k_binary_bin), w)]

    # each window is iterated over and checked if the result has partially been built
    # result is doubled w times, ie 2^w times.
    for window in windows:
        if result is not None:
            for i in range(w):
                result = point_addition(result, result)

        # if the window is not zero, the corresponding precomputed point is added
        if window != 0:
            added_point = precomputed_values[window - 1]
            if result is None:
                result = added_point

            else:
                result = point_addition(result, added_point)

    return result


def is_generator(candidate_g, cyclic_group):
    n = len(cyclic_group)
    q = max(factorint(n).keys())
    # takes largest prime factor of cyclic group order n

    # cofactor h is calculated
    h = n // q

    # the potential candidate is multiplied by cofactor h
    # if it equals the identity point then it's not a generator
    if point_multiply(h, candidate_g) == (None, None):
        return False

    return True


# This instantiates the cyclic group
# It picks a generator that is valid according to the is_generator function, ensuring it is also not the identity point
# It generates each public key by point multiplying each party's private key with the generator
# Then the final private key is generated through each party point multiplying the
# others public key with their private key
def ecc_parameters():
    print("=========== ELLIPTIC CURVE PARAMETERS: ===========")
    print(f"A's Private Key: {k_value_ec_a}")
    print(f"B's Private Key: {k_value_ec_b}")
    cyclic_group = find_cyclic_group()
    print(f"Cyclic group generated.")

    while True:
        g = random.choice(cyclic_group)
        if is_generator(g, cyclic_group) and g != "O":
            print(f"Generator Chosen: {g}")
            break

    A_public_key = point_multiply(k_value_ec_a, g)
    B_public_key = point_multiply(k_value_ec_b, g)
    print(f"A's Public Key: {A_public_key}")
    print(f"B's Public Key: {B_public_key}")

    A_shared_key = point_multiply(k_value_ec_a, B_public_key)
    B_shared_key = point_multiply(k_value_ec_b, A_public_key)
    print(f"Shared Secret Key: {A_shared_key}")
    print("=================================")

    return {
        "p": p,
        "a": a,
        "b": b,
        "group": cyclic_group,
        "order": len(cyclic_group),
        "g": g,
        "A_private": k_value_ec_a,
        "B_private": k_value_ec_b,
        "A_public": A_public_key,
        "B_public": B_public_key,
        "A_shared": A_shared_key,
        "B_shared": B_shared_key
    }




