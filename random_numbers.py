import random

def main():
    randnums = [16.2, 75.1, 52.3]
    print(randnums)
    # append_random_numbers(5)
    print(randnums)
    # append_random_numbers(8, 15)
    print(randnums)

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        random_num = round(random.uniform(1, 100), 1)
        numbers_list.append(random_num)