"""
Упражнение 6. Налоги и чаевые

Программа, которую вы напишете, должна начинаться с запроса у пользователя суммы заказа в ресторане.
После этого должен быть произведен расчет налога и чаевых официанту. Вы можете использовать принятую в вашем регионе
налоговую ставку для подсчета суммы сборов. В качестве чаевых мы оставим 18 % от стоимости заказа без учета налога.
На выходе программа должна отобразить отдельно налог, сумму чаевых и итог, включая обе составляющие.
Форматируйте вывод таким образом, чтобы все числа отображались с двумя знаками после запятой.
"""

tax = 0.2
tips = 0.18

total = input("Enter yor total price in restaurant: ")

price_withot_tax = float(total) - (float(total) * tax)
for_tips = float(price_withot_tax) * tips

print(f'Price without tax will be {price_withot_tax:.2f}.'      
      f'\nTax = {float(total) * tax:.2f}'
      f'\nTips = {for_tips:.2f}.'
      f'\nTotal is', float(total) + for_tips, end='.')