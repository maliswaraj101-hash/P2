from multiprocessing import Process , Queue

def brew(queue):
    queue.put("Coffee is ready")

if __name__ == "__main__":
    queue = Queue()

    p = Process(target=brew(queue))

    p.start()
    p.join()

    print(f"{queue.get()}")

# threads share the same memory as the spawn from the same process
# but between 2 processes have their own memory , so we can use something like queue to share the data