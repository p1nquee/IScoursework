'''Нам нужно ПО, которое мы собираемся обеспечить защитой. Поскольку нам не
важно что за программа будет защищена, то пусть это будет простейший
калькулятор, выполняющий только сложение или вычитание двух чисел.
'''
key = str(input('Введите ключ активации: ')) #Нужно дать на вход программе серийный ключ, который мы получили из генератора ключа.
def licensee(x):
    count1 = 0
    count2 = 0
    l = []
    k = key.split('-')      #Разделим наш ключ на две четвёрки.
    a = list(k[0])          #Первая четвёрка
    b = list(k[1])          #Вторая четвёрка
    for i in range(4):      #Ниже идёт проверка условий, получаемых наложением условий на ключ генератором.
        if 47 < ord(a[i]) < 58:
            a[i] = int(a[i])
        else:
            a[i] = ord((a[i]))
        if 47 < ord(b[i]) < 58:
            b[i] = int(b[i])
        else:
            b[i] = ord((b[i]))
#    print(a,b)
    for i in range(4):
        if 65 <= a[i] < 91:
            count1 += 1
#            print(1)
            l.append(i)
    if count1 == 2:
#        print(2)
        if 64 < a[l[0]] < 78 and 77 < a[l[1]] < 91 or 64 < a[l[1]] < 78 and 77 < a[l[0]] < 91:
#            print(3)
            if 0 <= a[0] <= 9 and a[0] % 2 == 0 and 64< a[1] < 91 and a[1] % 2 == 0 and 0 <= a[2] < 10 and 64 < a[3] < 91 or 64 < a[0] < 91 and 0 <= a[2] < 10 and a[2] % 2 == 1 and 64< a[1] < 91 and a[1] % 2 == 0 and 0 <= a[3] < 10  or 0 <= a[0] <= 9 and a[0] % 2 == 0 and 0 <= a[1] < 10 and 64 < a[2] < 91 and 64 < a[3] < 91 and a[2] % 2 == 1 or 64 < a[0] < 91 and 0 <= a[2] < 10 and a[2] % 2 == 1 and 0 <= a[1] < 10 and 64 < a[3] < 91 and a[3] % 2 == 1:
#                print(4)
                l = []
                for i in range(4):
                    if 0 <= b[i] < 10:
                        count2 += 1
                        l.append(i)
#                        print(5)
                if count2 == 1:
#                    print(6)
                    if 64 < b[0] < 91 and 0 <= b[1] < 10 and 64 < b[2] < 91 and 64 < b[3] < 91:
                        print('Поздравляю! Продукт активирован!')
                    else:
                        print('Сожалею, но ваш ключ недействителен.')
                        raise SystemExit        #Для того, чтобы пользователь не получил доступа к программе в случае несовпадения серийного ключа, я воспользовался вызовом ошибки, которая моментально прекращает работу программы.
                elif count2 == 3:
                    if 0 <= b[0] < 10 and 64 < b[1] < 91 and 0 <= b[2] < 10 and 0 <= b[3] < 10:
                        print('Поздравляю! Продукт активирован!')
                    else:
                        print('Сожалею, но ваш ключ недействителен.')
                        raise SystemExit
                elif count2 == 2:
                    if b[l[0]] + b[l[1]] > 5:
#                        print(7)
                        if 0 <= b[0] < 10 and 0 <= b[1] < 10 and 64 <= b[2] < 91 and 64 <= b[3] < 91:
                            print('Поздравляю! Продукт активирован!')
                        else:
                            print('Сожалею, но ваш ключ недействителен.')
                            raise SystemExit
                    elif b[l[0]] + b[l[1]] < 5:
                        if 64 <= b[0] < 91 and 0 <= b[1] < 10 and 64 <= b[2] < 91 and 0 <= b[3] < 10:
                            print('Поздравляю! Продукт активирован!')
                        else:
                            print('Сожалею, но ваш ключ недействителен.')
                            raise SystemExit
            else:
                print('Сожалею, но ваш ключ недействителен.')
                raise SystemExit
        else:
            print('Сожалею, но ваш ключ недействителен.')
            raise SystemExit
    else:
        print('Сожалею, но ваш ключ недействителен.')
        raise SystemExit
licensee(key)


d = str(input('Введите действие, которое хотите произвести. (+, если сложение, - если вычитание): '))
if d == '+' or d == '-':
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    if d == '+':
        z = x + y
        print(z)
    elif d == '-':
        z = x - y
        print(z)
else:
    print('Вообще-то надо было ввести + или -, а не "',d,'"!!! Так что программа не сработает :)')