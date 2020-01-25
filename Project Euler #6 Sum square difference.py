for _ in range(int(input())):
    n = int(input())
    s1 = (n * (n + 1) // 2) ** 2
    s2 = n * (n + 1) * (2 * n + 1) // 6
    print(abs(s1 - s2))
