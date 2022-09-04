# Реализуйте алгоритм перемешивания списка.
import random

n = random.randint(5, 15)

i = 0
my_list = []

while i < n:
    my_list.append(random.randint(-99, 99))
    i += 1

print(f"Исходный список: {my_list}")

# random.shuffle(first_list)
# print(first_list)

for k in range(len(my_list)):
    temp = my_list[k]
    rnd = random.randint(0, n - 1)
    my_list[k] = my_list[rnd]
    my_list[rnd] = temp

print(f"Итоговый список: {my_list}")