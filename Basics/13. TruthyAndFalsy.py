# Truthy & Falsy

print(bool(5))
print(bool('hello'))

print(bool(0))
print(bool(''))
print(bool(None))

username = 'kaushik'
password = '123'

if username and password:
    print("Success!!")
else:
    print("Fail!!")