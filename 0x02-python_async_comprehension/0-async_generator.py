#!/usr/bin/env python
"""Async Comprehensions"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Coroutine will loop 10 times"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
