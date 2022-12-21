# 5 - Реализуйте RLE алгоритм:
# реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol

def input_list_element(path, elements):
    with open(path, 'w', encoding='utf-8') as file_start:
        """Запись данных в файл"""
        file_start.writelines(elements)

def output_list_element(path):
    """Печать данных из файла"""
    list_element = open(path, 'r', encoding='utf-8')
    for i in list_element:
        print(i)
    list_element.close()


input_list_element('exmp05_elemet_too_much.txt', 'AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool')

with open('exmp05_elemet_too_much.txt', 'r', encoding='utf-8') as file_start:
    """Получаем данные из файла"""
    list = file_start.readlines()

text = list[0]
length_text = len(text)
text_new = ''
k = -1
fist_element_in_section = text[0]
count = 1

for i in text:
    if k < (length_text - 2):
        k += 1
    fist_element_in_section = text[k+1]

    if text[k] == fist_element_in_section:
        count += 1
    else:
        if count > 1:
            text_new = text_new + str(count) + text[k]
        else: 
            text_new = text_new + text[k]
        count = 1

input_list_element('exmp05_elemet_enough.txt', text_new)
print('Начальные данные')
output_list_element('exmp05_elemet_too_much.txt')
print('Измененные данные')
output_list_element('exmp05_elemet_enough.txt')