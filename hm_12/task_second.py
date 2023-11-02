def generate_even_squares(start, end):
    for i in range(start, end + 1, 2):
        yield i * i
if __name__ == "__main__":
    start_range = 0
    end_range = 1000000000
    for task_result in generate_even_squares(start_range, end_range):
        print(task_result)
        