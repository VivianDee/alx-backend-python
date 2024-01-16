#!/usr.bin/env python3
"""
   Asynchronous coroutine
"""

import random
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """Spawns wait_random n times with the specified max_delay"""
    my_list = []
    for i in range(n):
        my_list.append(wait_random(max_delay))

    delay = await asyncio.gather(*my_list)
    return delay
