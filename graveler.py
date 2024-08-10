import random
import time
from itertools import repeat
from multiprocessing import Process, Pool, TimeoutError

runs = 1000000

def simulate(ignored):
    roll_counts = [0,0,0,0]
    for i in repeat(None, 231):
        roll = random.randrange(0,3) # equivalent to 4-sided die
        roll_counts[roll] += 1
    return roll_counts[0]



if __name__ == '__main__':
    start_time = time.time()
    with Pool(processes=60) as pool:    # Max processes somewhat dependent on your machine/hardware. 
        results = []
        try:
            results = pool.map(simulate, range(1,runs))
            run_time = time.time() - start_time
            print(f'Maximum in {runs}: {max(results)}')
            print(f"We did it! In only {run_time} seconds")
        except TimeoutError:
            print("TimeoutError")
