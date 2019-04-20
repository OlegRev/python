import os
##################################функция вывода списка директорий и файлов
if __name__ == '__main__':
    print('список директорий и файлов')
def dir_list():
        print('Список директорий',[('{}.{}'.format(idx, item))\
               for idx, item in enumerate(os.listdir())\
               if os.path.isdir(item)])
        print('Список файлов',[('{}.{}'.format(idx, item))\
              for idx, item in enumerate(os.listdir())\
              if os.path.isfile(item)])
if __name__ == '__main__':
    dir_list()
###############################функция удаления директорий
def rm_dir(name):
    try:
        os.rmdir(name)
        print('{}-удалена'.format(name))
    except FileExistsError:
        print("Директория {} уже не существует".format(name))
if __name__ == '__main__':
    pass
##############################функция создания директорий
def mk_dir(name):
    try:
        os.mkdir(name)
        print('{}-создана'.format(name))
    except FileExistsError:
        print("Директория {} уже существует".format(name))
if __name__ == '__main__':
    pass
############################функция перехода в директорию
def dir_change(path):
    try:
        os.chdir(path)
        return 'Вы перешли в директорию: {}'.format(path)
    except FileNotFoundError:
        return ('{} - директория не существует'.format(path))
####################
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


