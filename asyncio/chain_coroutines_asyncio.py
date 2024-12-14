#!/usr/bin/env python3
# chained.py

import asyncio
import random
import time

# ANSI colors
c =( "\033[91m",    # red
     "\033[33m",    # yellow
     "\033[35m",   # Magenta
     "\033[37m",  # dark white
    )
async def part_1(n: int) -> str:
    i = random.randint(0, 10)
    print(c[0] + f"part1({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-1"
    print(c[0] + f"Returning part1({n}) == {result}.")
    return result

async def part_2(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(c[1] + f"part2{n, arg} sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-2 derived from {arg}"
    print(c[1] + f"Returning part2{n, arg} == {result}.")
    return result

async def chain(n: int) -> None:
    start = time.perf_counter()
    p1 = await part_1(n)
    p2 = await part_2(n, p1)
    end = time.perf_counter() - start
    # first p1, then p2, then chain fun only
    print(c[2] + f"-->Chained result{n} => {p2} (took {end:0.2f} seconds).")

async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))

if __name__ == "__main__":
    import sys
    random.seed(444)
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()
    asyncio.run(main(*args))
    end = time.perf_counter() - start
    print(c[3] + f"Program finished in {end:0.2f} seconds.")