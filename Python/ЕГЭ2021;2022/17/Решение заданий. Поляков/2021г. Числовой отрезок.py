#С открытого курса Алексея Кабанов!
# Условие: https://prnt.sc/1dkx7q2

def check_1_condition(x):
    count = 0
    while x:
        if x % 15 == 10:
            count +=1
        x//=15 #не забываем 
    return count == 1

    
def check_2_condition(x):
    count = 0 #переменные в функции локальные, можно так делать
    while x:
        if x % 15 == 14:
            count +=1
        x//=15 #не забываем 
    return count == 0

a = []
for x in range(14770, 89921+1):
    if ( check_1_condition(x) and x % 6 ==0) != \
       ( check_2_condition(x) and x % 13 ==2):
        a.append(x)
print(min(a), len(a))


# Что важно понимать:
''' Не будьте глупцами как я и считайте по пальцам номер буквы Е :)'''
