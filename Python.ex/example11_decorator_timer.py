from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        before = time()
        result = func(*args, **kwargs)
        after = time()
        print(f"Elapsed time: {after - before}")
        return result
    return wrapper


@timer
def add(x, y=10):
    return x + y


@timer
def sub(x, y=10):
    return x - y


print(add(10))
print(add(20, 30))
print(sub(20))
print(sub(20, 30))
