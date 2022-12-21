# 2 - Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности. 
# Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

numbers_list = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4]

def search_unique_elements(n_list):
    """Создаем список уникальных элементов из заданного"""
    unique_list = []
    for number in n_list:
        if number not in unique_list:
            unique_list.append(number)
    return unique_list

print(search_unique_elements(numbers_list))
 