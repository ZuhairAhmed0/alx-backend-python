#!/usr/bin/env python3

import time
from random import uniform
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n  # Replace '1-concurrent_coroutines' with the actual filename

def measure_time(n, max_delay):
    start_time = time.time()
    run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    average_time = total_time / n

    return average_time
