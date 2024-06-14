print(type("Hi hello there"))

username = 'supercoder'
password = 'supersecret'
long_string = '''
WOW
0 0
---
'''

print(long_string)
first_name = 'Kaushik'
last_name = 'M N'

full_Name = first_name + ' ' + last_name
print(full_Name)

# string concatenation
print('hello' + " Kaushik!")

# Type Conversion
print(type(str(100)))

# Escape Sequence
weather = "It's Sunny"
print(weather)

weather = "It's \"kind of\" Sunny"
print(weather)

# Formatted Strings
print('\nFormatted String:')
name = 'Kaushik'
age = 29
print('Hi ' + name + '. You are ' + str(age) + ' years old.')
print('Hi {}. You are {} years old.'.format(name, age))  # Old Way
print(f'Hi {name}. You are {age} years old.')  # New Way

# String indices
print('\nString indices:')
selfish = "01234567"
print(selfish[0])
print(selfish[7])

# [start: stop]
print(selfish[0:2])
print(selfish[0:8])

# [start: stop: stepover]
print(selfish[0:8:2])

# Built-in functions
print('\nBuilt-in functions:')
print(len('Helloooo'))

quote = 'to be or not to be'
print(quote)
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
print(quote.replace('be', 'me'))
quote2 = quote.replace('be', 'me')
print(quote)
print(quote2)
