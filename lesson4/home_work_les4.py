# Все задачи текущего блока решите с помощью генераторов списков!


# Задание-1:EASY

# Дан список, заполненный произвольными целыми числами. 

# Получить новый список, элементы которого будут

# квадратами элементов исходного списка

# [1, 2, 4, 0] --> [1, 4, 16, 0]


temp2 = [int(itm)**2 for itm in range(1, 10)]
print(temp2)

# Задание-2:

# Даны два списка фруктов.

# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1 = ['бананы', 'грушы', 'киви', 'яблоки', 'апельсины', 'манго', 'парсики']
fruits2 = ['айва', 'грушы', 'грейпфрут', 'памело', 'апельсины', 'манго', 'парсики']
cross_fruits = [itm1 for itm1 in fruits1 if itm1 in fruits2]
print(cross_fruits)

# Задание-3:

# Дан список, заполненный произвольными числами.

# Получить список из элементов исходного, удовлетворяющих следующим условиям:

# + Элемент кратен 3

# + Элемент положительный

# + Элемент не кратен 4

temp = [itm for itm in range(-15, 30) if itm % 3 == 0 and itm > 0 and itm % 4 != 0]
print(temp)

##########################################################################

# Задание-1:NORMAL

# Вывести символы в нижнем регистре, которые находятся вокруг

# 1 или более символов в верхнем регистре.

# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']

# Решить задачу двумя способами: с помощью re и без.


import re

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO' \
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK' \
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn' \
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa' \
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete' \
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ' \
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb' \
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC' \
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB' \
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT' \
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu' \
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB' \
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa' \
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ' \
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

re_template = r"[A-Z]*([a-z]+)*[A-Z]"
print(re.findall(re_template, line))



# Задание-2:

# Вывести символы в верхнем регистре, слева от которых находятся

# два символа в нижнем регистре, а справа - два символа в верхнем регистре.

# Т.е. из строки 

# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"

# нужно получить список строк: ['AY', 'NOGI', 'P']

# Решить задачу двумя способами: с помощью re и без.


import re

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

re_template =r"[a-z]{2}([A-Z]+)[A-Z]{2}"
print(re.findall(re_template, line_2))




# Задание-3:

# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)

# произвольными целыми цифрами, в результате в файле должно быть

# 2500-значное произвольное число.

# Найдите и выведите самую длинную последовательность одинаковых цифр

# в вышезаполненном файле.

#########################################################
# Задание-1:HARD

# Матрицы в питоне реализуются в виде вложенных списков:

# Пример. Дано:

matrix = [[1, 0, 8],

          [3, 4, 1],

          [0, 4, 2]]


# Выполнить поворот (транспонирование) матрицы

# Пример. Результат:

# matrix_rotate = [[1, 3, 0],

#                  [0, 4, 4],

#                  [8, 1, 2]]


# Суть сложности hard: Решите задачу в одну строку
rotate_matrix = [print(line) for line in list(map(list, zip(*matrix)))]

# Задание-2:

# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.

# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.

# Пример 1000-значного числа:

# number = """
#
# 73167176531330624919225119674426574742355349194934
#
# 96983520312774506326239578318016984801869478851843
#
# 85861560789112949495459501737958331952853208805511
#
# 12540698747158523863050715693290963295227443043557
#
# 66896648950445244523161731856403098711121722383113
#
# 62229893423380308135336276614282806444486645238749
#
# 30358907296290491560440772390713810515859307960866
#
# 70172427121883998797908792274921901699720888093776
#
# 65727333001053367881220235421809751254540594752243
#
# 52584907711670556013604839586446706324415722155397
#
# 53697817977846174064955149290862569321978468622482
#
# 83972241375657056057490261407972968652414535100474
#
# 82166370484403199890008895243450658541227588666881
#
# 16427171479924442928230863465674813919123162824586
#
# 17866458359124566529476545682848912883142607690042
#
# 24219022671055626321111109370544217506941658960408
#
# 07198403850962455444362981230987879927244284909188
#
# 84580156166097919133875499200524063689912560717606
#
# 05886116467109405077541002256983155200055935729725
#
# 71636269561882670428252483600823257530420752963450"""
#


# Задание-3 (Ферзи):

# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били

# друг друга. Вам дана расстановка 8 ферзей на доске.

# Определите, есть ли среди них пара бьющих друг друга.

# Программа получает на вход восемь пар чисел,

# каждое число от 1 до 8 — координаты 8 ферзей.

# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
