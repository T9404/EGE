'''
Сколько существует натуральных чисел, шестнадцатеричная запись 
которых содержит 6 знаков, не начинается с единицы и заканчивается на AB?
'''
# https://prnt.sc/zdRDkNDnLOYG


count = 0


# помните про границы и регистр
for i in range(int('100000', 16), int('1000000', 16)): 
    number = hex(i)[2:]
    if (number[0] not in '01') and (number[-2:] == 'ab'): 
        count += 1

    
print(count)
