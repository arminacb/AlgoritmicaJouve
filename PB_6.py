from time import time


def sum_square_difference(n):
    return (((n ** 2) * (n + 1) ** 2) / 4) - (n * (n + 1) * (2 * n + 1) / 6)

def sum_sqr_dif(n):
    """
    (a + b + c + ... + n)^2 = a^2 + b^2 + ... + n^2 + 2(a*b + a*c + ... + (n-1) * n)

    :param n:
    :return:
    """
    s = 0
    for i in range(1, n + 1):
        for j in range(1, n+1):
            if i != j:
                s += i * j
    return s

t1 = time()
for i in range(1):
    sum_sqr_dif(1000000)
t2 = time()
for i in range(1):
    sum_square_difference(1000000)
# t3 = time()
# for i in range(1):
#     sum_square_difference(100000)
t4 = time()

t5 = time()

e1 = t2 - t1
e2 = t4 - t1
# e3 = t4 - t1
# e4 = t5 - t1
print('Elapsed time sum_sqr_dif is %f seconds.' % e1)
print('Elapsed time sum_square_difference is %f seconds.' % e2)
print(sum_sqr_dif(100))

# print('Elapsed time 10 is %f seconds.' % e3)
# print('Elapsed time 100 is %f seconds.' % e4)