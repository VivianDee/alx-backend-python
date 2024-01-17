#!/usr/bin/env python
"""Async Comprehensions"""


import asyncio
import random
from typing import List


async def async_generator() -> List[int]:
    """Coroutine will loop 10 times"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1.0)
