def arithmetic_function(number_one, number_two, operation):
    if operation == '+':
        return number_one + number_two
    elif operation == '-':
        return number_one - number_two
    elif operation == '*':
        return number_one * number_two
    elif operation == '/':
        if number_two == 0:
            return "Error division by zero"
        return number_one / number_two
    else:
        return f"None operation: {operation}"
result = arithmetic_function(3, 3, '+')
print(result)
result = arithmetic_function(3, 3, '-')
print(result)
result = arithmetic_function(3, 3, '*')
print(result)
result = arithmetic_function(3, 3, '/')
print(result)
result = arithmetic_function(3, 0, '/')
print(result)
result = arithmetic_function(3, 3, '%')
print(result)
