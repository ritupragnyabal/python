# list comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list or range).
# number = [1,2,3,4,5]
# data = []
# for num in number:
#     data.append(num ** 2)
# print(data)  # Output: [1, 4, 9, 16, 25]

# Using list comprehension
nums = [1, 2, 3, 4, 5]
data = [num ** 2 for num in nums]
print(data)  # Output: [1, 4, 9, 16, 25]

# list comprehension with condition
numbers = [1,2,3,4,5,6]
even_numbers = [
    number 
    for number in numbers
    if number % 2 == 0
]
print(even_numbers)  # Output: [2, 4, 6]

# dictionary comprehension
# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# my_dict = {k: v for k, v in zip(keys, values)}
# print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

numbers = [1, 2, 3, 4, 5]
squares = {
    number: number ** 2
    for number in numbers
}
print(squares)  # Output: [1, 4, 9, 16, 25]

# set comprehension
numbers = [1, 2, 3, 4, 5, 1, 2, 3]
unique = {number for number in numbers}
print(unique)  # Output: {1, 2, 3, 4, 5}

names = ["Python","django","flask","python"]
unique_names = {
    # name.upper()
    name for name in names
}
print(unique_names)  # Output: {'PYTHON', 'DJANGO', 'FLASK'}00