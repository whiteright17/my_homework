def is_prime(number):
    number = int(number)
    if number < 2:
        return False
    for division in range(2, number):
        if number % division == 0:
            return False
    return True
number = input('Write number:')
result = is_prime(number)
print(result)

