numbers = [1,2,3,4,5]
squares = (number ** 2 for number in numbers)
for value in squares:
    print(value)  # Output: 1, 4, 9, 16, 25
# value = next(squares)
# print(value)  # Output: 1
# print(squares)  # Output: <generator object <genexpr> at 0x7f8e4c3b1d30>