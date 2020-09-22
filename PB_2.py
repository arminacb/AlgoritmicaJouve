from common import is_prime


def largest_prime_factor(num):
    max_prime = 2
    prod = 1
    for i in range(num+1):
        if not is_prime(i):
            continue

        if not num % i and i > max_prime:
           max_prime = i
           prod *= i

        if max_prime ** 2 > num or prod == num:
            break
    return max_prime

print(largest_prime_factor(600851475143))
