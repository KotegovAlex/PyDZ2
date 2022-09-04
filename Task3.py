# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

k = int(input("Введите число k => "))
i = 0
sequence = []

while i < k:
    sequence.append((1 + 1 / (i + 1))**(i + 1))
    i += 1

print(sequence)
print(round(sum(sequence), 3))