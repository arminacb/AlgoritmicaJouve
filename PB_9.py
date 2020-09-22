import datetime


def solution(n):
    """
    a^2 + b^2 = c^2
    a + b + c = target_sum

    :param n: target sum
    :return: prod(a, b, c)
    """

    for i in range(1, n):
        for j in range(2, n + 1):
            a, b, c = calculate_triplet(j, i)

            if a + b + c > n:
                break

            if a + b + c == n:
                return a * b * c


def calculate_triplet(u, v):
    """

    :param u:
    :param v:
    :return:
    """
    a = u ** 2 - v ** 2
    b = 2 * u * v
    c = u ** 2 + v ** 2
    return a, b, c


start = datetime.datetime.now()
for i in range(10000):
    solution(1000)
end = datetime.datetime.now()

print(f"Total time {end - start}")
