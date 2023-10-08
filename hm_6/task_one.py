from collections import namedtuple
Tuple_my = namedtuple('MyTuple', ['value1', 'value2'])
tuple_my_list = [Tuple_my(10, 'Vadym'), Tuple_my(20, 'Tester'), Tuple_my(30, 'QA')]
for tup in tuple_my_list:
    if isinstance(tup, Tuple_my):
        print('Value 1: {}, Value 2: {}'.format(tup.value1, tup.value2))
    else:
        print('Warning! Invalid data type. Expected MyTuple, Actual {}')
        