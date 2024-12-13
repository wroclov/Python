#!/usr/bin/env python3


import asyncio
import random

# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
    "\033[33m",  # Yellow
)


async def makerandom(idx: int, threshold: int = 6) -> int:
    print(c[idx + 1] + f"Initiated makerandom({idx}).")
    i = random.randint(0, 10)
    while i <= threshold:
        print(c[idx + 1] + f"makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
    return i

async def main():
    # several makerandom couroutines executed concurrently with various thresholds
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(4)))
    return res

if __name__ == "__main__":
    #random.seed(444)
    r1, r2, r3, r4 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}, r4: {r4}")
