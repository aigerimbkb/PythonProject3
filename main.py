#!/usr/bin/env python3
# coding=utf-8

import random


# функция для получения массива случайных чисел
def random_array(n, m=8, max_value=21):
    array = []  # основной массив
    for i in range(0, n):
        sub_array = []  # подмассив с числами
        for j in range(m):
            # от минимального числа (-10) до максимального -1 (max_value - 1 = 20) с шагом (1)
            number = random.randrange(-10, max_value, 1)
            sub_array.append(number)  # добавление случайного числа в подмассив
        array.append(sub_array)  # добавление подмассива в массив
    return array  # возвращается массив с подмассивами внутри


# функция для вывода массива
def print_array(array):
    print()
    for i in array:  # перебор по подмассивам(строкам)
        for j in i:  # перебор по элементам строк
            print("%5.1f\t" % j, end='')
        print()


# функция для нахождения элементов условия (в этом случае максимум и минимум,
# может быть количество нулей, количество отрицательных числе и т.д.)
def counting(array):
    print()
    # как начальное значение для макс/мин берется первый элемент массива
    max_value = array[0][0]
    min_value = array[0][0]
    for i in range(len(array)):
        for j in range(len(array[i])):
            e = array[i][j]
            if e > max_value:
                max_value = e
            if e < min_value:
                min_value = e
    print("Максимум: %d, минимум: %d" % (max_value, min_value))
    print()
    return max_value, min_value


def main():
    rowCount = 4
    colCount = 5
    # вызов функции рандома массива, которая возвращает полученный массив
    array = random_array(rowCount, colCount)  # можно изменить размер
    print("Условие задания:\n"
          "Если сумма значений таблицы меньше ста, \n"
          "то поменять местами максимальный и минимальный элементы таблицы, \n"
          "а вторую строку заменить на значения 0")

    # вызов функции вывода массива

    print_array(array)
    # вызов функции массива по условию, который возвращает элементы для проверки условия
    max_value, min_value = counting(array)

    while True:
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        key = input('Введите команду (1, 2 или 3): ')


        if key == '1':  # рандом, вывод и новые значения по условию нового массива
            array = random_array(rowCount, colCount)
            print_array(array)
            max_value, min_value = counting(array)

        elif key == '2':
            # проверка выполнения условия
            s=0
            for i in range(len(array)):
                for j in range(len(array[i])):
                    s = s + array[i][j]

            if s >= 100:
                print("Сумма значений таблицы больше ста: " + str(s))
                print("Задание не будет выполнено.")
            else:
                # выполнения результата совпадения условия,
                print("Cумма значений таблицы меньше ста (%d)" % s)

                a_max = a_min = array[0][0]  # Задаем начальное значение максимума и минимума равным ячейке [0][0]
                a_max_row = a_min_row = _max_col = a_min_col = 0  # Задаем координаты максимума и минимума равными [0][0]

                for row, r in enumerate(array):  # Перебираем строки
                    for col, cell in enumerate(r):  # Перебираем столбцы
                        #print("%5.1f\t" % cell, end=' ')
                        if (cell > a_max):  # Если текущая ячейка больше максимума, то изменяем данные о максумуме
                            a_max = cell
                            a_max_col = col
                            a_max_row = row
                        if (cell < a_min):  # Если текущая ячейка меньше минимума, то изменяем данные о минимуме
                            a_min = cell
                            a_min_col = col
                            a_min_row = row

                array[a_max_row][a_max_col] = a_min  # Поместим в место максимального элемента минимальное значение
                array[a_min_row][a_min_col] = a_max  # Поместим в место минимального элемента максимальное значение

                for i in range(len(array[1])):
                   array[1][i] = 0  # изменяем на 0

                print("Поменяли местами максимальный и минимальный элементы таблицы. ")
                print("Вторую строку заменили на значения 0. ")
                print_array(array)
                break  # выход из цикла
        elif key == '3':
            exit(0)  # выход из программы


if __name__ == '__main__':
    main()
