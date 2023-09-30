numbers = [*range(1, 50)]
divide = int(input('Divide by: '))
for i in numbers:
    if i % divide == 0:
        print(i)
# first_task
numb = [1, 2, 3, 4, 6, 7, 8]
one_not_sequential = None
for a in range(len(numb) - 1):
    number_ok = numb[a]
    next_number = numb[a + 1]
    if next_number != number_ok + 1:
        one_not_sequential = next_number
        break
if one_not_sequential is not None:
    print("Error: ", one_not_sequential)
else:
    print("Its OK")
# second_task
for i in range(1, 5):
    print('*' * i)
# third_task




