### sets
-Set elements are unique.
-Set elements are unordered,sets do not record element position or order of insertion.
-Sets are mutable,but can only store immutable data.
-Sets do not support indexing, slicing, or other sequence-like behavior

### class constructor 
set()
my_set = set([1, 2, 3])
my_set = {1, 2, 3}

{}-empty dict

### operations

1) x in set:Test x for membership in s.
2) len(set):Return the number of elements in set s
3) x not in s:Test x for non-membership in s
4) copy():Return a shallow copy of the set.
5) add(elem)
6) remove(elem):Remove element elem from the set. Raises KeyError if elem is not contained in the set.
7) discard(elem): Remove element elem from the set if it is present.
8) clear() -Remove all elements from the set.
9) pop(): Remove and return an arbitrary element from the set. Raises KeyError if the set is empty


Note, the non-operator versions of union(), intersection(), difference()

set('abc').intersection('cbs')
### uses
# Instantiating a set using a sequence is a good way to isolate unique members.

my_list = [1, 2, 1, 3, 2]
set(my_list)

my_string = "the big red cat ate the fat rat"
set(my_string)

# Check whether two sets are identical,same members

set(range(1, 10)) == set([1, 2, 3, 4, 5, 6, 7, 8, 9])

# common elements/intersection (&)

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_1 & set_2

# difference in sets (-)

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_1 - set_2

# union of sets

 set | other



# set values as we  move (&= ,-=)

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_1 &= set_2
set_2 -= set_1

# support comprehensions with the same syntax as lists

sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
unique_consonants = {c.lower() for c in sentence if c not in "aeiou ,."}
# {'g', 'p', 'b', 'l', 'r', 'd', 'm', 'q', 'c', 't', 's', 'n'}
