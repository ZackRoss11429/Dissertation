a = int(input("Input integer: "))
p = int(input("Input a modulus that is prime: "))
r = a % p
a_inv = (r**(p-2)) % p

super_s = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
p_digits = []
for digit in str(p):
    p_digits.append(super_s[int(digit)])

print(a, "mod", p, "≡", r, "mod", p)
print("---------------")
print(r, "⁻¹ mod", p)
print("r⁻¹ ≡ rᴾ⁻² mod p")
print(r, "⁻¹" "≡", r, "".join([digit for digit in p_digits]), "⁻² mod", p)
print("=", a_inv)
