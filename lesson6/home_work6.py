#easy
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

"""
import math
class triangle():

    def __init__(self, dot_x1, dot_y1, dot_x2, dot_y2, dot_x3, dot_y3):

        self.dot_x1 = dot_x1

        self.dot_y1 = dot_y1

        self.dot_x2 = dot_x2

        self.dot_y2 = dot_y2

        self.dot_x3 = dot_x3

        self.dot_y3 = dot_y3

        self.dot1_dot2 = round(math.fabs(math.sqrt(((int(dot_x2) - int(dot_x1))**2) + ((int(dot_y2) - int(dot_y1))**2))), 2)

        self.dot2_dot3 = round(math.fabs(math.sqrt(((int(dot_x3) - int(dot_x2))**2) + ((int(dot_y3) - int(dot_y2))**2))), 2)

        self.dot3_dot1 = round(math.fabs(math.sqrt(((int(dot_x1) - int(dot_x3))**2) + ((int(dot_y1) - int(dot_y3))**2))), 2)

    def area_of_triangle(self):
        self.area = round((math.fabs(((self.dot_x2 - self.dot_x1)\
                                      *(self.dot_y3 - self.dot_y1))\
                                      -((self.dot_x3 - self.dot_x1)\
                                      *(self.dot_y2 - self.dot_y3))))/2, 2)
        return (self.area)

    def triangle_height(self):
        #self.height_of_dot1_2 = (self.area * 2) / self.dot1_dot2
        #self.height_of_dot2_3 = (self.area * 2) / self.dot2_dot3
        self.height_of_dot3_1 = round((self.area * 2) / self.dot3_dot1, 2)
        return (self.height_of_dot3_1)

    def perimeter_triangle(self):
        self.perimeter = round(self.dot1_dot2 + self.dot2_dot3 + self.dot3_dot1, 2)
        return (self.perimeter)

data_triangle = triangle(3,3,4,4,5,3)
print('Длинна строны dot1_dot2 = {}, dot2_dot3 = {}, dot3_dot1 = {}'.\
      format(data_triangle.dot1_dot2 , data_triangle.dot2_dot3, data_triangle.dot3_dot1))
print('Периметр треугольника xy1_xy2_xy3 = {}'.format(data_triangle.perimeter_triangle()))
print('Площадь треугольника xy1_xy2_xy3 = {}'.format(data_triangle.area_of_triangle()))
print('Высота треугольника xy1_xy2_xy3, проведенная на основание стороны dot3_dot1 = {}'.\
      format(data_triangle.triangle_height()))

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math

class trapezium():

    def __init__(self, dot_x1, dot_y1, dot_x2, dot_y2, dot_x3, dot_y3, dot_x4, dot_y4):

        self.dot_x1 = dot_x1

        self.dot_y1 = dot_y1

        self.dot_x2 = dot_x2

        self.dot_y2 = dot_y2

        self.dot_x3 = dot_x3

        self.dot_y3 = dot_y3

        self.dot_x4 = dot_x4

        self.dot_y4 = dot_y4

    def side_length_dot1_dot2(self ):
        self.dot1_dot2 = round(math.fabs(math.sqrt(((int(self.dot_x2)\
                                - int(self.dot_x1))**2) + ((int(self.dot_y2)\
                                - int(self.dot_y1))**2))), 2)
        return (self.dot1_dot2)
    def side_length_dot2_dot3(self):
        self.dot2_dot3 = round(math.fabs(math.sqrt(((int(self.dot_x3)\
                                - int(self.dot_x2))**2) + ((int(self.dot_y3)\
                                - int(self.dot_y2))**2))), 2)
        return (self.dot2_dot3)
    def side_length_dot3_dot4(self):
        self.dot3_dot4 = round(math.fabs(math.sqrt(((int(self.dot_x4)\
                                - int(self.dot_x3))**2) + ((int(self.dot_y4)\
                                - int(self.dot_y3))**2))), 2)
        return (self.dot3_dot4)
    def side_length_dot4_dot1(self):
        self.dot4_dot1 = round(math.fabs(math.sqrt(((int(self.dot_x1)\
                                - int(self.dot_x4))**2) + ((int(self.dot_y1)\
                                - int(self.dot_y4))**2))), 2)
        return (self.dot4_dot1)

    def diagonal_dot1_3(self):
        self.diagonal_dot1_3 = round(math.fabs(math.sqrt(((int(self.dot_x3)\
                                    - int(self.dot_x1))**2) + ((int(self.dot_y3)\
                                    - int(self.dot_y1))**2))), 2)
        return (self.diagonal_dot1_3)

    def diagonal_dot2_4(self):
        self.diagonal_dot2_4 = round(math.fabs(math.sqrt(((int(self.dot_x4)\
                                    - int(self.dot_x2))**2) + ((int(self.dot_y4)\
                                    - int(self.dot_y2))**2))), 2)
        return (self.diagonal_dot2_4)

    def isoscience_test(self):
        self.diagonal_dot2_4 == self.diagonal_dot1_3
        return True

    def trapezium_height(self):
        self.height = round((math.sqrt((4*self.dot1_dot2**2)-(self.dot4_dot1 - self.dot2_dot3)**2))/2 , 2)
        return (self.height)

    def area_of_trapezium(self):
        self.area = round((((self.dot4_dot1 + self.dot2_dot3)/2)*self.trapezium_height()), 2)
        return (self.area)

    def perimeter_trapezium(self):
        self.perimeter = round(self.side_length_dot1_dot2() + self.side_length_dot2_dot3()\
                               + self.side_length_dot3_dot4()+ self.side_length_dot4_dot1(), 2)
        return (self.perimeter)

data_trapezium = trapezium(2,2,3,5,5,5,6,2)

if data_trapezium.isoscience_test():
    print('Яаляется ли трапеции xy1_xy2_xy3_xy4 равнобедренной = {}'.format( data_trapezium.isoscience_test()))
    print('Периметр равнобедренной трапеции xy1_xy2_xy3_xy4 = {}'.format(data_trapezium.perimeter_trapezium()))
    print('Площадь равнобедренной трапеции xy1_xy2_xy3_xy4 = {}'.format(data_trapezium.area_of_trapezium()))
    print('Высота равнобедренной трапеции xy1_xy2_xy3_xy4, проведенная на основание стороны dot4_dot1 = {}'.\
          format(data_trapezium.trapezium_height()))
    print('Сторона xy1_xy2 равнобедренной трапеции xy1_xy2_xy3_xy4 = {}'\
          .format(data_trapezium.side_length_dot1_dot2()))
    print('Сторона xy2_xy3 равнобедренной трапеции xy1_xy2_xy3_xy4 = {}'\
          .format(data_trapezium.side_length_dot2_dot3()))
    print('Сторона xy3_xy4 равнобедренной трапеции xy1_xy2_xy3_xy4 = {}'\
          .format(data_trapezium.side_length_dot3_dot4()))
    print('Сторона xy4_xy1 равнобедренной трапеции xy1_xy2_xy3_xy4 = {}'\
          .format(data_trapezium.side_length_dot4_dot1()))
    print('Диагональ xy1-xy3 трапеции xy1_xy2_xy3_xy4 = {}'.format(data_trapezium.diagonal_dot1_3()))
    print('Диагональ xy2-xy4 трапеции xy1_xy2_xy3_xy4 = {}'.format(data_trapezium.diagonal_dot2_4()))
else:
    print("Трапеция НЕ является равнобедренной")
    print('Диагональ xy1-xy3 трапеции xy1_xy2_xy3_xy4 = {}'.format(data_trapezium.diagonal_dot1_3()))
    print('Диагональ xy2-xy4 трапеции xy1_xy2_xy3_xy4 = {}'.format(data_trapezium.diagonal_dot2_4()))
    """
