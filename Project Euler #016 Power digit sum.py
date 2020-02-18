for _ in range(int(input())):
    n = int(input())
    su = 0
    for i in str(2 ** n):
        su += int(i)
    print(su)
