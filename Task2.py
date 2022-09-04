# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
    # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math

number = int(input("Введите число N => "))
number_composition = []
if number == 0:
    number_composition.append(math.factorial(0))
    print(number_composition)
elif number < 0:
    print("Требуется ввести число N >= 0!!!")
else:
    for i in range(1, number + 1):
        number_composition.append(math.factorial(i))
    print(number_composition)