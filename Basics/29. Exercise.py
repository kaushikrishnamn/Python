# def highest_even(num_list):
#     highest = -1
#     for item in num_list:
#         if item % 2 == 0 and item > highest:
#             highest = item
#     return highest

def highest_even(num_list):
    evens = []
    for num in num_list:
        if num % 2 == 0:
            evens.append(num)
    return max(evens)


print(highest_even([10, 3, 5, 7, 9]))
