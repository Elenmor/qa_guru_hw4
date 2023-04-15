def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25

    output = f"Привет, {name}! Тебе {age} лет."
    print(output)

    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20


    perimeter = 2 * a + 2 * b
    print(perimeter)
    assert perimeter == 60


    area = a * b
    print(area)
    assert area == 200

import math
pi = math.pi

def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23

    area = pi * (r ** 2)
    print(area)
    assert area == 1661.9025137490005


    length = 2 * pi * r
    print(length)
    assert length == 144.51326206513048

import random
def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    """


    l = [random.randint (0, 100) for _ in range (10)]
    l.sort()
    print(l)
    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    l= list(set(l))
    print(l)
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Выведите на экран все значения словаря.
    Подсказка: используй встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]

    keys = ["a", "b", "c", "d", "e"]
    values = [1, 2, 3, 4, 5]
    d = dict (zip(keys, values))
    print(f'values: {d.values()}')

    assert isinstance(d, dict)
    assert len(d) == 5


