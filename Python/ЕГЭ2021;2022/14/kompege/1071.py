'''
При каком наименьшем введённом значении x запись выражения

125200 - 5x + 74

содержит ровно 100 цифр "4" в пятеричной записи числа?
'''
# https://prnt.sc/2D_SMBBEFvDv


def f(number, count=0):
    while number:
        if number % 5 == 4:
            count += 1
        number //= 5

    return count


for i in range(1, 1000):
    y = 125 ** 200 - 5 ** i + 74
    if f(y) == 100:
        print(i)
        break
