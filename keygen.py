'''Пусть суть нашего ключа заключается в том, что в первой четвёрке 
содержится две случайные цифры и две буквы, причём одна буква - из первой половины английского 
алфавита, а вторая - из второй половины. Вторая четвёрка - от одной до трёх цифр
и от одной до трёх букв, причем, если в сумме цифры превышают 10, то одна из 
букв -из первой половины алфавита, а остальные - из второй. Иначе - все буквы -из второй
половины алфавита

Пусть порядок символов в четвёрках тоже подчиняется определённым правилам, а 
именно:
в первой четвёрке:
если первое сгенерированное случайным образом число - чётное, то на первом
месте стоит это число. Иначе - вторая сгенерированная буква. Если первая
сгенерированная буква имеет чётный порядок в алфавите, то она стоит на втором
месте. иначе - на втором месте ставится вторая цифра. Третье и четвёртое место
символы расставляются в порядке их генерации в коде;
во второй четвёрке:
если количество цифр - нечетное, и если цифра одна, идёт последовательность:
первая буква, цифра, вторая буква, третья буква. Если цифры три, то идёт последовательность:
первая цифра, буква, затем вторая и третья цифры. Иначе - если две цифры в сумме
дают больше пяти, то идёт последоватьельность: первая цифра, вторая цифра,
первая буква, вторая буква. Иначе - последовательность: вторая буква, вторая
цифра, первая буква, первая цифра.
'''

import random             #random - библиотека, из которой нам нужен randint, позволяющий получить случайное число.
def keygen(x):            #Создадим функцию keygen (генератор ключа)
    for q in range(x):    #Весь цикл генерации ключа пройдёт x раз. то есть, мы получим x ключей.
        key = []
        f = ''
        for i in range(2):#Поскольку мы разбили ключ на две четвёрки, то мы получим ключ, составленный из двух четвёрок, поэтому данный цикл пройдёт два раза.
            if i == 0:    #В данном цикле пройдёт генерация первой четвёрки ключа
                p = random.randint(0,9)
                j = random.randint(0,9)
                a = random.randint(65,90) #В кодировке Python'а английский алфавит заглавных букв пронумерован с 65 до 90 включительно.
                if 64 < a < 77:
                    b = random.randint(78,90)
                else:
                    b = random.randint(65,77)
                if p % 2 == 0:
                    key.append(str(p))
                    p = ''
                else:
                    key.append(str(chr(b)))
                    b = ''
                if a % 2 == 0:
                    key.append(str(chr(a)))
                    a = ''
                else:
                    key.append(str(j))
                    j = ''
                if type(p) == int:
                    key.append(str(p))
                if type(j) == int:
                    key.append(str(j))
                if type(a) == int:
                    key.append(str(chr(a)))
                if type(b) == int:
                    key.append(str(chr(b)))
                if i != 3:
                    key.append('-')


            if i == 1:        #В данном цикле пройдёт генерация первой четвёрки ключа
                del a, b
                n = random.randint(1,3)
                s = []
                for t in range(n):
                    d = random.randint(0,9)
                    s.append(d)
#                print(n,s)
                if sum(s) > 10:
                    if len(s) == 2:
                        a = random.randint(65,90)
                        key.append(str(s[0]))
                        key.append(str(s[1]))
                        key.append(str(chr(a)))
#                        print(n,s,a)
                        if 64 < a < 77:
                            b = random.randint(78,90)
                            key.append(str(chr(b)))
#                            print(n,s,a,b)
                        else:
                            b = random.randint(65,77)
                            key.append(str(chr(b)))
#                            print(n,s,a,b)
                    elif len(s) == 3:
                        a = random.randint(65,77)
                        key.append(str(s[0]))
                        key.append(str(chr(a)))
                        key.append(str(s[1]))
                        key.append(str(s[2]))
#                        print(n,s,a)
                else:
                    a = random.randint(78,90)
                    b = random.randint(78,90)
                    c = random.randint(78,90)
                    if len(s) % 2 == 1:
#                        print(n,s,a,b)
                        if len(s) == 1:
                            key.append(str(chr(a)))
                            key.append(str(s[0]))
                            key.append(str(chr(b)))
                            key.append(str(chr(c)))
#                            print(n,s,a,b,c)
#                            print(key)
                        else:
                            key.append(str(s[0]))
                            key.append(str(chr(a)))
                            key.append(str(s[1]))
                            key.append(str(s[2]))
#                            print(n,s,a)
#                            print(key)
                    else:
                        if sum(s) > 5:
                            key.append(str(s[0]))
                            key.append(str(s[1]))
                            key.append(str(chr(a)))
                            key.append(str(chr(b)))
#                            print(n,s,a,b)
#                            print(key)
                        else:
                            key.append(str(chr(b)))
                            key.append(str(s[1]))
                            key.append(str(chr(a)))
                            key.append(str(s[0]))
#                            print(n,s,a,b)
#                            print(key)
                for i in range(9):
                    f += key[i]
        print(f)
keygen(1)                       #теперь осталось лишь обратиться к нашей функции, чтобы на выход получить ключ.