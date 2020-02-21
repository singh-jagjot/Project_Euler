# A basic recursive function can give the required answer as the constraints are small.
def max_path(ls, n, i):
    if len(ls) - 1 == n:
        return ls[n][i]

    else:
        left_sum = ls[n][i] + max_path(ls, n + 1, i)
        right_sum = ls[n][i] + max_path(ls, n + 1, i + 1)
        return max(left_sum, right_sum)


for _ in range(int(input())):
    n = int(input())
    ls = [list(map(int, input().split())) for _ in range(n)]
    res = max_path(ls, 0, 0)
    print(res)
