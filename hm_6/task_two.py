input_my_string = "hello 1 one two three 15 world"
words = input_my_string.split()
consecutive_count = 0
for i in range(2, len(words)):
    if words[i-2].isalpha() and words[i-1].isalpha() and words[i].isalpha():
        consecutive_count += 1
        if consecutive_count >= 1:
            print("Є три слова поспіль.")
        else:
            print("Немає трьох слов поспіль.")
