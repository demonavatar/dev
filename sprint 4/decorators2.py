import time
from functools import wraps
cached = {}

def time_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = round(time.time() - start_time, 1)
        print(f'Время выполнения функции {func.__name__}: {execution_time} с.')
        return result

    return wrapper


def cache_args(func):
    # Здесь код декоратора
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = args
        if cached.get(key, False) == False:
            cached[key] = func(*args, **kwargs)
            result = cached[key]
        else:
            result = cached[key]
        return result
    return wrapper



@time_check
@cache_args
def long_heavy(num):
    time.sleep(1)
    return num * 2


print(long_heavy(1))
# Время выполнения функции long_heavy: 1.0 с.
# 2
print(long_heavy(1))
# Время выполнения функции long_heavy: 0.0 с.
# 2
print(long_heavy(2))
# Время выполнения функции long_heavy: 1.0 с.
# 4
print(long_heavy(2))
# Время выполнения функции long_heavy: 0.0 с.
# 4
print(long_heavy(2))
# Время выполнения функции long_heavy: 0.0 с.
# 4