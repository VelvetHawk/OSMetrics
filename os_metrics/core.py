#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module extracts OS metrics and streams them asynchronously
to apache kafka in 1 second intervals."""

import platform

import requests
import requests_async
import psutil
import asyncio


@asyncio.coroutine
async def get_cpu_metrics() -> list:
	"""
	Gets the utilisation percentage and temperature for each CPU
	:return:
	"""
	pass


async def get_memory_metrics() -> list:
	"""
	Gets the utilisation percentage for both virtual memory and
	swap space on the target OS
	:return:
	"""
	pass


async def stream_metrics():
	"""
	Send data to apache kafka instance in 1 second intervals
	:return:
	"""
	while True:
		await asyncio.sleep(1)


# Get basic OS information
os_name = platform.system()
os_release = platform.release()
os_architecture = "%s (%s)" % (platform.architecture()[0], platform.machine())
os_version = platform.version()

# Get information about processor and memory
processor = platform.processor()
cpu_physical_cores = psutil.cpu_count(logical=False)
cpu_logical_cores = psutil.cpu_count(logical=True)
total_ram = psutil.virtual_memory().total
total_swap_space = psutil.swap_memory().total


# Collect and stream data
loop = asyncio.get_event_loop()
try:
	asyncio.ensure_future(stream_metrics())
	loop.run_forever()
except KeyboardInterrupt as interrupt:
	# Allow keyboard inturrupts to stop loop
	loop.stop()
finally:
	# End loop and close all connections
	loop.close()
