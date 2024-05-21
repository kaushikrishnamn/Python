'''

    # Fundamental Data Types

    => int
    => float
    => complex
    => bool
    => str
    => list
    => tuple
    => set
    => dict

    # Classes -> custom types

    # Specialized Data Types

    None

'''
print('Int & Float Operations:')

print(2 + 4)
print(2 - 4)
print(2 * 4)
print(2 / 4)
print(2 ** 3) # Power
print(3 // 4) # Quotient
print(6 // 4) # Quotient
print(6 % 4)  # Reminder

print('\nTypes: ')
print(type(2 + 4))
print(type(2 - 4))
print(type(2 * 4))
print(type(2 / 4))

# math functions
print('\n Math Functions: ')
print(round(3.1))
print(round(3.1, 2))
print(abs(-2))

# Exercise

print('\nExercise:')

print((5 + 4) * 10 / 2) #45

print(((5 + 4) * 10) / 2) #45

print((5 + 4) * (10 / 2)) #45

print(5 + (4 * 10) / 2) #25

print(5 + 4 * 10 // 2) #25

#bin()

print('\nBin: ')

print(bin(5))
print(int('0b101', 2))