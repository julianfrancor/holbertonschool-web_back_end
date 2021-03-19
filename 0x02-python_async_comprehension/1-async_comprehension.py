#!/usr/bin/env python3
"""Define a asynchronous coroutine - async_comprehension"""


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an async comprehensing"""
    return [num async for num in async_generator()]
