# I'm using inbuilt function to calculate factorial but for languages with no inbuilt factorial/BigInteger support
# we have to develop a different logic.
from math import factorial

for _ in range(int(input())):
    ans = 0
    for x in str(factorial(int(input()))):
        ans += int(x)
    print(ans)
