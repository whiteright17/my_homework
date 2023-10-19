course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}
try:
    user_input = input('Print Key:')
    value = course[user_input]
    print(user_input, value)
except KeyError:
    print('Error')
