'''
Все 5-буквенные слова, составленные из букв А, З, Н, С, записаны в алфавитном 
порядке и пронумерованы. Вот начало списка:
1. ААААА
2. ААААЗ
3. ААААН
4. ААААС
5. АААЗА
...
Какое количество слов находятся между словами САЗАН и ЗАНАС (включая эти слова)?
'''
# https://prnt.sc/A7phLT6vsy_n


from itertools import product


arr = []

for i, letter in enumerate(product('АЗНС', repeat=5), start=1):
    word = ''.join(letter)
    if (word == 'САЗАН') or (word == 'ЗАНАС'):
        arr.append(i)


# количество = длина + 1
print(arr[1] - arr[0] + 1)
