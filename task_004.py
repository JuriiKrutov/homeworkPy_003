'''Напишите программу, которая будет преобразовывать десятичное число в двоичное.'''
num = int(input('Введите число: '))
number = ''
while num != 0:
    number += str(num % 2)
    num //= 2

print(int(number[::-1]))