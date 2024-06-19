# DRY -> Don't Repeat Yourself!
# positional arguments WITH default parameters
def say_hello(name="Darth Vader", emoji="👿"):
    print(f"Hello, {name}{emoji}")


say_hello("kaushik", "❤️")
say_hello("abhiram", "😶‍🌫️")
say_hello("ganya", "😎")

# keyword arguments

say_hello(emoji="🧑‍💻", name="yasha")
say_hello()


# Function should do one thing really well.
# Should return something.
def sum(num1, num2):
    return num1 + num2


total = sum(2, 3)
print(sum(15, total))


def summing(num1, num2):
    def another_summing(n1, n2):
        return n1 + n2
    return another_summing(num1, num2)


print(summing(2, 3))
