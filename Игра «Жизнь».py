import random
import tkinter

print("Приветсвую в симуляторе океана")
print("Введите размер океана(целое число, которое задаст сторону квадрата карты)")
n = int(input())
print("Для простоты восприятия игры были добавлены условные обозначения:")
print("^ - склала")
print("$ - креветка")
print("% - рыба")
print("И пустое поле, если в этом месте ничего нет")
print()
print("Создать океан случайным образом или вы введёте его с клавиатуры")
print("1  - Случайно")
print("2 - Ввести с клавиатуры")
s = int(input())
while s != 1 and s != 2:
    print("Вы нажали не ту кнопку. Вот варианты ответа:")
    print("1 - Случайно")
    print("2 - Ввести с клавиатуры")
    s = int(input())
if s == 1:
    a = [0] * n
    for i in range(n):
        a[i] = [0] * n
    for i in range(n):
        for j in range(n):
            a[i][j] = random.choice(['^', '$', '%', ' '])
    print("Вот ваша карта")
    print()
    for i in range(n):
        for j in range(n):
            print(a[i][j], end="")
        print()
    print("Хотите изменить её?")
    print("1 - Да")
    print("2 - Нет")
    s = int(input())
    while s != 1 and s != 2:
        print("Вы нажали не ту кнопку. Вот варианты ответа:")
        print("1 - Да")
        print("2 - Нет")
        s = int(input())
    while s == 1:
        print("Хорошо, что вы хотите изменить?")
        print("1 - размер")
        print("2 - карту")
        s = int(input())
        while s != 1 and s != 2:
                print("Вы нажали не ту кнопку. Вот варианты ответа:")
                print("1 - Изменить размер")
                print("2 - Изменить карту")
                s = int(input())
        if s == 1:
            print("Введите размер океана(целое число, которое задаст сторону квадрата карты)")
            n = int(input())
            a = [0] * n
            for i in range(n):
                a[i] = [0] * n
            for i in range(n):
                for j in range(n):
                    a[i][j] = random.choice(['^', '$', '%', ' '])
            print("Вот ваша карта")
            print()
            for i in range(n):
                for j in range(n):
                    print(a[i][j], end="")
                print()
            print("Хотите изменить её?")
            print("1 - Да")
            print("2 - Нет")
            s = int(input())
            while s != 1 and s != 2:
                print("Вы нажали не ту кнопку. Вот варианты ответа:")
                print("1 - Да")
                print("2 - Нет")
                s = int(input())
        elif s == 2:
            for i in range(n):
                for j in range(n):
                    a[i][j] = random.choice(['^', '$', '%', ' '])
            print("Вот ваша карта")
            print()
            for i in range(n):
                for j in range(n):
                    print(a[i][j], end="")
                print()
            print("Хотите изменить её?")
            print("1 - Да")
            print("2 - Нет")
            s = int(input())
            while s != 1 and s != 2:
                print("Вы нажали не ту кнопку. Вот варианты ответа:")
                print("1 - Да")
                print("2 - Нет")
                s = int(input())
elif s == 2:
    print("Введите океан")
    a = [0] * n
    for i in range(n):
        a[i] = list(input())
b = [0] * n
for i in range(n):
    b[i] = [0] * n
print("Чтобы смотреть, как развивается ваш океан в каждый отрезок времени, нажимайте 1")
print("Чтобы выйти из симуляции нажмите 2")
s = int(input())
while s != 1 and s != 2:
    print("Вы нажали не ту клавишу")
    print("Чтобы смотреть, как развивается ваш океан в каждый отрезок времени, нажимайте 1")
    print("Чтобы выйти из симуляции нажмите 2")
    s = int(input())
