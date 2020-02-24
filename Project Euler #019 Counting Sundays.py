# Using Zeller’s Congruence to find the Day for a Date.
def get_day(year: int, month: int, day: int):
    if month == 1:
        month = 13
        year -= 1
    if month == 2:
        month = 14
        year -= 1
    q = day
    m = month
    k = year % 100
    j = year // 100
    return (q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7


for _ in range(int(input())):
    dow = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    y1, m1, d1 = tuple(map(int, input().split()))
    y2, m2, d2 = tuple(map(int, input().split()))
    count = 0

    # if d1 != 1 then we have to increment next month so that my logic won't check 1st of same month.
    if d1 != 1:
        m1 += 1

    while y1 < y2:
        while m1 <= 12:
            if dow[get_day(y1, m1, 1)] == dow[1]:
                count += 1
            m1 += 1
        y1 += 1
        m1 = 1
    while m1 <= m2:
        if dow[get_day(y1, m1, 1)] == dow[1]:
            count += 1
        m1 += 1

    print(count)
