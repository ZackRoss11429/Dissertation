import random


# include constants for both files
# prime number generator
# timer wrapper functions


def private_key_generator(p):
    bit_length = p.bit_length()
    min_val = 2 ** (bit_length - 2)
    max_val = p - 2
    return random.randint(min_val, max_val)


# prime number for both applications

# p = 2593697
# p = 4294967291  # (=~ 30-bit
# p = 140737488355327  # (=~ 2^47
# p = 7519907

#p = 62_047  # (16 bit)
#p = 690_127 #(20-bit)
#p = 10_391_999 #(24-bit)
p = 220_830_871 #(28-bit)
# p = 3_726_267_107 #(32-bit)


# coefficients for ECC
coefficient_a = 2
coefficient_b = 2

# private keys for person A and B -- Finite Fields
priv_key_ff_a = private_key_generator(p)
priv_key_ff_b = private_key_generator(p)

# private keys for person A and B -- ECC
k_value_ec_a = private_key_generator(p)
k_value_ec_b = private_key_generator(p)
