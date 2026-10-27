import asyncio

async def work():
    print("Work started")
    await asyncio.sleep(2)
    print("Work finished")

async def main():
    task = asyncio.create_task(work())

    await asyncio.sleep(1)
    print("Now waiting for work")
    await task

asyncio.run(main())


# Work started
# Now waiting for work
# Work finished

# async def work():
#     print("Work started")
#     await asyncio.sleep(2)
#     print("Work finished")

# async def main():
#     await work()

#     print("Doing other stuff...")
#     await asyncio.sleep(1)

#     print("Now waiting for work")

# asyncio.run(main())


# Work started
# Work finished
# Doing other stuff...
# Now waiting for work

# In example 1:-
# create_task always schedules the task , it doesnt run it immediately
# we can run that coroutine only when we switch from current one
# so when we hit asyncio.sleep we switch and print ( work started) 
# we again hit asyncio.sleep and switch to main print(now waiting for work)
# and then when we await we go back and pritnt (work finished)


# In 2nd one:-
# as we only schedule main , work is inside main and even if we hit asncyio.sleep , 
# event loop has none other coroutine to switch to



# In example 1:
# create_task schedules the coroutine, and it runs when the event loop gets control (on await). When main awaits sleep, work starts. Both tasks then pause on their awaits, and the event loop resumes whichever becomes ready first.

# In example 2:
# only main is scheduled; work runs inside it. Even if we hit await, there is no other coroutine to switch to.