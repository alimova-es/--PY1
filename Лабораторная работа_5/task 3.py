# TODO написать функцию для получения списка уникальных целых чисел
import random


def get_unique_list_numbers() -> list[int]:
    list_numbers = []
    while len(list_numbers) != 15:
        list_numbers = list(set([random.randint(-10, 10) for _ in range(15)]))
    return list_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
