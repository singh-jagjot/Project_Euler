# Used Memoization (Dynamic Programming)
limit = 5000001
cache = [0] * limit
cache[1] = 1


def get_collatz(num):
    # This is to avoid exception if num >= limit(this can occur in recursive call).
    if num < limit:
        temp1 = cache[num] if cache[num] != 0 else (
            get_collatz(num // 2) + 1 if num % 2 == 0 else get_collatz(3 * num + 1) + 1)
        cache[num] = temp1
    else:
        # Here we don't store result is cache as num >= limit.
        temp1 = get_collatz(num // 2) + 1 if num % 2 == 0 else get_collatz(3 * num + 1) + 1
    return temp1


currentMax = 0
MAX = [0]
# Need to calculate for every value till limit(nothing can be done).
for i in range(1, limit):
    temp2 = get_collatz(i)
    if temp2 >= currentMax:
        currentMax = temp2
        MAX.append(i)
    else:
        MAX.append(MAX[i - 1])

for _ in range(int(input())):
    n = int(input())
    print(MAX[n])
    # print(cache)
