roles = {
    'admin': ['Alice', 'Bob', 'Carol'],
    'maintainer': ['David', 'Eve'],
    'manager': ['Frank', 'Grace'],
    'developer': ['Heidi', 'Ivan']
}
all_users = ('Alice, Bob, Carol, David, Eve, Frank, Grace, Heidi, Ivan')
print(all_users)
user_name = input("Print name: ")
for role, users in roles.items():
    if user_name in users:
        print(f"Hello, {role}")