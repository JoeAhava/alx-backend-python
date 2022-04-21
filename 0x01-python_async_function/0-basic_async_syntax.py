#!/usr/bin/env python3
'''
Async Python Basic syntax
'''


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''
    wait randomly between 0 and max_delay
    '''
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == '__main__':
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
