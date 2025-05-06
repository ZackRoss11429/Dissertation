import time
import tracemalloc

from baby_step_giant_step import EC_BSGS


def benchmark(bsgs, *args):
    tracemalloc.start()
    start_time = time.time()

    result = bsgs(*args)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "result": result,
        "execution_time_sec": end_time - start_time,
        "peak_memory_kb": peak / 1024
    }

