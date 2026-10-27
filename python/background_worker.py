import asyncio
import time

def background_worker_fn():
    while True:
        print("Logging")
        time.sleep(1)

async def print_fetch():
    print("fetch")

async def random():
    await asyncio.gather(
    asyncio.to_thread(background_worker_fn),
    print_fetch()
    )



asyncio.run(random())


# gather schedules BOTH tasks

# to_thread(blocking_task):

# immediately offloads work to a thread

# hits await → yields control

# async_task():

# starts running in event loop