"""
Упражнение 8. Сувениры и безделушки

Интернет-магазин занимается продажей различных сувениров и безделушек. Каждый сувенир весит 75 г, а безделушка – 112 г.
Напишите программу, запрашивающую у пользователя количество тех и других покупок, после чего выведите на экран общий вес
посылки.
"""

souvenir_weight = 0.075
bauble_weight = 0.112

q_souvenir = input('Enter the quantity of souvenir: ')
q_bauble = input('Enter the quantity if bauble: ')

print(f'Total weight of souvenir = {int(q_souvenir) * souvenir_weight:.2f} kilograms')
print(f'Total weight of bauble = {int(q_bauble) * bauble_weight:.2f} kilograms')
