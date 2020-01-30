# Just iterate over n-digit number checking every possibility
# by removing/incrementing rear digit in one go.
for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    num = input()
    s = 0
    while len(num) >= k:
        temp = 1
        for x in num[:k]:
            temp *= int(x)
        if temp > s:
            s = temp
        num = num[1:]
    print(s)
