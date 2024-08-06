#!/usr/bin/env python3
"""module"""
import asyncio
import random


async def async_generator() -> float:
    """Waits for 1s then ggives random number """
    for _ in range(10):
        await asyncio.sleep(1)
        r_number = random.uniform(0, 10)
        yield r_number
