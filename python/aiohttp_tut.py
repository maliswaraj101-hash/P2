# aiohttp offers pure async api calls
# for async its better than requests and httpx

# GIL -> Global Interpreter Lock is very important in python.


# basic get request
import aiohttp
import asyncio

async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get("/url") as response:
            data = await response.json()
            print(data)

asyncio.run(fetch())

# ClientSession() → manages connections



# MULTIPLE REQUESTS

import aiohttp
import asyncio

urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3"
]

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        print(results)

asyncio.run(main())


# POST REQUEST
async def post_data():
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://jsonplaceholder.typicode.com/posts",
            json={"title": "test", "body": "hello"}
        ) as response:
            data = await response.json()
            print(data)

asyncio.run(post_data())


# Headers & Params
async def fetch_with_headers():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://api.github.com",
            headers={"User-Agent": "my-app"},
            params={"q": "python"}
        ) as response:
            print(await response.text())


# TIMEOUT
# request should finish within particular seconds

# import aiohttp

# timeout = aiohttp.ClientTimeout(total=5)

# async with aiohttp.ClientSession(timeout=timeout) as session:
#     async with session.get("https://example.com") as res:
#         print(await res.text())