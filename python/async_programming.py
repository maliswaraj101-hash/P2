import time
import asyncio

# async def first():
#     print("Task 1 starting...")
#     await asyncio.sleep(2)
#     print("Task 1 ending...")

# def second():
#     print("Task 2 starting...")
#     time.sleep(2)
#     print("Task 2 ending...")
    

# asyncio.run(first())
# second()

# Task 1 starting...
# Task 1 ending...
# Task 2 starting...
# Task 2 ending...

# first is a coroutine , it runs in the event loop
# when it hits await , it wants to switch with other coroutine in the event loop while .sleep(2) keeps running in bg , but none others are scheduled



# async def first():
#     print("Task 1 starting...")
#     await asyncio.sleep(2)
#     print("Task 1 ending...")

# async def second():
#     print("Task 2 starting...")
#     time.sleep(2)
#     print("Task 2 ending...")
    

# asyncio.run(first())
# asyncio.run(second())

# Task 1 starting...
# Task 1 ending...
# Task 2 starting...
# Task 2 ending...

# same result even though both are async , WHY SO?
# its because they are not scheduled together , when the first is ran , it hits await , on hitting await it checks for other coroutine in evenLoop , but because second() is not scheduled yet , there is no other coroutine to run , therefore await task in first() finishes and then second() is run




# async def first():
#     print("Task 1 starting...")
#     await asyncio.sleep(2)
#     print("Task 1 ending...")

# async def second():
#     print("Task 2 starting...")
#     time.sleep(2)
#     print("Task 2 ending...")
    

# async def main():
#     await asyncio.gather(first() , second())

# asyncio.run(main())

# Task 1 starting...
# Task 2 starting...
# Task 2 ending...
# Task 1 ending...

# here time.sleep() blocks the whole main thread
# so whole main thread sleeps for 2 seconds then we print 
# Task 2 ending...




# async def first():
#     print("Task 1 starting...")
#     await asyncio.sleep(2)
#     print("Task 1 ending...")

# async def second():
#     print("Task 2 starting...")
#     await asyncio.sleep(2)
#     print("Task 2 ending...")
    

# async def main():
#     await first()
#     await second()

# asyncio.run(first())
# asyncio.run(second())

# both ways works , give same results.


# Task 1 starting...
# Task 1 ending...
# Task 2 starting...
# Task 2 ending...

# because both functions are not scheduled together , when first() hits await , second() is not scheduled yet in the event loop
# so on await in first() we cant switch because there is nothing present to switch

# if we do 
# async def main():
#     await asyncio.gather(first() , second())

# asyncio.run(main())

# Task 1 starting...
# Task 2 starting...
# Task 1 ending...
# Task 2 ending...

# this is perfect async code where we switch between coroutines.





# time.sleep() is a blocking call. It pauses the entire thread.
# In async Python (e.g., using asyncio), the event loop runs in a single thread by default.
# If you call time.sleep() inside an async function, you freeze the whole event loop, so:

#  Async = concurrency via scheduling


# THE THING IS 
# if we do await task()
# it does not mean we switch to other coroutine immediately
# AWAIT is necessarily not a switching point always
# important thing here is its internal working.
#  Concurrency happens only if there is await inside the coroutine
# await task()

# task():
# print("random")

# this wont cause switching.

# in above examples switching happened using asyncio.sleep(2) BECAUSE
# It registers a timer with the event loop and returns immediately
# this happens because of a thing called Future
# Future is kind of a placeholder which will be filled in the future.


# async def func():
#     print("awaiting func")

# async def compute1():
#     total = 0
#     for i in range(10**3):
#         total += i
#     print(total)
#     await func()
#     print("done1")

# async def compute2():
#     total = 0
#     for i in range(10**4):
#         total += i
#     print(total)


# async def first():
#     print("Task 1 starting...")
#     await compute1()
#     print("Task 1 ending...")

# async def second():
#     print("Task 2 starting...")
#     await compute2()
#     print("Task 2 ending...")
    

# async def main():
#     await asyncio.gather(first() , second())

# asyncio.run(main())

# Task 1 starting...
# 499500
# awaiting func
# done1
# Task 1 ending...
# Task 2 starting...
# 49995000
# Task 2 ending...

# here u might thing await func() will cause a switch , but it doesn't
# its because of the internal implementation , asyncio.sleep , registers a Future
# if we change the code something like this , just observe the output.



async def func():
    await asyncio.sleep(4)
    print("awaiting func")

async def compute1():
    total = 0
    for i in range(10**3):
        total += i
    print(total)
    await func()
    print("done1")

async def compute2():
    total = 0
    for i in range(10**4):
        total += i
    print(total)


async def first():
    print("Task 1 starting...")
    await compute1()
    print("Task 1 ending...")

async def second():
    print("Task 2 starting...")
    await compute2()
    print("Task 2 ending...")
    

async def main():
    await asyncio.gather(first() , second())

asyncio.run(main())


# Task 1 starting...
# 499500
# Task 2 starting...
# 49995000
# Task 2 ending...
# awaiting func
# done1
# Task 1 ending...

# here we got the switch , when we used asyncio.sleep()
# if we await [something setting Future] then we get switch

