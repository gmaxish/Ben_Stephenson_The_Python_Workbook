"""
Упражнение 4. Площадь садового участка

Создайте программу, запрашивающую у пользователя длину и ширину садового участка в футах.
Выведите на экран площадь участка в акрах.

Подсказка. В одном акре содержится 43 560 квадратных футов.
"""

lenght = input('Enter length of the garden plot in feet: ')
width = input('Enter width of the garden plot in feet: ')

square_in_acr = (float(lenght) * float(width)) / 43560
print(f'The square of garden plot in acres is {square_in_acr:.6f}\u00B2')
