import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    The coroutine will collect 10 random numbers using
    an async comprehension over async_generator,
    then return the 10 random numbers.
    """
    values = [x async for x in async_generator()]
    return values
