for item in 'Zero to Mastery':
    print(item)

for item in [1, 2, 3, 4, 5]:
    print(item)

for item in {1, 2, 3, 4, 5}:
    print(item)

for item in (1, 2, 3, 4, 5):
    print(item)

# Nesting of Loops

for item in {1, 2, 3, 4, 5}:
    for alphabet in ['a', 'b', 'c', 'd']:
        print(item, alphabet)


user = {
    'name': "Golem",
    'age': 5006,
    'can_swim': False
}

for item in user.items():
    print(item)

for item in user.keys():
    print(item)

for item in user.values():
    print(item)

for key, value in user.items():
    print(key, value)

# range

print(range(0, 100))
for item in range(1, 11):
    print(item)

for item in range(1, 11, 2):
    print(item)

for item in range(10, 0, -1):
    print(item)

for _ in range(2):
    print(list(range(11)))
