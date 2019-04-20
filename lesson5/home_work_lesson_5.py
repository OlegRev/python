#EASY
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os                                                          #  функция
def mk_dir(name):                                                  #  создающая
    try:                                                           #  директорию name = 'dir'
        os.mkdir(name)                                             #
        print('{}-создана'.format(name))                           #
    except FileExistsError:                                        #
        print("Директория {} уже существует".format(name))         #
if __name__ == '__main__':
    for itm in range(1,10):              #
        mk_dir('dir_' + str(itm))        # создание директории dir_'itm'

#удаление папок
import os
def rm_dir(name):
    try:
        os.rmdir(name)
        print('{}-удалена'.format(name))
    except FileExistsError:
        print("Директория {} уже не существует".format(name))
if __name__ == '__main__':
    for itm in range(1,10):          #
        rm_dir('dir_' + str(itm))    #удаление директории dir_'itm'


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os
def dir_list():
        print('Список директорий',[('{}.{}'.format(idx, item))\
               for idx, item in enumerate(os.listdir())\
               if os.path.isdir(item)])
        print('Список файлов',[('{}.{}'.format(idx, item))\
              for idx, item in enumerate(os.listdir())\
              if os.path.isfile(item)])
if __name__ == '__main__':
    dir_list()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


import os
import shutil

def copy_file ():
    name_file = os.path.realpath(__file__)
    new_file = name_file +'.copy' + '.py'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        return new_file + ' - создан'
    else:
        return 'Файл уже скопирован'
if __name__ == '__main__':
    print(copy_file ())





#NORMAL
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

def dir_change(path):
    try:
        os.chdir(path)
        return 'Вы перешли в директорию: {}'.format(path)
    except FileNotFoundError:
        return ('{} - директория не существует'.format(path))
from easy import *
def console():
    answer =''
    dirs_number = range(1, 10)

    while answer != '5':

        answer = input('Выберите пункт меню:\n'
                       '1. Создать директории dir_1 - dir_9\n'
                       '2. Удалить директории dir_1 - dir_9\n'
                       '3. Показать списки файлов и директорий\n'
                       '4. Перейти в папку\n'
                       '5.Выход\n')
        if answer =='5':
            break
        if answer == '1':
            for itm in dirs_number:              #
                mk_dir('dir_' + str(itm))
        elif answer == '2':
            for itm in dirs_number:              #
                rm_dir('dir_' + str(itm))
        elif answer == '3':
            dir_list()
        elif answer == '4':
            dir_name = input('Укажите папку для перехода: ')
            print(dir_change(dir_name))


if __name__ == '__main__':
    console()
#HARD
#Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
