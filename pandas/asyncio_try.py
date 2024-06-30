import aiohttp
import asyncio
import pandas as pd
import matplotlib.pyplot as plt
from async_time_logger import async_time_logger

@async_time_logger
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

@async_time_logger
async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/albums",
        "https://jsonplaceholder.typicode.com/photos",
        "https://jsonplaceholder.typicode.com/todos"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

results = asyncio.run(main())

# Example processing of results with pandas
data_lengths = [len(result) for result in results]
df = pd.DataFrame({
    'URL': ["Posts", "Comments", "Albums", "Photos", "Todos"],
    'Length': data_lengths
})

# Plotting the data
df.plot(kind='bar', x='URL', y='Length', legend=False)
plt.title('Length of data fetched from URLs')
plt.ylabel('Length')
plt.show()
