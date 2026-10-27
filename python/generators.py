def gen():
    yield 1
    yield 2
    yield 3

def not_gen():
    return [1 , 2 , 3]

func1 = gen()
func2 = not_gen()

print(func1 , func2)
# <generator object gen at 0x000002D0CB0650C0> [1, 2, 3]

# func1 is now an iterable , pointing to the gen() function in memory , its just a reference to that function.

# for num in func1:
    # print(num)

# print(next(func1))



def customer():
    print("Placing order")
    order = yield
    while True:
        print(f"preparing {order}")
        order = yield

stall = customer()
next(stall) # when this is called code pauses at order = yield , it waits for a value to be sent to this generator function
stall.send("pizza") # pizza value is sent so the code moves further and stalls again at another order=yield waiting for one more send
stall.send('burger')

# OUTPUT
# Placing order
# preparing pizza
# preparing burger

def function1():
    yield "random1"
    yield "random2"

def function2():
    yield "random3"
    yield "random4"

def function3():
    yield from function1()
    yield from function2()

for item in function3():
    print(item)


