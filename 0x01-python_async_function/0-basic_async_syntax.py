import asyncio
import random

async def wait_random(max_delay=10):
    """Waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

    Args:
        max_delay (int, optional): The upper bound of the random delay in seconds. Defaults to 10.

    Returns:
        float: The random delay in seconds.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
