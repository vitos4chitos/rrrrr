import random

D = dict()
proverka = "йцукенгшщзхъфывапролджэячсмитьбюё"
a = 1
while a != 3:
    if a == 1:
        print("Введите название файла, из которого будет производиться чтение текста")
        nazvanie = input()
        f = open(nazvanie)
        for line in f:
            sv = line.split()
            for i in range(len(sv)):
                sv[i] = sv[i].lower()
                if sv[i][len(sv[i]) - 1] == '.' or sv[i][len(sv[i]) - 1] == ';' or sv[i][len(sv[i]) - 1] == '?' or sv[i][len(sv[i]) - 1] == '!' or sv[i][len(sv[i]) - 1] == ':':
                    while len(sv[i]) != 0 and proverka.rfind(sv[i][len(sv[i]) - 1]) == -1:
                        sv[i] = sv[i][:len(sv[i]) - 1]
                    while len(sv[i]) != 0 and proverka.find(sv[i][0]) == -1:
                        sv[i] = sv[i][1:len(sv[i])]
                    if sv[i] not in D and sv[i] != '':
                        D[sv[i]] = D.get(sv[i], [])
                    if sv[i] != '':
                        D[sv[i]] += ["."]
                else:
                    while len(sv[i]) != 0 and proverka.rfind(sv[i][len(sv[i]) - 1]) == -1:
                        sv[i] = sv[i][:len(sv[i]) - 1]
                    while len(sv[i]) != 0 and proverka.find(sv[i][0]) == -1:
                        sv[i] = sv[i][1:len(sv[i])]
                    if sv[i] not in D and sv[i] != '':
                        D[sv[i]] = D.get(sv[i], [])
                    if sv[i] != '' and i != len(sv) - 1:
                        s = sv[i + 1].lower()
                        while len(s) != 0 and proverka.find(s[0]) == -1:
                            s = s[1:len(s)]
                        while len(s) != 0 and proverka.rfind(s[len(s) - 1]) == -1:
                            s = s[:len(s) - 1]
                        if s != '':
                            D[sv[i]] += [s]
        words = list(D.keys())
        print("Ваш текст обработан, нажмите 1, чтобы занести ещё один текст, или 2, чтобы создать предложение")
        a = int(input())
        while a != 1 and a != 2:
            print("Вы нажали не ту кнопку. Вот варианты ответа:")
            print("1 - Занести ещё один текст")
            print("2 - Создать предложение")
            a = int(input())
    elif a == 2:
        word = random.choice(words)
        while word != '.':
            print(word, end=" ")
            word = random.choice(list(D[word]))
        print('.')
        print("1 - Занести ещё один текст")
        print("2 - Создать предложение")
        print("3 - Выйти из программы")
        a = int(input())
        while a != 1 and a != 2 and a != 3:
            print("1 - Занести ещё один текст")
            print("2 - Создать предложение")
            print("3 - Выйти из программы")
            a = int(input())
print("Спасибо, что воспользовались программой, до скорых встреч")
