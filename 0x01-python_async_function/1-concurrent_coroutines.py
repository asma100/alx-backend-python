#!/usr/bin/env python3
"""module"""
import asyncio
import random
from typing import List
import heapq
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Waits for n coroutines to finish"""
    tasks = []
    delays = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    delays = await asyncio.gather(*tasks)
    heapq.heapify(delays)
    sorted_delays = []
    for _ in range(len(delays)):
        sorted_delays.append(heapq.heappop(delays))
    return sorted_delays
