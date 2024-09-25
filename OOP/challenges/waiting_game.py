
import random
import time

def waiting_game():
    target = random.randrange(2, 4)
    print(f"Your target time is {target} seconds.")
    input(f"--- Please Enter to begin a game ---")

    start_time = time.perf_counter()

    input(f"--- Please Enter again after {target} seconds...")
    elapsed = (time.perf_counter() - start_time)
    expected = elapsed - target

    diff = "fast" if expected < 0 else "slow"

    print(f"Elapsed time: {elapsed:.6f} seconds \n({abs(expected):.6f} seconds too {diff})")

waiting_game()
