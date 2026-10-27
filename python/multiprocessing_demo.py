from multiprocessing import Process
import time

def brew(name):
    print(f"Start of {name}")
    time.sleep(3)
    print(f"End of {name}")


if __name__ == "__main__":
    chai_makers = [
        Process(target=brew , args=(f"Chai maker {i + 1}", ))
        for i in range(3)
    ]

    for p in chai_makers:
        p.start()

    for p in chai_makers:
        p.join()
        

# Start of Chai maker 1
# Start of Chai maker 2
# Start of Chai maker 3
# End of Chai maker 1
# End of Chai maker 2
# End of Chai maker 3

# all start together end together
# uses 3 cores