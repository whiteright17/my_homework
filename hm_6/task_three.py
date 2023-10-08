my_petals = int(input("Введіть кількість пелюсток: "))
if my_petals > 0:
    words = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    index = (my_petals - 1) % len(words)
    print("Petals:", words[index])
else:
    print("Petals must > 0.")
