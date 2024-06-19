def super_func(*args, **kwargs):
    print(args)
    print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))

# Rule: params, *args, default params, **kwargs


def args_kwargs_rev(*numbers, **more_numbers):
    print(numbers)
    print(more_numbers)
    total = 0
    for items in more_numbers.values():
        total += items
    return sum(numbers) + total


print(args_kwargs_rev(1, 2, 3, 4, 5, num1=5, num2=10))
