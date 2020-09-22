def get_fibonacci(max_val):
    a = 0
    b = 1
    res = 1
    sum = 0
    while res < max_val:
        res = a + b
        a = b
        b = res
        if not res % 2:
            sum += res
    return sum


limit = 4000000
import time

t1 = time.time()
for i in range(1000000):
    get_fibonacci(limit)
t2 = time.time()

print(str(t2 - t1))
