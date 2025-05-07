from utils import p, priv_key_ff_a, priv_key_ff_b
from sympy import factorint, isprime
import random


# This function randomly picks a generator by picking some number below p-2
# and checking if raising it to the power of q mod p is not 1, where q is the largest prime factor of p-1.

def find_generator():
    exp = (p - 1) // max(factorint(p - 1).keys())
    for i in range(1000):
        potential_generator = random.randint(2, p - 2)
        if pow(potential_generator, exp, p) != 1:
            return potential_generator


# This instantiates a generator value, generates each public value with g^a mod p or g^b mod p
# Then a shared key is generated via: g^ab mod p
def ff_parameters():
    print("=========== FINITE FIELD PARAMETERS: ===========")
    print(f"A's Private Key: {priv_key_ff_a}")
    print(f"B's Private Key: {priv_key_ff_b}")
    g = find_generator()
    print(f"Generator Chosen: {g}")
    A_public_key = pow(g, priv_key_ff_a, p)
    B_public_key = pow(g, priv_key_ff_b, p)
    print(f"A's Public Key: {A_public_key}")
    print(f"B's Public Key: {B_public_key}")
    A_shared_key = pow(B_public_key, priv_key_ff_a, p)
    B_shared_key = pow(A_public_key, priv_key_ff_b, p)
    print(f"Shared Secret Key: {A_shared_key}")
    print("=================================")

    return {
        "p": p,
        "g": g,
        "A_private": priv_key_ff_a,
        "B_private": priv_key_ff_b,
        "A_public": A_public_key,
        "B_public": B_public_key,
        "A_shared": A_shared_key,
        "B_shared": B_shared_key
    }
