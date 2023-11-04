class Apple:
    def __init__(self, name, qa, founded, departments):
        self.name = name
        self.qa = qa
        self.founded = founded
        self.departments = departments

apple = Apple(
    name="Apple",
    qa="Vadym Andriienko",
    founded=1994,
    departments="QA Department"
)

print(f"Company Name: {apple.name}")
print(f"QA: {apple.qa}")
print(f"Founded: {apple.founded}")
print(f"Department: {apple.departments}")

