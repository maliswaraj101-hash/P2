from multiprocessing import Process
import time
import threading

def cpu_heavy():
    print("Task Started")
    cnt = 0
    for i in range(10**7):
        cnt += i
    print("Task Done") 

start = time.time()

threads = [threading.Thread(target = cpu_heavy) for _ in range(2)]

[t.start() for t in threads]
[t.join() for t in threads]

end = time.time()

print(f"Time taken {end - start}")

# Task Started
# Task Started
# Task Done
# Task Done
# Time taken 1.0418052673339844

# NOW LETS TRY WITH PROCESSES , i.e. , multiprocessing



# def cpu_heavy():
#     print("Task Started")
#     cnt = 0
#     for i in range(10**7):
#         cnt += i
#     print("Task Done") 


# if __name__ == "__main__":
#  start = time.time()

#  processes = [Process(target = cpu_heavy) for _ in range(2)]

#  [t.start() for t in processes]
#  [t.join() for t in processes]

#  end = time.time()

#  print(f"Time taken {end - start}")

#  Task Started
# Task Started
# Task Done
# Task Done
# Time taken 0.5807991027832031