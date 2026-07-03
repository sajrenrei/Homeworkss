import time


def my_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func()
        print(f"Execution time: {time.time() - start} seconds")
    return wrapper
