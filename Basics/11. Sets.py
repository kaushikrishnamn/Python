# sets => unordered collection of unique objects

my_set = {1,2,3,4,5,6,7,8,9,10,10}
print(my_set)

#adding

my_set.add(11)
my_set.add(10)
print(my_set)

my_list = [1,2,3,4,5,5]
print(set(my_list))

new_set = my_set.copy()
my_set.clear()
print(my_set)
print(new_set)

# Methods

my_set = {1,2,3,4,5,}
your_set = {4,5,6,7,8,9,10}

# difference => gives the difference in the first set as compared to the second set.
# Removes the duplicates from the both sets and only returns the remaining elements from the first set
print(my_set.difference(your_set))

#discard => discards the element from the set
my_set.discard(5)
print(my_set)
my_set.add(5)

# difference_update => removes all elements of another set from this set.
my_set.difference_update(your_set)
print(my_set)
my_set.add(4)
my_set.add(5)

# intersection => gives common elements in both the sets
print(my_set.intersection(your_set))
# print(my_set & your_set)

#isdisjoint => if they have nothing in common we get True, else False
print(my_set.isdisjoint(your_set))

# issubset => Returns true if the first set is subset of second
print(my_set.issubset(your_set))

# issuperset => Returns true if the first set is super set to the second one
print(my_set.issuperset(your_set))

# union => combines both the sets
print(my_set.union(your_set))
# print(my_set | your_set)