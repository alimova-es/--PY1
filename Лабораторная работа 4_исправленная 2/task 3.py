# TODO реализовать функцию удаления элемента из списка по индексу
def delete(list_, index=None):
    if index is None:
        list_ = list_[:-1]  # Если пользователь не указал индекс, выводим весь список без последнего элемента
    else:
        list1_ = list_[0:index]
        list2_ = list_[index+1:]
        list_ = list1_ + list2_
    return list_


print(delete([0, 0, 1, 2], index=0))  # [0, 1, 2]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3, 4]