#normal
#
# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Human:
    def __init__(self, name, surname, father_name):
        self.name = name
        self.surname = surname
        self.father_name = father_name

    def full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.father_name

class ClassRoom():
    def __init__(self, class_room):
        self.class_room = {'class_number': int(class_room.split()[0]),
                          'class_letter': class_room.split()[1]
                           }
    def name_class(self):
        return str(self.class_room['class_number']) + ' ' + self.class_room['class_letter']


class Student(Human):
    def __init__(self, name, surname, father_name, class_room, mom, dad):
        Human.__init__(self, name, surname, father_name)
        self.class_room = class_room
        self.dad = dad
        self.mom = mom

    def get_a_class(self):
        return self.class_room

    def get_a_parents(self):
        return self.dad.full_name(), self.mom.full_name()

class Teacher(Human):
    def __init__(self, name, surname, father_name, classes, subject):
        Human.__init__(self, name, surname, father_name)
        self.classes = classes
        self.subject = subject

    def get_a_subject(self):
        return self.subject

    def get_a_classes(self):
        return self.classes

class_rooms = ['5 А','6 В','7 Б']

parents = [Human('Иван', 'Иванов', 'Александрович'),
           Human('Милана', 'Иванова', 'Егоровна'),
           Human('Петр', 'Петров', 'Алексеевич'),
           Human('Гала', 'Петрова', 'Олеговна'),
           Human('Михаил', 'Михайлов', 'Сергеевич'),
           Human('Мелиса', 'Михайлова', 'Андреевна'),
           Human('Альберт', 'Максвелл', 'Николович'),
           Human('Мария', 'Максвелл', 'Николваевна')
           ]


students = [Student('Иван', 'Ивановов', 'Иванович', str(class_rooms[0]), parents[1], parents[0]),
            Student('Петр', 'Петров', 'Петрович', str(class_rooms[1]), parents[3], parents[2]),
            Student('Михаил', 'Михайлов', 'Михайлович', str(class_rooms[2]), parents[5], parents[4]),
            Student('Евклид', 'Максвелл', 'Альбертович', str(class_rooms[2]), parents[7], parents[6])
            ]

teachers_class = [[class_rooms[0], class_rooms[2]], [class_rooms[1], class_rooms[0]], [class_rooms[2], class_rooms[1]]]

teachers = [Teacher('Егор', 'Фомичев', 'Олегович', str(teachers_class[0]), 'Физика'),
            Teacher('Юрий', 'Андреев', 'Петрович', str(teachers_class[1]), 'Математика'),
            Teacher('Игорь', 'Поляков', 'Андреевич', str(teachers_class[2]), 'Информатика')
           ]

full_list_all_classes = list([itm.get_a_class() for itm in students])

clas_name = '7 Б'

print(class_rooms)
print(full_list_all_classes)

students_in_class = [itm.full_name() for itm in students if itm.get_a_class() == clas_name]
print(students_in_class)

student = students[3]

list_subject_of_study = [itm for itm in teachers if student.get_a_class() in itm.get_a_classes()]

sub = [itm.subject for itm in list_subject_of_study]
print(student.full_name() + '-|>' + student.get_a_class() + \
      '-|>' +  ' '.join(map(lambda x: x.full_name(), list_subject_of_study)) + '-|>' + ' '.join(map(str, sub)))

his_parents = student.get_a_parents()
print(his_parents)

teacher_name = [itm.full_name for itm in list_subject_of_study]
print([itm.full_name() for itm in teachers if clas_name in itm.get_a_classes()])



#hard
# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
