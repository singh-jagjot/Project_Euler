# My solution uses dynamic programming but better solution is to use
# combinatorics. The combinatorial solution implemented in a smart way
# to make use of the modulus will be orders of magnitude quicker.
# Here is a link for refrence https://en.wikipedia.org/wiki/Lattice_path
limit = 501
cache = [[-1 for j in range(limit)] for _ in range(limit)]


def routes(n, m):
    if cache[n][m] != -1:
        return cache[n][m]
    elif n == 1 or m == 1:
        return n + m
    else:
        cache[n][m] = routes(n - 1, m) + routes(n, m - 1)
        return cache[n][m]


for _ in range(int(input())):
    (n, m) = map(int, input().split())
    res = routes(n, m)
    print(res % 1000000007)
    # print(cache)
