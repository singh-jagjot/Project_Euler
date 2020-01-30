n = 120000  # Value used as per constraint
# Using Sieve of eratosthenes
prime = [True for i in range(n + 1)]
p = 2
while p * p <= n:
    if prime[p]:
        for i in range(p * p, n + 1, p):
            prime[i] = False
    p += 1

lst = [x for x, y in enumerate(prime) if y]

for _ in range(int(input())):
    n = int(input()) + 1
    print(lst[n])
