from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("before")
        func()
        print("after")

    return wrapper

@my_decorator
def greet():
    print("Hello")

greet()
print(greet.__name__)