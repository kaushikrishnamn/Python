# while loop

i = 1
while i <= 50:
    print(i)
    i += 1
else:
    print("Thank you!")

while True:
    response = input("Enter a number: ")
    if response.isdigit():
        break
