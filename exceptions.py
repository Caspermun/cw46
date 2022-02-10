import errno
import os
import socket
import subprocess
import sys
import warnings
from xmlrpc import server

import requests as requests
from requests.exceptions import ConnectionError

try:
    exit(33)
except SystemExit as e:
    print(sys.exc_info())
    print('Exit code: %s' % e.code)


def my_generator():
    try:
        for i in range(5):
            yield i
    except GeneratorExit:
        print(sys.exc_info())
        print("Not get all value")


g = my_generator()
print(next(g))
g.close()

try:
    z = [5, 9, 7]
    i = iter(z)
    print(i)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
except StopIteration as e:  # возникает если заканчивается элемент для итерации
    print(sys.exc_info())
    print('Iteration stopped')

try:
    7 / 0
except ArithmeticError as e:  # арифметическая ошибка
    print(sys.exc_info())
    print('This is an example of catching ArithmeticError')

i = 1
try:
    f = 3.0 ** i
    for i in range(100):
        print(i, f)
        f = f ** 2
except OverflowError as err:  # возникает, когда результат арифметической операции слишком велик для представления
    print(sys.exc_info())
    print('Overflowed after ', f, err)

try:
    x = 11 / 0
    print(x)
except ZeroDivisionError as e:  # деление на ноль
    print(sys.exc_info())
    print(e)

try:
    assert (-1 > 0)  # выражение в функции assert ложно
except AssertionError as e:
    print(sys.exc_info())

try:
    x = 10
    x.append(6)
except AttributeError as e:  # объект не имеет данного атрибута
    print(sys.exc_info())
    print(e)

try:
    from time import datetime  # не удалось импортирование модуля или его атрибута
except ImportError as e:
    print(sys.exc_info())
    print(e)

try:
    foo = ['a', 's', 'd']
    print(foo[5])
except IndexError as e:  # индекс не входит в диапазон элементов
    print(sys.exc_info())
    print(e)

try:
    s = {'a': 5, 'b': 7}['c']  # несуществующий ключ
except KeyError:
    print(sys.exc_info())

try:
    x = ['a', 'b']
    print(y)
except NameError:  # не найдено переменной с таким именем
    print(sys.exc_info())

try:
    def f():
        a += 1


    f()
except UnboundLocalError:  # нет переменной над функцией,вы пытаетесь присвоить значение локальной переменной до того,
    # как она была объявлена
    print(sys.exc_info())

try:
    print(os.ttyname(1))
except OSError:  # системная ошибка
    print(sys.exc_info())

try:
    r = requests.get("http://example.com", timeout=0.001)
except ConnectionError as e:  # базовый класс для исключений, связанных с подключениями
    print(sys.exc_info())

try:
    os.mkdir('main.py')
except FileExistsError as e:  # попытка создать существующий файл или папку
    if e.errno == errno.EEXIST:
        print('Directory not created.')
        print(sys.exc_info())
    else:
        raise

try:
    with open('main.csv', 'r') as file:
        file = file.read()
        file.encode('UTF-8')
except FileNotFoundError:  # файл не найден
    print(sys.exc_info())

try:
    with open('venv', 'r') as file:
        file = file.read()
        file.encode('UTF-8')
except IsADirectoryError:  # ожидался файл, но это директория
    print(sys.exc_info())

try:
    img_list = os.listdir('main.py')
except NotADirectoryError:  # ожидалась папка, но это файл
    print(sys.exc_info())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.0000001)
try:
    s.connect(("www.python.org", 80))
except socket.timeout:  # закончилось время ожидания
    print(sys.exc_info())

import weakref


class Foo(object):
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('(Deleting %s)' % self)


obj = Foo('obj')
p = weakref.proxy(obj)
print('BEFORE:', p.name)
try:
    obj = None
    print('AFTER:', p.name)
except ReferenceError:  # попытка доступа к атрибуту со слабой ссылкой
    print(sys.exc_info())


class C(object):
    def f(self):
        raise NotImplementedError()


try:
    C().f()
except NotImplementedError:  # возникает, когда абстрактные методы класса
    # требуют переопределения в дочерних классах
    print(sys.exc_info())

try:
    print(eval('geeks for geeks'))
except SyntaxError:  # синтаксическая ошибка
    print(sys.exc_info())

try:
    geek = "Geeks"
    num = 4
    print(geek + num + geek)
except TypeError:  # операция применена к объекту несоответствующего типа
    print(sys.exc_info())

try:
    print(int('a'))
except ValueError:  # функция получает аргумент правильного типа, но некорректного значения
    print(sys.exc_info())

try:
    warnings.warn("deprecated", DeprecationWarning)
except Warning:  # предупреждения
    print(sys.exc_info())