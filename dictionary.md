### Dictionary 
"is a python data structure"
this is an unordered collection of items(key, value) pairs

#     1.Creating a new dictionary
    {} or dict ()
**syntax** = my_dict = {
    "key": "value",
} 
**syntax** = my_dict = dict(
    name="value"
)


# 2.Accesing Dictionary items.
by using [] or get()
 **name** = my_dict["name"]
**age** = my_dict.get("age") 
 *safe to use than [],since it returns a none if key doesn't exist* 

#  3.Modifying a Dictionary.
adding / removing 
**Adding** 
my_dict["age"] = 26 #updates the original 
my_dict["name"] = "ian" #adds a new key-value pair
**Removing**
*pop () method.*
my_dict.pop("age") #removes key and returns value.
*del statement*
del my_dict["key"]
*clear() method*
my_dict.clear() #empties the entire dictionary

#  4.Looping Through a Dictionary.
## Looping through keys
for key in my_dict:
    print(key)
## Looping through values
for value in my_dict.values():
    print(value)
## Looping through key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")

#  5.Dictionary Methods.
## keys() returns a view object containing the dictionary keys.
keys = my_dict.keys()
## values () returns a view object containing the dictionary values.
values = my_dict.values()
## items() returns a view object containing key-value pairs.
items = my_dict.items()
## updates () updates the dictionary with elements from another dictionary or an iterable of key-value pairs.
my_dict.updates({"key": "value"})

#  6.Dictionary Comprehensions.
::can create a dictionary with a concise syntax similar to list Comprehensions.
squares = {x: x*x for x in range(6)}

#  7.Nested Dictionaries.
# dict in another dictionary
netsed_dict = {
    "user1": {"key": "value"},
    "user2": {"key": "value"},
}

#  8.Checking Existence of Keys.
## using `in`
if "name" in my_dict:
    print("Name is a key in the dictionary")

#  9.Copying Dictionaries.
## shallow Copying
dict_copy = my_dict.copy()
## deep copy #for nested dictionary
import copy 
dict_copy.deep_copy = copy.deepcopy(my_dict)


#   10.Handling Missing Keys with `defaultdict`.
## `collections.defaultdict`
allows one to define a default value for a missing key
from collections import defaultdict
my_default_dict = defaultdict(int)
my_default_dict["missing_key"] += 1 

#   11.Merging Dictionaries (Python 3.9+).
## using `|` operator
dict1 = {"key": "value"}
dict2 = {"key": "value"}
merged_dict = dict1 | dict2 

#  12.Common Dictionary Use Cases.
## countering occurences.
from collections import counter 
my_list = ["apple", "banana", "apple","orange", "banana", "apple"]
counts = counter(my_list)
## grouping data by key
data = [
    {"name": "Alice", "group": "A"},
    {"name": "Bob", "group": "B"},
    {"name": "Charlie", "group": "A"}
]
grouped_data = defaultdict(list)
for item in data:
    grouped_data[item["group"]].append(item["name"])
    #output {'A': ['Alice', 'Charlie'], 'B': ['Bob']}


