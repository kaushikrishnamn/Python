# 1 - Start with local
# 2 - Parent local?
# 3 - Global
# 4 - Built-in python functions

counter = 0


def count(counter):
    counter += 1
    return counter


print(count(count(count(counter))))
