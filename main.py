# целые числа

def summ(x, y):  # сумма
    return x + y
print(summ(255, 34))


def multiply(x, y):  # умножение
    return x * y
print(multiply(5, 2))


def division_with(x, y):  # деление с остатком
    return x / y
print(division_with(20, 3))


def division(x, y):  # деление без остатка
    return x // y
print(division(20, 3))


def remainder(x, y):  # только остаток
    return x % y
print(remainder(20, 3))


def exponentiation(x, y):  # возведение в степень
    return x ** y
print(remainder(3, 4))


def pow1(x, y):  # возведение в степень
    return pow(x, y)
print(pow(3, 4))


def pow2(x, y, z):  # возведние в степень по модулю, 81/27=0
    return pow(x, y, z)
print(pow2(3, 4, 27))


d = {'dict': 1, 'dictionary': 2}  # создание словаря
d2 = dict(short='dict', long='dictionary')  # создание словара с помощью функции dict,
                                            # где параметры являются именновыми аргументами
d3 = dict([(1, 1), (2, 4)])  # создание словаря списком
d4 = dict.fromkeys(['a', 'b'])  # создание словара с помощью метода fromkeys, создает ключи
d5 = dict.fromkeys(['a', 'b'], 100)  # создание словара с помощью метода fromkeys и присваивание значения
d6 = {a: a ** 2 for a in range(7)}  # генератор словарей


list1 = list('список')  # создание списка при помощи метода list
s = []  # пустой список
l = ['s', 'p', ['isok'], 2]
c = [c * 3 for c in 'list']  # генератор списка
c2 = [c * 3 for c in 'list' if c != 'i']  # умножит каждую букву на 3 и не добавит 'i'
c3 = [c + d for c in 'list' if c != 'i' for d in 'spam' if d != 'a']  # добавит буквы двух слов,
                                                                      # кроме букв 'i' и 'a'