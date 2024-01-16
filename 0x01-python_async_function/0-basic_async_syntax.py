#!/usr/bin/env python3
"""
   Asynchronous coroutine
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """Waits for a random delay between 0 and max_delay"""
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
