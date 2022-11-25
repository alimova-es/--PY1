import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    with open(filename) as f_csv:
        list_dicts = []
        for index_of_line, line in enumerate(f_csv):
            # 1. Формируем из строки line список list_of_line_element из элементов line
            # split() возвращает копию исходной строки
            # путем удаления начальных и конечных пробелов или символов, переданных в функцию strip()
            list_of_line_element = line.strip(new_line).split(delimiter)

            # 2. Первая строка выступает в качестве заголовков столбцов, которые мы будем дальше использовать
            if index_of_line == 0:
                column_headings = list_of_line_element
                continue

            # 3. Добавляем в конец списка пустой словарь, чтобы в нем формировать строки: заголовок - значение
            list_dicts.append({})

            # 4. В последней элемент списка (пустой словарь) добавляем нужные строки: заголовок - значение
            output = {name_column: list_of_line_element[index_of_name_column]
                      for index_of_name_column, name_column in enumerate(column_headings)}
            list_dicts[-1] = output
    return list_dicts


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
