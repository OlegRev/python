﻿#easy
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
def my_round(number, ndigits):
    number = number*(10**ndigits)+0.5
    number = number//1
    return number/(10**ndigits)
print(my_round(float(input('введите число через точку"."')), float(input('количество знаков после точки'))))
# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
def lucky_ticket(numb):
    numb = (str(numb))
    if len(numb)<6:
        return 'некоректный номер билета'
    left = int(numb[0]) + int(numb[1]) + int(numb[2])
    right = int(numb[3]) + int(numb[4]) + int(numb[5])
    if left == right:
        return 'lucky man'
    else:
        return 'not today'
print(lucky_ticket(456654))
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
#normal
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
def fibonacci(n, m):
    a = 0
    b = 1
    j = 0
    for i in range(n, m):
        if j < m:
            a, b = b, a+b
            print(a)
        j +=1
print(fibonacci(3,12))
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
def sort_to_max(origin_list):
    i = 1
    while i < len(origin_list):
        for j in range(len(origin_list) - i):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
        i += 1
    return origin_list
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_filter(func,iter):
    out_iter = []
    for i in range(len(iter)):
        if func(iter[i]) == True:
            out_iter.append(iter[i])
    return out_iter

func = lambda x: type(x) == int
iter = [-1, 2, 'a', 4, 'fgf']
print(my_filter(func,iter))
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

#hard
# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
