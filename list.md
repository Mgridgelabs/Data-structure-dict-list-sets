Python Lists
----------------------

1. Introduction:
   - A list is a collection of items in a particular order.
   - The items can be of different data types.
   - Lists are defined by enclosing elements in square brackets [].

2. Creating a List:
   - Syntax: `my_list = [item1, item2, item3]`
   - Example: `names = ["sammy", "sharon", "cherry"]`

3. Accessing Elements:
   - Use the index to access elements: `my_list[index]`
   - Indexing starts at 0.
   - Example: `first_name = names[0]`
   - Extract a portion of the list: `my_list[start:stop]`
   - Example: `first_two = names[0:2]`  # ["sammy", "sharon"]

4. Modifying Elements:
   - Assign a new value to a specific index: `my_list[index] = new_value`
   - Example: `names[1] = "Ian"`  # changes "sharon" to "Ian"

5. Adding Elements:
   # append(item) - add at the end
   my_list.append(8)
   print(my_list)  # Output: [2, 7, 4, 9, 8]

   # insert(index, item) - add item at specific index
   my_list.insert(1, 3)
   print(my_list)  # Output: [2, 3, 7, 4, 9, 8]

6. Removing Elements:
   # del(item index)
   del(my_list[1])
   print(my_list)  # Output: [2, 7, 4, 9, 8]

   # remove(specific item)
   my_list.remove(8)
   print(my_list)  # Output: [2, 7, 4, 9]

   # pop() - removes last item and returns it
   my_list.pop()
   print(my_list)  # Output: [2, 7, 4]

7. Find length of list:
   # len() - returns the number of items in the list
   print(len(my_list))  # Output: 3