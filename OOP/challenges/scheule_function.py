import sched
from typing import Callable
import time
import winsound
import threading

# pygame could be used to import music files
# import pygame
def beep_sound(freq, duration):
    print("Beep_started:", time.asctime(time.localtime(time.time())))
    winsound.Beep(freq, duration)
    print("Beep_finished",time.asctime(time.localtime(time.time())))

def schedule_function(seconds: int, func: Callable, *args, **kwargs):
    """
    Waits for a given number of seconds before executing the provided function.

    Parameters:
    seconds (int): The time to wait before executing the function.
    func (Callable): The function to execute after the wait.
    *args: Arguments to pass to the function.
    **kwargs: Keyword arguments to pass to the function.

    Returns:
    The return value of the executed function.
    """
    time.sleep(seconds)
    beep_thread = threading.Thread(target=beep_sound, args=(1000,100))
    beep_thread.start()

    #beep_thread.join()
    return func(*args, **kwargs)

# second approach
def sched_fun(event_time, function, *args):
    s = sched.scheduler(time.time,time.sleep)
    s.enterabs(event_time, 1, function, argument=args)
    print(f"{function.__name__}() scheduled for {time.asctime(time.localtime(event_time))}")
    s.run()


# Example usage
def example_function(msg):
    print(msg)


# Wait n seconds, then execute the example function
schedule_function(2, example_function, "Hello after 2 seconds!")
schedule_function(1, example_function, "Ohdsjakhdkas")
schedule_function(1, print, "hh")
schedule_function(1, print, "hh","ooo")


sched_fun(time.time()+1, print,"Hello", " bee", "more")