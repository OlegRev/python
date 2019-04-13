#n1 = 1
#n2 = n1
#n2 = 4
#print(n1)
#test1 = [1, 2, 3, 4, 5]
#test2 = test1
#test2.append("STROKA")
#print(test1)
#test2=test1[:]
#test2.append('NOVAi')
#print(test1)
#test2 = test1.copy()
#test2.append("NEW")
#print(test1)
#print(test2)
#test2=test1
#nom1 = 22
#num2 = num1
#test_str = str('sndkhnjkshdkjfh')
#
#test_str2 = test_str
#test_str2[3] = 'THIS NEW'
#test_str2.replace('this is new string')
#test = [1, 2, 3, 4, 5, 6]
#test2=test[0]
#test2.append(22)
#print(test)
#test2 = test[0].copy()
#
#matrix = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9],
#          ]
#for i, line in enumerate(matrix):
#
#    for j, item in enumerate(line):
#        print(f"matrix[{i}][{j}] === {matrix[i][j]}")
#        print(item + matrix[i+1][j])
#for line in matrix:
#    print(line)
#r_matrix = list(map(list, zip(*matrix))) #перевернуть матрицу
#print('#'*30)
#for line in r_matrix:
#    print(line)
##zip() берет симетричные элементы и создает кортеж
test = {1:'hello', 2:'', 3:"MAY BY"}
for _, itm in test.items():
    print(itm or "NICHEGO HET")
print(test[2] if test[2] else 'NET')

#1 is 1
#2 is 3
#a= 1
#b=1
#a is b
#test = [1, 2, 3]
#test2 = test
#test is test2
#test2 = test.copy()
#if test == test2:
#    print('OK')
#test is test2
#if not a:  # полезно пользоваться
#
temp = []
for itm in range(1, 100):
    temp.append(itm)
print(temp)
temp2 = [itm for itm in range(1, 100)]
print(temp2)
temp2 = [itm for itm in range(1, 100) if itm % 2]
print(temp2)
tem3 = [itm for itm in temp if itm%2]
print(tem3)
def tmp(a):
    return a+3
temp4 = [tmp(itm) for itm in temp ]
print(temp4)
temp4 = [tmp(itm) for itm in temp if itm%2]
print(temp4)
keys = [1, 2, 3, 4, 5]
val = ["1", "2", "3", "4", "5"]
#test_dict = {kay: value for key, value in zip(keys, val)}
#test_dict = {kay: value for key, value in zip(keys, val)}


temp = [[idx for idx in range(value)] for value in [itm for itm in range(12)]]

a = "HELLO \n WORLD"
print(a)
b = r"HELLO \n WORLD" #сырые строки используются регулярных выражениях
print(b)
import re
string = "это текст в котором надо найти слово Жаба"
patern = r"Жаба"
re.search(patern, string)
#for itm in re.search(patern, string)
obj = re.search(patern, string)
if obj:
    print("OK")
patern_1 = r"Жаба$"
obj2 = re.search(patern_1, string)
if obj2:
    print("OK2")
#print(obj2.pos)
print(obj2.group())
print(obj2.start())
print(string[obj2.start(): obj2.end()])

def email_search(text): # патерн поислка exempl@exempl.exempl
    re_template = r"[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,6}"
    mail = re.findall(re_template, text, re.MULTILINE)
    return mail
test_string = 'sjdfjlsjdjklsjdfjlskd  sdfjl ksdjkflskdlfjksjlljll  jja kjklj lkj llj aklsjdkl@lasjdlka.alksdj'
print(email_search(test_string))

def email_search(text): # патерн поислка exempl@exempl.exempl
    re_template = r"[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,6}"
    rx = re.compile(re_template)
    mail = re.findall(re_template, text, re.MULTILINE)
    return mail


re_template = r"\d"
tm_str = 'asfmkjasdflkj2lf2j3fkfjdflkkl3jj45980j09fj'

print(re.findall(re_template, tm_str))
print('#'*40)
try:
    print(10/0)
except ZeroDivisionError or IndexError as e:
    print(e)
    print('#'*30)
finally:
    print("Едем дальше")
print("*"*35)
#te_list = [1, 2]
#print(te_list[3])
a = 'qwe'
try:
    a = int(a)
    print(type(a))
except ValueError:
    print(a)
except IndexError:
    print("NO")


try:
    a = int(a)
    print(type(a))
except Exception:
    print(a)
