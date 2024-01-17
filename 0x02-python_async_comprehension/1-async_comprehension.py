#!/usr/bin/env python3
"""Async Comprehensions"""

import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    """Collect 10 random numbers"""
    numbers = [i async for i in async_generator()]
    return numbers