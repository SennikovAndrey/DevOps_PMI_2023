print('Введите два числа:')
a, b = list(map(int, input().split()))
if (a%b == 0 or b%a ==0):
    if (a%b ==0):
        print('a делится на b')
    else:
        print('b делится на a')
    print('P.s. Макс лох!')
else:
    print('a и b не делятся друг на друга!')
    print('Все равно Макс лох')