def cache3(func):
    cache_count = {0:0}
    cache = func()
    def wrapper ():
        cache_count[0] += 1
        while cache_count[0] <= 3 :
            return cache
        result = func()
        cache_count[0] = 0
        return result
    return wrapper


@cache3
def heavy():
    print('Сложные вычисления')
    return 1


print(heavy())
# Сложные вычисления
# 1
print(heavy())
# 1
print(heavy())
# 1

# Опять кеш устарел, надо вычислять заново
print(heavy())
# Сложные вычисления
# 1