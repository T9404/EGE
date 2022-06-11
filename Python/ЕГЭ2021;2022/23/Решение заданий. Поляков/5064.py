'''
Исполнитель Ландыш преобразует пару чисел, записанную на экране. У исполнителя Ландыш 
есть четыре команды:
1. Прибавь к первому числу 3
2. Умножь первое число на 4
3. Прибавь ко второму числу 5
4. Умножь второе число на 2
Первая из них увеличивает первое число из пары на 2, вторая – умножает его на 4. 
Третья команда увеличивает второе число из пары на 5, четвертая – умножает его на 2. 
Сколько различных пар взаимно простых чисел можно получить из пары чисел (2, 3) с помощью программы, 
которая состоит ровно из 5 команд? Пары, отличающиеся только перестановкой чисел, считать одинаковыми.
'''
# https://prnt.sc/nMlOsAPhtfNq


from math import gcd


unique = set()


def command(start, end, count):
    if count > 5:
        return 0
    elif (count == 5) and (gcd(start, end) == 1) and ((start, end) not in unique) and ((end, start) not in unique):
        unique.add((start, end))
    else:
        command(start + 3, end, count + 1)
        command(start * 4, end, count + 1)
        command(start, end + 5, count + 1)
        command(start, end * 2, count + 1)


command(2, 3, 0)

print(len(unique))
