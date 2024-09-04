# Creating a dictionary
my_dict = {"name": "Ian", "age": 26}
# print("Initial dictionary:", my_dict)

# Accessing items
value = my_dict["name"]
print("Value accessed with []:", value)
value = my_dict.get("age")
print("Value accessed with get():", value)

# Modifying a dictionary
my_dict["age"] = 27
my_dict["location"] = "USA"
print("After updating and adding items:", my_dict)

# Removing items
value = my_dict.pop("age")
# print("Removed value:", value)
del my_dict["location"]
print("After removing a key with del:", my_dict)
my_dict.clear()
# print("After clearing the dictionary:", my_dict)

# Copying dictionaries
dict_copy = {"name": "Ian", "age": 27}  # Resetting to original for copying example
dict_copy = dict_copy.copy()
print("Shallow copy of dictionary:", dict_copy)

# Nested dictionaries
nested_dict = {
    "user1": {"name": "Alice", "age": 30},
    "user2": {"name": "Bob", "age": 25}
}
print("Nested dictionary:", nested_dict)

# Checking existence of keys
value = "name" in my_dict
print("Key 'name' exists:", value)

# Dictionary methods
keys = dict_copy.keys()
print("Keys:", keys)
values = dict_copy.values()
print("Values:", values)
items = dict_copy.items()
print("Items:", items)
dict_copy.update({"email": "ian@example.com"})
print("After update:", dict_copy)

# Dictionary comprehensions
squares = {x: x*x for x in range(6)}
print("Dictionary comprehension - squares:", squares)

# Common dictionary use cases
from collections import defaultdict
data = [
    {"name": "Alice", "group": "A"},
    {"name": "Bob", "group": "B"},
    {"name": "Charlie", "group": "A"}
]
grouped_data = defaultdict(list)
for item in data:
    grouped_data[item["group"]].append(item["name"])
# print("Grouped data:", dict(grouped_data))  

