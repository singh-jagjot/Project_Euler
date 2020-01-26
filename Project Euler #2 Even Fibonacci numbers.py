for _ in range(int(input())):
    val = int(input())
    lst = [2]
    a, b = 1, 2
    # In Fibonacci sequence even terms appear after every 2 odd terms
    while b <= val:
        for x in range(3):
            a, b = b, a + b
        lst.append(b)
        # print(lst)

    print(sum(lst[:-1]))
