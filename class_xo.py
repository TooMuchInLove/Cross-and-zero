# -*- coding: utf-8 -*-
from time import sleep

class xo: # CLASS CROSS & ZERO
    # CREATING FIELD
    __Field = [i for i in range(1, 10)]
    # FLAG [ X or O ]
    __flag = True
    __count = 0

    def __init__(self, digit): # Инициализируем переменные
        self.digit = int(digit)

    def timer(self=None): # ЗАДЕРЖКА после победы
        for T in range(5, 0, -1):
            print(f"Программа завершится через {T}...")
            sleep(1) # ЗАДЕРЖКА

    def outwon(self): # ВЫВОД ПОБЕДИТЕЛЯ
        print(self)
        xo.timer() # Функция ЗАДЕРЖКИ
        exit() # ВЫХОД из программы

    def win(*LIST): # Определяем ПОБЕДИТЕЛЯ
        for i in range(3): # Проверяем СТРОКИ, СТОЛБЦЫ и ДИАГОНАЛИ
            if (LIST[i * 2 + i] == LIST[i * 2 + i + 1] == LIST[i * 2 + i + 2]): # LINES [ 1, 2, 3 ]
                xo.outwon(f"Winner [" + LIST[i * 2 + i] + "]!") # Функция ВЫВОДА
            if (LIST[i] == LIST[i + 3] == LIST[i + 6]): # COLUMN [ 1, 2, 3 ]
                xo.outwon(f"Winner [" + LIST[i] + "]!") # Функция ВЫВОДА
            if (i == 2): break
            if (LIST[i * 2] == LIST[i * 0 + 4] == LIST[abs(i * 2 - 8)]): # DIAGONAL [ 1, 2 ]
                xo.outwon(f"Winner [" + LIST[i * 2] + "]!") # Функция ВЫВОДА

    def draw(*LIST): # ОТРИСОВКА
        print(f"+---+---+---+\n| {LIST[0]} | {LIST[1]} | {LIST[2]} |\n"
              f"+---+---+---+\n| {LIST[3]} | {LIST[4]} | {LIST[5]} |\n"
              f"+---+---+---+\n| {LIST[6]} | {LIST[7]} | {LIST[8]} |\n+---+---+---+")

    def out_in_console(self): # ВЫВОД ФОРМЫ В КОНСОЛЬ
        for i in range(len(xo.__Field)):
            ELEM = str(xo.__Field[self.digit - 1])
            if (not ELEM.isdigit()): # Если введена одна и таже ЦИФРА несколько раз
                print("This cell is already occupied!")
                break
            if (self.digit == xo.__Field[i]):
                del xo.__Field[i] # Удаление элемента ячейки для замены
                if xo.__flag: # TRUE
                    xo.__Field.insert(i, "x")
                    xo.__flag = False
                else:
                    xo.__Field.insert(i, "o")
                    xo.__flag = True

                xo.draw(*xo.__Field) # ОТРИСОВКА
                xo.win(*xo.__Field) # ПРОВЕРКА НА ПОБЕДИТЕЛЯ
                xo.__count += 1 # СЧЁТЧИК
                if (xo.__count == len(xo.__Field)):
                    xo.outwon("Nobody won!") # Функция ВЫВОДА
                break
