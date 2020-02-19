# Unique values initialization.
ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
rest = ["Hundred", "Thousand", "Million", "Billion", "Trillion"]
ls = []

# Constants to identify whether function call to word() is a recursive one of not.
MAIN = "main"
INTERNAL = "internal"


# Recursive function to find words.
def word(n: int, call: str):
    if len(str(n)) < 2:
        if call != MAIN and n == 0:
            return
        ls.append(ones[n])
    elif len(str(n)) < 3 and n < 20:
        ls.append(teens[n % 10])
    elif len(str(n)) < 3:
        ls.append(tens[n // 10])
        word(n % 10, INTERNAL)
    elif len(str(n)) < 4:
        word(n // 100, INTERNAL)
        ls.append(rest[0])
        word(n % 100, INTERNAL)
    elif len(str(n)) < 7:
        word(n // 1000, INTERNAL)
        ls.append(rest[1])
        word(n % 1000, INTERNAL)
    elif len(str(n)) < 10:
        word(n // 1000000, INTERNAL)
        ls.append(rest[2])
        word(n % 1000000, INTERNAL)
    else:
        word(n // 1000000000, INTERNAL)
        ls.append(rest[3])
        word(n % 1000000000, INTERNAL)


for _ in range(int(input())):
    n = int(input())
    ls = []
    if n == 1000000000000:
        print("One", rest[4])
    else:
        word(n, MAIN)
        for i in ls:
            print(i, end=' ')
        print()
