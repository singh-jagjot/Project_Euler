# This was the logic I used to solve this problem but correct
# approach is to use LCM.
for _ in range(int(input())):
    n = int(input())
    val = 1
    lst = [1, 2, 3, 2, 5, 1, 7, 2, 3, 1, 11, 1, 13, 1, 1, 2, 17, 1, 19, 1, 1, 1, 23, 1, 5, 1, 3, 1, 29, 1, 31, 2, 1, 1,
           1, 1, 37, 1, 1, 1]
    for x in range(n):
        val *= lst[x]
    print(val)
