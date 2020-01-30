# Use Sieve of Eratosthenes in clever way.
limit = 1000001
lst = [True] * limit
lst_sum = [0] * limit
lst[0] = lst[1] = False
p = 2
for p in range(limit):
    if lst[p]:
        lst_sum[p] = lst_sum[p - 1] + p
        for x in range(p ** 2, limit, p):
            lst[x] = False
    else:
        lst_sum[p] = lst_sum[p - 1]

# print(lst_sum)
for _ in range(int(input())):
    n = int(input())
    print(lst_sum[n])
