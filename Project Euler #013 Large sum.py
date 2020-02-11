# This one was really easy for Python. For JAVA use BigInteger. For C/C++ you have to develop the logic.
ans = 0
for x in range(int(input())):
    ans += int(input())
ans = str(ans)
print(ans[:10])
