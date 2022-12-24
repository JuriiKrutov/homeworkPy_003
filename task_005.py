'''Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.'''
def pozitiv_fib(n):
    pozitiv_list = [0, 1]
    for i in range(n - 1):
        pozitiv_list.append(pozitiv_list[-2] + pozitiv_list[-1])
    return pozitiv_list

def negativ_fib(n):
    negativ_list = [0, 1]
    for i in range(n - 1):
        negativ_list.append(negativ_list[-2] - negativ_list[-1])
    return negativ_list

n = int(input())

print(negativ_fib(n)[::-1] + pozitiv_fib(n)[1:])