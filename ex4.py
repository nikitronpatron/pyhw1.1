## Программа загадывает число от 0 до 1000.
## Необходимо угадать число за 10 попыток.
## Программа должна подсказывать «больше» или «меньше» после каждой попытки.
## Для генерации случайного числа используйте код:
## from random import
## randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import *

a = randint(0, 1001)
## print(a)
b = int(input("Угадай число от 0 до 1000: "))
count = 0

while count < 10:
    if b < 0 or b > 1000:
        b = int(input("Число не входит в диапозон 0-1000, попробуй еще: "))
        count += 1
    elif b < a:
        b = int(input("Больше!!! Угадывай: "))
        count += 1
    elif b > a:
        b = int(input("Меньше!!! Угадывай: "))
        count += 1
    elif b == a:
        print("Вы угадали число!!!")
        break
    else:
        print("Ошибка.")