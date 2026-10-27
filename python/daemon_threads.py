import time
import threading

# def logging():
#     while True:
#         print("logging...")
#         time.sleep(3)

# t = threading.Thread(target=logging , daemon=True)
# t.start()

# print("main done")


# logging...
# main done



def logging():
    while True:
        print("logging...")
        time.sleep(3)

t = threading.Thread(target=logging , daemon=False)
t.start()

print("main done")


# logging...
# main done
# logging...
# logging...



#  Behavior comparison
# 🔸 Daemon thread
# t = threading.Thread(target=worker, daemon=True)
# 👉 When main finishes:

# thread is killed immediately

# no cleanup

# no guarantee of finishing work

# 🔸 Non-daemon thread (default)
# t = threading.Thread(target=worker)
# 👉 When main finishes:

# Python waits for thread to finish

# program does NOT exit until thread ends

# 🔹 Visual intuition
# Main thread ends
#      ↓
# Daemon threads → 💀 killed instantly
# Non-daemon     → ⏳ must finish first