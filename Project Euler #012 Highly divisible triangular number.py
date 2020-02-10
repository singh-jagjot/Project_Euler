# Trick is to calculate divisors efficiently. Need to calculate till sqrt(n).
from math import ceil, sqrt


def get_divisors(num):
    count = 0
    expo = []
    while num % 2 == 0:
        count += 1
        num /= 2
    if count:
        expo.append(count + 1)

    for x in range(3, ceil(sqrt(num)) + 1, 2):
        count = 0
        while num % x == 0:
            count += 1
            num /= x
        if count:
            expo.append(count + 1)
    if num > 2:
        expo.append(2)
    # print(expo)
    tot = 1
    for x in expo:
        tot *= x
    return tot


for _ in range(int(input())):
    n = int(input())
    divisors = 1
    tn = 1
    while divisors <= n:
        if tn % 2 == 0:
            divisors = int(get_divisors(tn / 2) * get_divisors(tn + 1))
        else:
            divisors = int(get_divisors(tn) * get_divisors((tn + 1) / 2))
        tn += 1
    tn -= 1
    print(int(tn * (tn + 1) / 2))
