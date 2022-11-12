# TODO написать функцию для получения списка уникальных целых чисел
import random


def get_unique_list_numbers(num_min=-10, num_max=10, length=15) -> list[int]:
    list_numbers = []
    while len(list_numbers) != length:
        list_numbers = list(set([random.randint(num_min, num_max) for _ in range(length)]))
    return list_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
