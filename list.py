# 1. Introduction
list = ["item1", "item2", 3]

# 2. Creating a List
names = ["sammy", "sharon", "billy"]
print(names)  # Output: ['sammy', 'sharon', 'billy']

# 3. Accessing Elements
first_name = names[0]
print(first_name)  # Output: sammy

first_two_names = names[0:2]
print(first_two_names)  # Output: ['sammy', 'sharon']

# 4. Modifying Elements
names[1] = "Ian"
print(names)  # Output: ['sammy', 'Ian', 'billy']

# 5. Adding Elements
my_list = [2, 7, 4, 9]
my_list.append(8)
print(my_list)  # Output: [2, 7, 4, 9, 8]

my_list.insert(1, 3)
print(my_list)  # Output: [2, 3, 7, 4, 9, 8]

# 6. Removing Elements
del(my_list[1])
print(my_list)  # Output: [2, 7, 4, 9, 8]

my_list.remove(8)
print(my_list)  # Output: [2, 7, 4, 9]

my_list.pop()
print(my_list)  # Output: [2, 7, 4]

# 7. Find length of list
print(len(my_list))  # Output: 3