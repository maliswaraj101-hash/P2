import threading
import time
from threading import Thread


def take_orders():
    for i in range(1 , 4):
        print(f"Taking order {i}")
        time.sleep(1)

def brewing():
    for i in range(1 , 4):
        print(f"Brewing {i}...")
        time.sleep(2)

# creating Threads

orders = threading.Thread(target=take_orders)
brews = threading.Thread(target=brewing)

# one thread for each task

orders.start()
brews.start()

# Taking order 1
# Brewing 1...
# Taking order 2
# Brewing 2...
# Taking order 3
# Brewing 3...

# both start almost instantaneously
# start() = “Hey, begin this task in the background”
# so thread A does some work , then it hits sleep , so CPU releases it
# thread B does some work and then hits sleep , then CPU releases it and takes thread A to continue
# this is concurrency

orders.join()
brews.join()

# Both threads start running in the background
# But the main program does NOT wait

# 👉 The main thread just continues and can finish early.

# ⚠️ What can go wrong?

# If your program ends while threads are still running:

# Threads may get cut off abruptly
# You may see incomplete output
# Or inconsistent behavior in real applications
# 🔍 What join() does
# orders.join()
# brews.join()

# 👉 This tells the main thread:

# “Wait here until this thread finishes.”

# ⚡ Flow WITH join()
# Main thread:
#    start orders
#    start brews
#    wait for orders to finish
#    wait for brews to finish
#    then exit
# ❌ WITHOUT join()
# Main thread:
#    start orders
#    start brews
#    exit (even if threads still running!)