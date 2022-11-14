import random


def get_unique_list_numbers(num_min=-10, num_max=10, length=15) -> list[int]:
    list_numbers = []
    while len(list_numbers) < length:
        num_rand = random.randint(num_min, num_max)
        if num_rand not in list_numbers:
            list_numbers.append(num_rand)
    return list_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
