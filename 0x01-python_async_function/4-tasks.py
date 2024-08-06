#!/usr/bin/env python3
"""module"""
import asyncio
import random
from typing import List
import heapq
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Waits for n coroutines to finish"""
    tasks = []
    delays = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)
    delays = await asyncio.gather(*tasks)
    heapq.heapify(delays)
    sorted_delays = []
    for _ in range(len(delays)):
        sorted_delays.append(heapq.heappop(delays))
    return sorted_delays
