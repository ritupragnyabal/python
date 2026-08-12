n = int(input("Enter the n: "))
if n<10:
    print(n)
else:
    result = 0
    while n > 0:
        digit = n % 10
        if digit < result or result == 0:
            result = digit
        n = n // 10