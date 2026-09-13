# map func
numbers = [1, 2, 3, 4, 5]
result = (map(lambda x: x ** 2, numbers))
print(list(result))  # Output: [1, 4, 9, 16, 25]

price = [100,200,300]
prices_with_tax = list(
    map(lambda x: x * 1.18, price)
    )
print(prices_with_tax)  # Output: [110.0, 220.0, 330.0]

# filter func
numbers=[10,15,20,25,30]
even_numbers = list(
    filter(
        lambda x: x % 2 == 0, numbers)
    )
print(even_numbers)  # Output: [10, 20, 30]

# in place of filter func we can use map func to get the same output and it will give true false
numbers=[10,15,20,25,30]
even_numbers = list(
    map(
        lambda x: x % 2 == 0, numbers)
    )
print(even_numbers)  # Output: [10, 20, 30]


# reduce func =- reduce many values to one value
from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(
    lambda x, y: x + y, numbers)
print(result)  # Output: 15

# zip func
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
result = zip(names, scores)
print(list(result))  # Output: [('Alice', 85), ('Bob', 90), ('Charlie', 95)]

products = ["Apple", "Banana", "Orange"]
prices = [0.5, 0.3, 0.7]
product_prices = dict(zip(products, prices))
print(product_prices)  # Output: {'Apple': 0.5, 'Banana': 0.3, 'Orange': 0.7} dictionary


products = ["Apple", "Banana", "Orange"]
prices = [0.5, 0.3, 0.7]
product_prices = set(zip(products, prices))
print(product_prices)  # Output: {'Apple': 0.5, 'Banana': 0.3, 'Orange': 0.7} set

# enumerate func - to give index and value of the list
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names,start=1): #by default start=0 but we can change it to any number
    print(index, name)
    
    
# any func - returns true if any of the values in the iterable is true like or operator 
numbers = [1,3,5,8]
result = any(
    num % 2 == 0 for num in numbers
    )
print(result)  # Output: True

numbers = [1,3,5,7]
result = any(
    num % 2 == 0 for num in numbers
    )
print(result)  # Output: False


# all func - returns true if all of the values in the iterable is true like and operator like and operator
password = ["abc123","python123","hi123"]
result = all(
    len(password) >= 6 
    for password in password
    )
print(result)  # Output: True