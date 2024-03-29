#!/usr/bin/env python3
"""
   Asynchronous coroutine
"""


import asyncio
import random
from time import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:

    """Measures the total execution time for wait_n"""
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time() - start
    return end / n
