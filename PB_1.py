
sum = 0
n = 1
while n < 1000:
    if not n % 3 or not n % 5:
        sum += n
    n += 1
print(sum)