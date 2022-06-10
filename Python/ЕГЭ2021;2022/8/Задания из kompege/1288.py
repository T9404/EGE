''' 
Вася составляет 6-буквенные слова, в которых могут быть использованы 
только буквы В, И, Ш, Н, Я, причём буква В используется не более одного 
раза. Каждая из других допустимых букв может встречаться в слове любое 
количество раз или не встречаться совсем. Слово не должно начинаться с буквы Ш 
и оканчиваться гласными буквами. Словом считается любая допустимая 
последовательность букв, не обязательно осмысленная. Сколько существует 
таких слов, которые может написать Вася?
'''
# https://prnt.sc/KHpCif0Wsfqi


from itertools import product


amount = 0


for i in product('ВИШНЯ', repeat=6):
    word = ''.join(i)
    if (word.count('В') <= 1 and word[0] != 'Ш' and
            word[-1] not in 'ИЯ' and word[4:] != 'ИЯ'):
        amount += 1


print(amount)
