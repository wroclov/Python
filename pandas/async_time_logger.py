import time
import logging

logging.basicConfig(level=logging.INFO)

def async_time_logger(func):
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Execution time for {func.__name__} with args {args} : {execution_time} seconds")
        return result
    return wrapper
