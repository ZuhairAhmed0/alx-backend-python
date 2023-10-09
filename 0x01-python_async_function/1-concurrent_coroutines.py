#!/usr/bin/env python3
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n, max_delay):
    """
        Spawns n wait_random() coroutines with the specified max_delay
        and returns a list of all the delays
        in ascending order without using sort() because of concurrency.
    """
    delays = []
    tasks = []
    for i in range(n):
        delay = random.uniform(0, max_delay)
        delays.append(delay)
        tasks.append(asyncio.create_task(wait_random(delay)))

    await asyncio.gather(*tasks)
    return sorted(delays)
