users = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 3, "name": "Charlie", "age": 35},
]
user_map = {
    # user["id"] : user["name"]
    user["id"] : {"name": user["name"], "age": user["age"]}
    for user in users
}
print(user_map)  # Output: {1: {'name': 'Alice', 'age': 30}, 2: {'name': 'Bob', 'age': 25}, 3: {'name': 'Charlie', 'age': 35}}