# Tuples => Immutable Lists

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1])
print(5 in my_tuple)

user = {
    (1,2): [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print(user[(1,2)])

new_tuple = my_tuple[1:2]
print(new_tuple)

x,y,z, *other = my_tuple
print(x)
print(y)
print(z)
print(other)

# methods

# count
print(my_tuple.count(5))

#index
print(my_tuple.index(5))