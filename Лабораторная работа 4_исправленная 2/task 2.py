# TODO посчитать количество каждой буквы в строке в аргументе str_


def main():
    main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """
    print(get_count_char(main_str))
    print(get_percent_char(get_count_char(main_str)))


def get_count_char(str_):
    symbol_dict = {}
    default_count = 0
    str_ = "".join(str_.split())
    str_lower = str_.lower()
    list_str_lower = list(str_lower)
    list_str_lower.sort()
    for symbol in list_str_lower:
        if symbol.isalpha():
            symbol_dict[symbol] = symbol_dict.get(symbol, default_count) + 1
    return symbol_dict


def get_percent_char(dict_):
    percent_dict = {}
    total_count = sum(dict_.values())  # суммируем только значения
    for symbol in dict_:
        percent_dict[symbol] = (dict_.get(symbol)/total_count) * 100
    return percent_dict


main()
