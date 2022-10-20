# TODO посчитать количество каждой буквы в строке в аргументе str_

symbol_dict = {}
DEFAULT_COUNT = 0


def get_count_char(str_):
    str_ = "".join(str_.split())
    str_lower = str_.lower()
    list_str_lower = list(str_lower)
    list_str_lower.sort()
    for symbol in list_str_lower:
        if symbol.isalpha():
            symbol_dict[symbol] = symbol_dict.get(symbol, DEFAULT_COUNT) + 1
    return symbol_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

# Цикл для более красивого и наглядного вывода словаря
#for letter, count in symbol_dict.items():  # перебираем пары ключ-значение
    #print("Letter:", letter, "Value:", count)


total_count = sum(symbol_dict.values())  # суммируем только значения
percent_dict = {}


def get_percent_char(dict_):
    for symbol in symbol_dict:
        percent_dict[symbol] = (symbol_dict.get(symbol)/total_count) * 100
    return percent_dict


print(get_percent_char(symbol_dict))
