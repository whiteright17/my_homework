def my_max(*args):
    if not args:
        raise ValueError("No arguments")
    max_value = args[0]
    for value in args:
        if value > max_value:
            max_value = value
    return max_value
user_input = input("Enter values:")
values = [int(value) for value in user_input.split()]
result = my_max(*values)
print("Maximum value:", result)
