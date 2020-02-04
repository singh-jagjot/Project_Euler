lst = []
for _ in range(20):
    lst.append([int(x) for x in input().split()])
MAX_SUM = 0
for i in range(20):
    for j in range(17):
        temp = lst[i][j] * lst[i][j + 1] * lst[i][j + 2] * lst[i][j + 3]
        if temp > MAX_SUM:
            MAX_SUM = temp

for j in range(20):
    for i in range(17):
        temp = lst[i][j] * lst[i + 1][j] * lst[i + 2][j] * lst[i + 3][j]
        if temp > MAX_SUM:
            MAX_SUM = temp

for i in range(3, 20):
    temp = i
    j = 0
    dia = []
    while temp > -1:
        dia.append(lst[temp][j])
        temp -= 1
        j += 1
    for x in range(len(dia) - 3):
        temp = dia[x] * dia[x + 1] * dia[x + 2] * dia[x + 3]
        if temp > MAX_SUM:
            MAX_SUM = temp

for j in range(1, 20):
    temp = j
    i = 19
    dia = []
    while temp < 20:
        dia.append(lst[i][temp])
        temp += 1
        i -= 1
    for x in range(len(dia) - 3):
        temp = dia[x] * dia[x + 1] * dia[x + 2] * dia[x + 3]
        if temp > MAX_SUM:
            MAX_SUM = temp

for i in range(20):
    j = 0
    temp = i
    dia = []
    while temp < 20:
        dia.append(lst[temp][j])
        temp += 1
        j += 1
    # print(dia)
    for x in range(len(dia) - 3):
        temp = dia[x] * dia[x + 1] * dia[x + 2] * dia[x + 3]
        if temp > MAX_SUM:
            MAX_SUM = temp

for j in range(1, 20):
    temp = j
    i = 0
    dia = []
    while temp < 20:
        dia.append(lst[i][temp])
        temp += 1
        i += 1
    for x in range(len(dia) - 3):
        temp = dia[x] * dia[x + 1] * dia[x + 2] * dia[x + 3]
        if temp > MAX_SUM:
            MAX_SUM = temp
    # print(dia)
print(MAX_SUM)
