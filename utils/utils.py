import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        print(f"Execution time: {stop - start:.6f} seconds")
        return res

    return wrapper
