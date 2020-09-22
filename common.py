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