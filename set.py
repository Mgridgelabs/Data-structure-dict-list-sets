value = set([1, 2, 3])


my_set={'jack',2, 'sjoerd',"Tan",45}
value= 2 in my_set
value= 5 not in my_set
value=len(my_set)
value=my_set.copy()
my_set.remove(2)
my_set.discard("jack")
my_set.add("john")
value= my_set


value=my_set.copy()


value=my_set.pop()

value=set('abc').intersection('cbs')


value = set(range(1, 10)) == set([1, 2, 3, 4, 5, 6, 7, 8, 9])

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
value=set_1 & set_2

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
value=set_1 - set_2

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
value=set_1 | set_2



sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
value = {c.lower() for c in sentence if c not in "aeiou ,."}

print(value)