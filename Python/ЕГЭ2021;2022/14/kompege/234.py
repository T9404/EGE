'''
Значение арифметического выражения: 2∙277 + 310 – 9 записали в системе счисления 
с основанием 3. Сколько цифр «0» содержится в этой записи?
'''
# https://prnt.sc/-PBlQ-DeTDUC


number = 2 * 27 ** 7 + 3 ** 10 - 9
count = 0


while number:
    if number % 3 == 0:
        count += 1
    number //= 3


print(count)
