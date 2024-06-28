import time


def measure_time(func):
    """Returns wrapper for counting execution time and returns it"""
    def wrapper(*args, **kwargs):
        """Counts execution time and returns it"""
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time - start_time
        print(f"{func.__name__}: {exec_time:.4f} seconds")
        return exec_time
    return wrapper

