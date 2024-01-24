# # arg1 = float(input("Введите что-то там: "))
# # arg2 = float(input("Введите что-то там 2: "))
# # print("Площадь",arg1 * 2 + arg2 * 2)
# # print("Периметр", arg1+arg2 * 2 )
# # print("Площадь", f"{arg1} * 2 + {arg2} * 2 = {arg1 * 2 + arg2 * 2}")
# # print("Периметр", f"{arg1} + {arg2} * 2 = {arg1 + arg2 * 2}")
#
# import math
# #
# # arg1 = int(input('Введите число: '))
# # calc = math.sqrt(arg1)
# # print('Корень:',calc)
# arg1 = float(input('Введите что-то: '))
# print('Ответ', math.pi * arg1)
import math

a = float(input('Введите A '))
b = float(input('Введите B '))
x = float(input('Введите X '))
print('y =', math.pow(math.sin( (math.pow(x, 2) + a)**2), 3) - math.sqrt(x/b))
print('z =', math.pow(x, 2)/a + math.cos((x+b)**3))
