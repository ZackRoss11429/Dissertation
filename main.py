from utils import p
from elliptic_curves import ecc_parameters
from elliptic_curves import point_multiply
from finite_field import ff_parameters
from elliptic_curves import ecc_parameters, point_multiply
from baby_step_giant_step import FF_BSGS, EC_BSGS
from benchmark import benchmark


print("Initialising Parameters:")
ff_params = ff_parameters()
ecc_params = ecc_parameters()

FF_g = ff_params["g"]
FF_shared_key = ff_params["A_shared"]

EC_g = ecc_params["g"]
EC_shared_key = ecc_params["A_shared"]
cyclic_group = ecc_params["group"]

print("\nRunning Baby-Step Giant-Step Algorithm on Finite Field")
ff_benchmark = benchmark(FF_BSGS, FF_shared_key, FF_g)
print(f"Discrete Logarithm x = {ff_benchmark['result']}")
print(f"Execution Time: {ff_benchmark['execution_time_sec']} sec")
print(f"Peak Memory Usage: {ff_benchmark['peak_memory_kb']} KB")

print("\nRunning Baby-Step Giant-Step Algorithm on Elliptic Curve")
ecc_benchmark = benchmark(EC_BSGS, cyclic_group, EC_g, EC_shared_key)
print(f"Discrete Logarithm k = {ecc_benchmark['result']}")
print(f"Execution Time: {ecc_benchmark['execution_time_sec']} sec")
print(f"Peak Memory Usage: {ecc_benchmark['peak_memory_kb']} KB")




# print("\n ======== FINITE FIELD DIFFIE-HELLMAN =========")
# print(f"Execution Time: {ff_result['execution_time_sec']:.6f} seconds")
# print(f"Peak Memory: {ff_result['peak_memory_kb']:.2f} KB")
#
# print(f"Generator chosen: {ff['g']}")
#
# print(f"A's Public Key: {ff['A_public']}")
# print(f"B's Public Key: {ff['B_public']}")
#
# print(f"A and B's Shared Secret Key: {ff['A_shared']}")
#
#
# ecc_result = benchmark(FF_BSGS, ff_params['A_shared'], ff_params['g'])
# ecc = ecc_result['result']
# print("\n ======== ELLIPTIC CURVE DIFFIE-HELLMAN =========")
# print(f"Execution Time: {ecc_result['execution_time_sec']:.6f} seconds")
# print(f"Peak Memory: {ecc_result['peak_memory_kb']:.2f} KB")
# print(f"Order of Cyclic Group: {ecc['order']}")
# print(f"Generator chosen: {ecc['g']}")
#
# print(f"\nA's Private Key: {ecc['a']}")
# print(f"B's Private Key: {ecc['b']}")
#
# print(f"\nA's Public Key: {ecc['A_public']}")
# print(f"B's Public Key: {ecc['B_public']}")
# print(f"Shared Secret Key of A and B: {ecc['A_shared']}")
