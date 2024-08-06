#!/usr/bin/env python3
"""Module to collect random numbers using a regular for loop"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using a regular for loop"""
    result = []
    async for num in async_generator():
        result.append(num)
    return result
