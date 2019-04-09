﻿__author__ = 'Глухарев Олег Анатольевич/Glukharev Oleg'
easy
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

	fruits = ['бананы', 'грушы', 'киви', 'яблоки', 'апельсины', 'манго', 'парсики']
	number_fruits = len(fruits)
	for i in range(number_fruits):
	    print(str(i+1) + '.' + '{:>10}'.format(fruits[i]))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

	one_list = [1,2,3,4,5,6,7,8,9,0,'a','s','d','f','g','h','j','k']
	two_list = [1,3,5,7,9,'s','f','h','k']
	for i in one_list:
    		for j in two_list:
        		if i == j :
            			one_list.remove(i)
            			#break
	print(one_list)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

	one_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
	two_list = []
	for i in one_list:
	    if i%2 ==0:
	        i= i/4
	        two_list.append(i)
	    elif i%2!=0:
	        i = i*2
	        two_list.append(i)
	print(two_list)

normal
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math
one_list = [-1,-9,-8,-16,25,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
two_list = []
for i in one_list:
	if i>0 and math.sqrt(i)-int(math.sqrt(i))==0:
	    #print(i)
	    i = int(math.sqrt(i))
	    two_list.append(i)
print(two_list)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

day = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое',
       '06': 'шестое', '07': 'седьмое', '08': 'восьмое','09': 'девятое','10': 'десятое',
       '11':'одиннадцатое','12':'двенадцатое','13':'тринадцатое','14':'четырнадцатое','15':'пятнадцатое',
       '16':'шестнадцатое','17':'семнадцатое','18':'восемнадцатое','19':'девятнадцатое','20':'двадцатое',
       '21':'дватцать первое','22':'дватцать второе','23':'дватцать третье','24':'дватцать четвертое',
       '25':'дватцать пятое','26':'дватцать шестое','27':'дватцать седьмое','28':'дватцать восьмое',
       '29':'дватцать девятое','30':'тридцатое','31':'тридцать первое'
}
month  = {'01': 'январь', '02': 'февраль', '03': 'март', '04': 'апрель', '05': 'май',
          '06': 'июнь', '07': 'июль', '08': 'август','09': 'сентябрь','10': 'октябрь',
          '11':'ноябрь','12':'декабрь'
}
data = '03.04.2015'
dot_split = data.split('.')
print('{} {} {} года'.format(day[dot_split[0]], month[dot_split[1]], dot_split[2]))

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
n = random.randint(3, 20)
my_list = [random.randint(-100,100) for i in range(n)]
print(my_list)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

hard
# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
