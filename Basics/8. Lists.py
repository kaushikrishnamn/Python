# lists

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c', 'd', 'e']
li3 = [1, 2, 'a', 'b', True]
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
print(amazon_cart)

# List Slicing
print(amazon_cart[0:2])
print(amazon_cart[0::2])

# Lists are mutable
amazon_cart[0] = 'laptop'
print(amazon_cart)

new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(amazon_cart)
print(new_cart)

# Matrix

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print(matrix)
print(matrix[0][1])

# List Methods
basket = [1, 2, 3, 4, 5]
print(len(basket))

# Adding Elements

# append
basket.append(6)
print(basket)

# insert
basket.insert(1, 7)
print(basket)

# extend
basket.extend([8, 9])
print(basket)

# Removing Elements

# pop
basket.pop()
print(basket)

# pop with index
basket.pop(1)
print(basket)

# remove
basket.remove(8)
print(basket)

# clear
basket.clear()
print(basket)

# index
basket = ['a', 'b', 'c', 'd', 'e']
print(basket.index('d'))
print('d' in basket)
print('x' in basket)

# count
basket.append('d')
print(basket.count('d'))

# sort
basket.sort()
print(basket)

basket.insert(1, 'x')
basket.sort()
print(basket)

# reverse
basket = ['a', 'z', 'x', 'f', 'e']
basket.reverse()
print(basket)

# Tricks with lists
basket = ['a', 'z', 'x', 'f', 'e']
print(len(basket))
print(basket[::-1])
print(list(range(1, 100)))
sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'a', 'dog'])
print(new_sentence)

# unpacking

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a, b, c)
print(other)
print(d)
