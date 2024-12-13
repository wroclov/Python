#!/usr/bin/env python3


import asyncio
import time

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())


def count_sync():
    print("One")
    time.sleep(1)
    print("Two")

def main_sync():
    for _ in range(3):
        count_sync()

if __name__ == "__main__":
    ## async
    t1 = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - t1
    print(f"{main} asynchronously executed in {elapsed:0.2f} seconds.")

    ### synchronous version
    t2 = time.perf_counter()
    main_sync()
    elapsed_sync = time.perf_counter() - t2
    print(f"{main_sync} synchronous version executed in {elapsed_sync:0.2f} seconds.")