while s == 1:
    for i in range(n):
        for j in range(n):
            b[i][j] = a[i][j]
            if a[i][j] != '^':
                q = 0
                r = 0
                if i == 0:
                    if j == 0:
                        if a[i + 1][j + 1] == '$':
                            q += 1
                        elif a[i + 1][j + 1] == '%':
                            r += 1
                        if a[i][j + 1] == '$':
                            q += 1
                        elif a[i][j + 1] == '%':
                            r += 1
                        if a[i + 1][j] == '$':
                            q += 1
                        elif a[i + 1][j] == '%':
                            r += 1
                    elif j == n - 1:
                        if a[i + 1][j] == '$':
                            q += 1
                        elif a[i + 1][j] == '%':
                            r += 1
                        if a[i + 1][j - 1] == '$':
                            q += 1
                        elif a[i + 1][j - 1] == '%':
                            r += 1
                        if a[i][j - 1] == '$':
                            q += 1
                        elif a[i][j - 1] == '%':
                            r += 1
                    else:
                        if a[i][j - 1] == '$':
                            q += 1
                        elif a[i][j - 1] == '%':
                            r += 1
                        if a[i + 1][j - 1] == '$':
                            q += 1
                        elif a[i + 1][j - 1] == '%':
                            r += 1
                        if a[i + 1][j] == '$':
                            q += 1
                        elif a[i + 1][j] == '%':
                            r += 1
                        if a[i + 1][j + 1] == '$':
                            q += 1
                        elif a[i + 1][j + 1] == '%':
                            r += 1
                        if a[i][j + 1] == '$':
                            q += 1
                        elif a[i][j + 1] == '%':
                            r += 1
                elif i == n - 1:
                    if j == 0:
                        if a[i - 1][j] == '$':
                            q += 1
                        elif a[i - 1][j] == '%':
                            r += 1
                        if a[i - 1][j + 1] == '$':
                            q += 1
                        elif a[i - 1][j + 1] == '%':
                            r += 1
                        if a[i][j + 1] == '$':
                            q += 1
                        elif a[i][j + 1] == '%':
                            r += 1
                    elif j == n - 1:
                        if a[i][j - 1] == '$':
                            q += 1
                        elif a[i][j - 1] == '%':
                            r += 1
                        if a[i - 1][j - 1] == '$':
                            q += 1
                        elif a[i - 1][j - 1] == '%':
                            r += 1
                        if a[i - 1][j] == '$':
                            q += 1
                        elif a[i - 1][j] == '%':
                            r += 1
                    else:
                        if a[i][j - 1] == '$':
                            q += 1
                        elif a[i][j - 1] == '%':
                            r += 1
                        if a[i - 1][j - 1] == '$':
                            q += 1
                        elif a[i - 1][j - 1] == '%':
                            r += 1
                        if a[i - 1][j] == '$':
                            q += 1
                        elif a[i - 1][j] == '%':
                            r += 1
                        if a[i - 1][j + 1] == '$':
                            q += 1
                        elif a[i - 1][j + 1] == '%':
                            r += 1
                        if a[i][j + 1] == '$':
                            q += 1
                        elif a[i][j + 1] == '%':
                            r += 1
                else:
                    if j == 0:
                        if a[i - 1][j] == '$':
                            q += 1
                        elif a[i - 1][j] == '%':
                            r += 1
                        if a[i - 1][j + 1] == '$':
                            q += 1
                        elif a[i - 1][j + 1] == '%':
                            r += 1
                        if a[i][j + 1] == '$':
                            q += 1
                        elif a[i][j + 1] == '%':
                            r += 1
                        if a[i + 1][j + 1] == '$':
                            q += 1
                        elif a[i + 1][j + 1] == '%':
                            r += 1
                        if a[i + 1][j] == '$':
                            q += 1
                        elif a[i + 1][j] == '%':
                            r += 1
                    elif j == n - 1:
                        if a[i - 1][j] == '$':
                            q += 1
                        elif a[i - 1][j] == '%':
                            r += 1
                        if a[i - 1][j - 1] == '$':
                            q += 1
                        elif a[i - 1][j - 1] == '%':
                            r += 1
                        if a[i][j - 1] == '$':
                            q += 1
                        elif a[i][j - 1] == '%':
                            r += 1
                        if a[i + 1][j - 1] == '$':
                            q += 1
                        elif a[i + 1][j - 1] == '%':
                            r += 1
                        if a[i + 1][j] == '$':
                            q += 1
                        elif a[i + 1][j] == '%':
                            r += 1
                    else:
                        if a[i - 1][j - 1] == '$':
                            q += 1
                        elif a[i - 1][j - 1] == '%':
                            r += 1
                        if a[i - 1][j] == '$':
                            q += 1
                        elif a[i - 1][j] == '%':
                            r += 1
                        if a[i - 1][j + 1] == '$':
                            q += 1
                        elif a[i - 1][j + 1] == '%':
                            r += 1
                        if a[i][j - 1] == '$':
                            q += 1
                        elif a[i][j - 1] == '%':
                            r += 1
                        if a[i][j + 1] == '$':
                            q += 1
                        elif a[i][j + 1] == '%':
                            r += 1
                        if a[i + 1][j - 1] == '$':
                            q += 1
                        elif a[i + 1][j - 1] == '%':
                            r += 1
                        if a[i + 1][j] == '$':
                            q += 1
                        elif a[i + 1][j] == '%':
                            r += 1
                        if a[i + 1][j + 1] == '$':
                            q += 1
                        elif a[i + 1][j + 1] == '%':
                            r += 1
                if a[i][j] == '%':
                    if r == 2 or r == 3:
                        b[i][j] = '%'
                    else:
                        b[i][j] = ' '
                elif a[i][j] == '$':
                    if q == 2 or q == 3:
                        b[i][j] = '$'
                    else:
                        b[i][j] = ' ';
                elif a[i][j] == ' ':
                    if r == 3:
                        b[i][j] = '%'
                    elif q == 3:
                        b[i][j] = '$'
                    else:
                        b[i][j] = ' ';
    if a == b:
        print("Дальше будет всё одинаково, поэтому симуляция заканчивается")
        s = 2
    else:
        for i in range(n):
            for j in range(n):
                a[i][j] = b[i][j]
        print("Вот ваша карта")
        print()
        for i in range(n):
            for j in range(n):
                print(a[i][j], end="")
            print()
        print("Чтобы продолжить смотреть, как развивается ваш океан в каждый отрезок времени,  нажимайте 1")
        print("Чтобы выйти из симуляции нажмите 2")
        s = int(input())
        while s != 1 and s != 2:
            print("Вы нажали не ту клавишу")
            print("Чтобы продолжить смотреть, как развивается ваш океан в каждый отрезок времени,  нажимайте 1")
            print("Чтобы выйти из симуляции нажмите 2")
            s = int(input())
if s == 2:
    print("Перезапустите программу, чтобы заново начать симуляцию")
