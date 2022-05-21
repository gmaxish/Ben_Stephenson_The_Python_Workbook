"""
Упражнение 10.Арифметика

Создайте программу, которая запрашивает у пользователя два целых числа a и b, после чего выводит на экран результаты
следующих математических операций:
 сумма a и b;
 разница между a и b;
 произведение a и b;
 частное от деления a на b;
 остаток от деления a на b;
 десятичный логарифм числа a;
 результат возведения числа a в степень b.

Подсказка. Функцию log10 вы найдете в модуле math.
"""
from math import log10

a = input('Enter first number: ')
b = input('Enter second number: ')

print('Sum: ', int(a) + int(b))
print('Subtraction: ', (int(a) - int(b)))
print('Multiply: ', (int(a) * int(b)))
print('Quotient of division: ', (int(a) // int(b)))
print('Remainder of the division: ', (int(a) % int(b)))
print('Decimal logarithm of a number: ', log10(int(a)))
print('Result of raising a number: ', int(a) ** int(b))
