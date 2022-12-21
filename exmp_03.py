# 3 - В файле, содержащем фамилии студентов и их оценки,
# изменить на прописные буквы фамилии тех студентов,
# которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4

def output_student_list():
    """Печать данных из файла"""
    path = 'exmp03_student.txt'
    student = open(path, 'r', encoding='utf-8')
    for stud_i in student:
        print(stud_i[:-1])
    student.close()

with open('exmp03_student.txt', 'w', encoding='utf-8') as student:
    """Запись начальных данных в файл"""
    student.writelines('Ангела Меркель 5\n')
    student.writelines('Энакин Скайуокер 5\n')
    student.writelines('Фредди Меркури 3\n')
    student.writelines('Александр Пушкин 4\n')

print('\nНачальные данные:\n')
output_student_list()

with open('exmp03_student.txt', 'r', encoding='utf-8') as file:
    """Получаем данные из файла"""
    student_list = file.readlines()
k = 0
for i in student_list:
    """Отличникам меняем стиль записи"""
    if int(i[-2]) > 4:
        i = i.upper()
        student_list[k] = i
    else:
        student_list[k] = i
    k += 1

with open('exmp03_student.txt', 'w', encoding='utf-8') as file:
    """Запись измененных данных в файл"""
    file.writelines(student_list)

print('\nИзмененные данные:\n')
output_student_list()
