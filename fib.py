from functools import lru_cache
import time
import matplotlib.pyplot as plt

timing_data = []

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        timing_data.append(elapsed_time)
        print(f"Finished in {elapsed_time:.8f}s: {func.__name__}({args[0]}) -> {result}")
        return result
    return wrapper

@lru_cache
@timer
def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    for _ in range(10):
        fib(100)

    # Plot the timing data
    plt.plot(timing_data, marker='o')
    plt.xlabel('Iteration')
    plt.ylabel('Elapsed Time (s)')
    plt.title('Execution Time for fib(100)')
    plt.show()
