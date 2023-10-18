first_file = 'first.txt'
second_file = 'second.txt'
try:
    with open(first_file, 'r') as first_file:
        content = first_file.read()
        with open(second_file, 'w') as second_file:
            second_file.write(content)
    print('Copy')
except FileNotFoundError:
    print('Not file')
