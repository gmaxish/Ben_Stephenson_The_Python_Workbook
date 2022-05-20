"""
Упражнение 3. Площадь комнаты

Напишите программу, запрашивающую у пользователя длину и ширину комнаты.
После ввода значений должен быть произведен расчет площади комнаты и выведен на экран.
Длина и ширина комнаты должны вводиться в формате числа с плавающей запятой. Дополните ввод и вывод единицами измерения,
принятыми в вашей стране. Это могут быть футы или метры.
"""

lenght = input('Enter length of the room in meters: ')
width = input('Enter width of the room in meters: ')

square = float(lenght) * float(width)
print(f'The square of the room with lenght {lenght} and width {width} is {square:.2f} meter\u00B2')