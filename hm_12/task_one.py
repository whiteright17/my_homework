def name_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function Name:", func.__name__)
        return func(*args, **kwargs)
    return wrapper
@name_decorator
def my_max(*args):
    max_value = args[0]
    for value in args:
        if value > max_value:
            max_value = value
    return max_value
user_print = input("Enter values:")
values = [int(value) for value in user_print.split()]
result = my_max(*values)
print("Maximum value:", result)
