import math

for _ in range(int(input())):
    n = int(input())
    res = []
    while n % 2 == 0:
        res.append(2)
        n /= 2
    for x in range(3, math.floor(math.sqrt(n)) + 1, 2):
        while n % x == 0:
            res.append(x)
            n /= x
    if n > 2:
        res.append(int(n))
    print(max(res))
