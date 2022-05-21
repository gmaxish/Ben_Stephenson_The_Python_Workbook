"""
Упражнение 9. Сложные проценты

Представьте, что вы открыли в банке сберегательный счет под 4 % годовых.
Проценты банк рассчитывает в конце года и добавляет к сумме счета.
Напишите программу, которая запрашивает у пользователя сумму первоначального депозита, после чего рассчитывает и выводит
на экран сумму на счету в конце первого, второго и третьего годов. Все суммы должны быть округлены до двух знаков после
запятой.
"""

rate = 0.04

amount = input('Enter your deposit amount: ')

first_year = float(amount) * rate + float(amount)
second_year = float(first_year) * rate + first_year
third_year = float(second_year) * rate + second_year

print(f'After first year: {first_year:.2f}.\nAfter second year: {second_year:.2f}. \nAfter third year: {third_year:.2f}.')