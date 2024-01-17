#!/usr/bin/env python3
"""Async Comprehensions"""

import asyncio
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> int:
    """Measure the total runtime"""
    start = time()
    results = await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end = time() - start
    return end
