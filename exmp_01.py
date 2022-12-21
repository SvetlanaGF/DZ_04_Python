# 1 - Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

number = int(input('Введите натуральное число: '))

def factors_calculation(number):
    """Создает список простых множителей заданного числа"""
    factor = 2
    factors_array = []
    while factor * factor <= number:
        if number % factor == 0:
            factors_array.append(factor)
            number //= factor
        else:
            factor += 1
    if number > 1:
        factors_array.append(number)

    return factors_array

print(factors_calculation(number))