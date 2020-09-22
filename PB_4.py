def get_max_palindrome(nr_digits):
    max_palindrome = 0
    for i in range(1, 10 ** nr_digits):
        for j in range(1, 10 ** nr_digits):
            prod = i * j
            if check_palindrome(prod) and max_palindrome < prod:
                max_palindrome = prod
    return max_palindrome


def isNumberPalindrome(n):
    return str(n) == str(n)[::-1]

def check_palindrome(n):
    temp = n
    rev = 0
    while (n > 0):
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if temp == rev:
        return True
    return False
print(get_max_palindrome(3))