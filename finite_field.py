from utils import p, priv_key_ff_a, priv_key_ff_b
from sympy import factorint, isprime
import random


def find_generator():
    exp = (p - 1) // max(factorint(p - 1).keys())
    for i in range(1000):
        potential_generator = random.randint(2, p - 2)
        if pow(potential_generator, exp, p) != 1:
            return potential_generator


g = find_generator()
A_public_key = pow(g, priv_key_ff_a, p)
B_public_key = pow(g, priv_key_ff_b, p)
A_shared_key = pow(B_public_key, priv_key_ff_a, p)
B_shared_key = pow(A_public_key, priv_key_ff_b, p)
assert A_shared_key == B_shared_key

print(f"Generator chosen: {g}")
print(f"A's Public Key: {A_public_key}")
print(f"B's Public Key: {B_public_key}")
print(f"A and B's Shared Secret Key: {A_shared_key}")
