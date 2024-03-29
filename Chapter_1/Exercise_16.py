"""
Упражнение 16. Площадь и объем

Напишите программу, которая будет запрашивать у пользователя радиус и сохранять его в переменной r.
После этого она должна вычислить площадь круга с заданным радиусом и объем шара с тем же радиусом.
Используйте в своих вычислениях константу pi из модуля math.

Подсказка: Площадь круга вычисляется по формуле area = πr** , а объем шара – по формуле volume = (4/3)πr***
"""

from math import pi

r = float(input('Enter radius: '))

area = pi * pow(r, 2)
volume = (4/3) * pi * pow(r, 3)

print(area)
print(volume)
