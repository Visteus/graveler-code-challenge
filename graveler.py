import random
import time
from itertools import repeat
from multiprocessing import Process, Pool, TimeoutError

runs = 1000000000

def simulate_turns(ignored):
    return [random.randrange(0,3) for _ in range(0,231)].count(0)

if __name__ == '__main__':
    with Pool(processes=6) as pool:    # Max processes somewhat dependent on your machine/hardware.
        try:
            start_time = time.time()
            results2 = pool.map(simulate_turns, range(runs))
            run_time = time.time() - start_time
            print(f"Maximum in '{runs}' runs: {max(results2)}")
            print(f"\tIn only {run_time} seconds")
        except TimeoutError:
            print("TimeoutError")
