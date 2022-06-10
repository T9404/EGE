'''
Вася составляет 5-буквенные коды из букв И, Г, Р, О, К. Каждую букву 
нужно использовать ровно 1 раз, при этом код не может начинаться с буквы К 
и не может содержать сочетания РОК. Сколько различных кодов может составить Вася?
'''
# https://prnt.sc/vo22jtRGRnJZ


from itertools import permutations


count = 0


for i in permutations('ИГРОК', r=5):
    word = ''.join(i)
    if (word[0] != 'К') and ('РОК' not in word):
        count += 1


print(count)
