number_one = float(input('First number: '))
number_two = float(input('Two number: '))
formula = input('Operation: ')
result = ""
if formula == '1':
    result = number_one + number_two
elif formula == '2':
    result = number_one - number_two
elif formula == '3':
    result = number_one * number_two
elif formula == '4':
    if number_two != 0:
        result = number_one / number_two
        else:
        print('ssss')
    else:
        print('Error!')
if result is not None:
    print(f"Result: {result}")