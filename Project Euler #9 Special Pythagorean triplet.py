# Solve for:
# 1) a + b + c = n ==> c = n - (a + b)
# 2) a^2 + b^2 = c^2
for _ in range(int(input())):
    n = int(input())
    a = 3
    lst = []
    while a < n / 3:
        b = n * (2 * a - n) / (2 * (a - n))
        c = n - a - b
        if b % 1 == 0 and a < b < c:
            lst.append(int(a * b * c))
        a += 1

    if lst:
        print(max(lst))
    else:
        print("-1")
