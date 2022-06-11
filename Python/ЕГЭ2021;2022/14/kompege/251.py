'''
Запись числа 6810 в системе счисления с основанием N оканчивается на 2 и 
содержит 4 цифры. Чему равно основание этой системы счисления N?
'''
# https://prnt.sc/bHGeEH7UsU74


for number in range(1, 100):
    try:
        # (% 10) отправляем в нужную С.С.
        if 68 % int('10', number) == 2:
            if int('1000', number) <= 68 <= int('10000', number):
                print(number)
                break
    except:
        continue
