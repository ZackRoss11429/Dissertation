import json
from utils import p, priv_key_a, priv_key_b
from elliptic_curves import ecc_parameters
from elliptic_curves import point_multiply
from finite_field import ff_parameters
from elliptic_curves import ecc_parameters, point_multiply
from baby_step_giant_step import FF_BSGS, EC_BSGS
from benchmark import benchmark

all_results = {}

# Main loop for establishing parameters, creating shared keys, and benchmarking Baby-Step Giant-Step's effort to
# find the discrete logarithm / discrete scalar value
for i in range(30):
    print(f"Iteration: {i}")
    print("Initialising Parameters:")
    ff_params = ff_parameters()
    ecc_params = ecc_parameters()
    # This runs the finite field and ecc program to create shared keys and return its results as dictionaries

    FF_g = ff_params["g"]
    FF_shared_key = ff_params["A_shared"]

    EC_g = ecc_params["g"]
    EC_shared_key = ecc_params["A_shared"]
    cyclic_group = ecc_params["group"]

    # This section benchmarks the Baby-Step Giant-Step algorithms for each implementation, passing through each
    # function, and its arguments
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

    # These are the results found that get exported to a json file for comparison
    results = {
        "iteration": i,
        "prime": p,
        "a_private_key": priv_key_a,
        "b_private_key": priv_key_b,
        "ff_generator": FF_g,
        "ff_shared": FF_shared_key,
        "ff_exec_time (sec)": ff_benchmark['execution_time_sec'],
        "ff_peak_memory (KB)": ff_benchmark['peak_memory_kb'],
        "ecc_generator": EC_g,
        "ecc_shared": EC_shared_key,
        "ecc_exec_time (sec)": ecc_benchmark['execution_time_sec'],
        "ecc_peak_memory (KB)": ecc_benchmark['peak_memory_kb']
    }

    all_results[f"Iteration {i}"] = results

    with open('results2.json', 'w') as f:
        json.dump(all_results, f, indent=4)
