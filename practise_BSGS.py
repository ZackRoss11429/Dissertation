import math

a = 2
g = 2
p = 10007
equation = "a^x = g mod p"

m = math.ceil(math.sqrt(p))

baby_steps = {}

print("Calculating Baby Step")
for j in range(0, m):
    value = pow(a, m*j, p)
    baby_steps[value] = j
    print(f"Baby Step {j}: a^({j}*{m}) mod {p} = {value}")

print("Calculating Giant Step")
for i in range(0, m):
    giant_step_value = (g * pow(pow(a, i, p), -1, p)) % p
    print(f"Giant step {i}: g * a^(-{i}) mod {p} = {giant_step_value}")

    if giant_step_value in baby_steps:
        j = baby_steps[giant_step_value]
        print(f"Collision found:")
        print(f"Baby step j = {j}: a^{j} mod {p} = {giant_step_value}")
        print(f"Giant step i = {i}: g * a^(-{i}) mod {p} = {giant_step_value}")

        x = i * m + j % p
        print(f"Solution: x = {x}")
        break
