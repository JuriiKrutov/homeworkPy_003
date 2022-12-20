'''Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.'''

list = [2, 3, 4, 5, 6]
list_1 = []
l = len(list) // 2
for i in range(len(list) // 2 + 1):
    list_1.append(list[i] * list[-i - 1])
if len(list) % 2 == 0:
    list_1.append(list[len(list)//2 + 1]**2)
print(l)
print(list_1)