# Dictionary

dictionary = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
}

print(dictionary)
print(dictionary['a'])
print(dictionary['a'][1])
print(dictionary['b'])
print(dictionary['x'])

my_list = [
    {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
    },
    {
    'a': [4, 5, 6],
    'b': 'hello',
    'x': True
    }
]

print(my_list[0]['a'][2])

# Keys can be anything immutable like string, boolean, numbers it can't have something mutable, like a List
# Must have unique keys, else it'll override the previously stored value.

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print('age' in user)
print(user.get('age', 55))

# Another way to create a dictionary

user2 = dict(name='JohnJohn')
print(user2)

# methods

print('age' in user.keys())
print(20 in user.values())
print(user.items())

user3 = user.copy()
print(user)
print(user3)

# clear
print(user.clear())

# pop
print(user3.pop('age'))
print(user3)

# pops last item from the dictionary
print(user3.popitem())
print(user3)

# update

print(user3.update({'age': 55}))
print(user3)

































