def my_min(*args):
    if not args:
        raise ValueError("No arguments")
    min_value = args[0]
    for value in args:
        if value < min_value:
            max_value = value
    return min_value
user_input = input("Enter values:")
values = [int(value) for value in user_input.split()]
result = my_min(*values)
print("Minimum value:", result)
