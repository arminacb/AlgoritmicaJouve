import math
from time import time
from functools import reduce
from math import gcd

# ------------ STACK SOLUTION -----------------------------------------------------------------------------------------

def lcm(a, b):
    "Calculate the lowest common multiple of two integers a and b"
    return a * b // gcd(a, b)


def get_min_multi(n):
    return reduce(lcm, range(1, n + 1))


t1 = time()
for i in range(10000):
    get_min_multi(10)
t2 = time()
for i in range(10000):
    get_min_multi(20)
t3 = time()
for i in range(10000):
    get_min_multi(20)
t4 = time()

e1 = t2 - t1
e2 = t3 - t1
e3 = t4 - t1
print('Elapsed(stack) time 10 is %f seconds.' % e1)
print('Elapsed(stack) time 20 is %f seconds.' % e2)
print('Elapsed(stack) time 30 is %f seconds.' % e3)


# ------------ MY SOLUTION -----------------------------------------------------------------------------------------

def get_min_multiple(num):
    min_multiples = _get_min_multiple(num)

    final_res = 1
    for b in min_multiples:
        p = min_multiples[b]
        val = final_res * b ** p
        final_res = val
    return final_res




def _get_min_multiple(num):
    res = {}
    for n in range(1, num + 1):
        n_primes = get_all_prime_factors(n)
        res = choose_max_power(res, n_primes)
    return res


def get_all_prime_factors(n):
    """
    Return a dict containing all primes factors for n and their powers
    :param n:
    :return:
    """
    d = 2
    res = {}
    while n > 1:
        s = 0
        while n % d == 0:
            s = s + 1
            n = n / d
        if s != 0:
            res[d] = s
        d = d + 1
    return res


def choose_max_power(res, n_primes):
    for base in n_primes:
        power = n_primes[base]
        if res.get(base, None) and res[base] > power:
            continue
        res[base] = power
    return res



t1 = time()
for i in range(10000):
    get_min_multiple(10)
t2 = time()
for i in range(10000):
    get_min_multiple(20)
t3 = time()
for i in range(10000):
    get_min_multiple(20)
t4 = time()

e1 = t2 - t1
e2 = t3 - t1
e3 = t4 - t1
print('Elapsed time 10 is %f seconds.' % e1)
print('Elapsed time 20 is %f seconds.' % e2)
print('Elapsed time 30 is %f seconds.' % e3)
