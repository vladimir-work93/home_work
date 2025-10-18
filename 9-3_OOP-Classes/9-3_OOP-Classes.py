# Задача 1: Температурный конвертер
# Условие:
# Создайте класс Temperature, который хранит температуру в Цельсиях, но
# позволяет получать и устанавливать ее также в Фаренгейтах и Кельвинах через свойства.
# При изменении значения в одной шкале автоматически должны обновляться значения в других.

# class Temperature:
#     def __init__(self, temp=0):
#         self.__temp = temp
#
#     @property
#     def temp_c(self):
#         return self.__temp
#
#     @temp_c.setter
#     def temp_c(self, value):
#         self.__temp = value
#
#     @property
#     def temp_f(self):
#         return self.__temp * 9/5 + 32
#
#     @temp_f.setter
#     def temp_f(self, value):
#         self.__temp = (value - 32) * 5/9
#
#     @property
#     def temp_k(self):
#         return self.__temp + 273.15
#
#     @temp_k.setter
#     def temp_k(self, value):
#         if value < 0:
#             raise ValueError('Температура в К не может быть отрицательной!')
#         self.__temp = value - 273.15
#
#     def print_temp(self):
#         print(f'Цельсия: {self.temp_c:.2f}\n'
#               f'Фаренгейт: {self.temp_f:.2f}\n'
#               f'Кельвин: {self.temp_k:.2f}\n')
#
# # Задаем Цельсия
# temp_1 = Temperature()
# temp_1.temp_c = 0
# temp_1.print_temp()
#
# # Задаем Кельвин
# temp_2 = Temperature()
# try:
#     temp_2.temp_k = 0
# except ValueError as e:
#     print(e)
# else:
#     temp_2.print_temp()
#
# # Задаем Фаренгейт
# temp_3 = Temperature()
# temp_3.temp_f = 0
# temp_3.print_temp()

# Задача 2: Валидация электронной почты
# Условие:
# Создайте класс User со свойством email, которое автоматически проверяет
# корректность адреса электронной почты при установке значения.
# Если email невалиден, должно вызываться исключение.

# import re
#
# class User:
#     def __init__(self):
#         self.__mail = None
#
#     @property
#     def mail(self):
#         return self.__mail
#
#     @mail.setter
#     def mail(self, value):
#         pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#         if not re.match(pattern, value):
#             raise ValueError('Некорректная почта!')
#         self.__mail = value
#
# mail_1 = User()
# mail_1.mail = 'semenov_1@mail.ru'
# print(mail_1.mail)
#
# mail_2 = User()
# try:
#     mail_2.mail = 'semenov_1mail.ru'
# except ValueError as e:
#     print(e)
# else:
#     print(mail_2.mail)

# Задача 3: Вычисление площади круга
# Условие:
# Создайте класс Circle, который принимает радиус при инициализации.
# Реализуйте свойство area, которое возвращает площадь круга, и свойство
# circumference для длины окружности. Свойства должны вычислять значения динамически.

# import math
#
# class Circle:
#     def __init__(self, radius = 0):
#         self.__radius = radius
#
#     @property
#     def radius(self):
#         return self.__radius
#
#     @radius.setter
#     def radius(self, value):
#         if value < 0:
#             raise ValueError('Радиус должен быть положительным!')
#         self.__radius = value
#
#     @property
#     def area(self):
#         return math.pi * self.__radius ** 2
#
#     @property
#     def circumference(self):
#         return 2 * math.pi * self.__radius
#
#     def print_circle(self):
#         print(f'Радиус = {self.radius:.2f}\n'
#               f'Площадь = {self.area:.2f}\n'
#               f'Длина = {self.circumference:.2f}\n')
#
#
# circle_1 = Circle()
# circle_1.radius = 1
# circle_1.print_circle()
#
# circle_2 = Circle()
# try:
#     circle_2.radius = -1
# except ValueError as e:
#     print(e)
# else:
#     circle_2.print_circle()