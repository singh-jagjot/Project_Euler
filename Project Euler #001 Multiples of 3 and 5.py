def res(x, y):
    return y * x * (x + 1) // 2


for _ in range(int(input().strip())):
    ls = 0
    n = int(input().strip())
    sum3 = res((n - 1) // 3, 3)
    sum5 = res((n - 1) // 5, 5)
    sum15 = res((n - 1) // 15, 15)
    print(sum3 + sum5 - sum15)
