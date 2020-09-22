from time import time


def is_prime(n):
    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if not (n % 2 and n % 3):
        return False

    i = 5
    while i * i <= n:
        if not (n % i and n % (i + 2)):
            return False
        i += 6

    return True


def get_nth_prime(n):
    num = 1
    prime_cnt = 0
    while True:
        if is_prime(num):
            prime_cnt += 1
        if prime_cnt == n:
            break
        num += 1
    return num


print(get_nth_prime(10001))

t1 = time()
for i in range(10):
    get_nth_prime(10001)
t2 = time()

e1 = t2 - t1
print('Elapsed time is %f seconds.' % e1)
