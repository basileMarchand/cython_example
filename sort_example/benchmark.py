import time
import numpy as np 
import sortcpp

def performance(f, args, repeat=10):
    start = time.perf_counter()
    for _ in range(repeat):
        f(*args)
    stop = time.perf_counter()
    print(f"{f.__module__}::{f.__name__} mean time ({repeat} run): {(stop-start)/repeat} s")


l = np.random.rand(1000000).tolist()

def python_sort(l: list):
    return sorted(l)

repeat = 10
performance(python_sort, (l, ), repeat )
performance(sortcpp.cppSorter, (l, ), repeat )
