#!/usr/bin/env python3
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n, max_delay):
	"""
		The code is nearly identical to wait_n except task_wait_random is being called.
	"""
	tasks = []
	for _ in range(n):
		tasks.append(task_wait_random(max_delay))

	return await asyncio.gather(*tasks)

