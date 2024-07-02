import asyncio
import aiohttp
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time

# Decorator to measure time taken by a function
def timeit(func):
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken by {func.__name__}: {end_time - start_time:.2f} seconds")
        return result, end_time - start_time  # Return result and time taken
    return wrapper

# Simulate fetching data from an API
@timeit
async def fetch_data(session, url):
    async with session.get(url) as response:
        data = await response.json()
        return data

# Asynchronous data fetching
@timeit
async def fetch_all_data(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        return await asyncio.gather(*tasks)

# Process the data
def process_data(data):
    # Example transformation for demonstration
    if isinstance(data, dict):
        if 'userId' in data and 'id' in data:  # Example of possible numeric fields
            # Simulate multiple points for each user
            processed_data = {
                'id': [data['id'] + i for i in range(5)],
                'userId': [data['userId']] * 5,
                'value': [(data['id'] + i) * np.random.rand() for i in range(5)]  # Create multiple 'value' points
            }
            df = pd.DataFrame(processed_data)
            return df
        else:
            raise KeyError("Expected keys are not in the data")
    else:
        raise ValueError("Expected a dictionary format for the data")

# Plot the data
@timeit
async def plot_data(urls):
    plt.figure(figsize=(10, 5))
    plt.title('Asynchronous Data Fetching and Plotting')
    plt.xlabel('ID')
    plt.ylabel('Value')
    plt.grid(True)

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        for task in asyncio.as_completed(tasks):
            data, time_taken = await task
            df = process_data(data)
            label = f"User {df['userId'][0]} (Time: {time_taken:.2f} sec)"
            plt.plot(df['id'], df['value'], marker='o', label=label)
            plt.legend()
            plt.pause(1)  # Pause to show the plot updating
    plt.show()

# Main function
async def main(urls):
    try:
        await plot_data(urls)
    except Exception as e:
        print(f"An error occurred: {e}")

# Simulated URLs for fetching data
urls = [
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/2',
    'https://jsonplaceholder.typicode.com/posts/3'
]

# Run the main function
asyncio.run(main(urls))
