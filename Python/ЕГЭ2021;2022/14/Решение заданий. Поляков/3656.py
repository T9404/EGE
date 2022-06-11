'''
Число 456 записали в системах счисления с основаниями от 2 до 10 включительно. 
При каком основании количество нечётных цифр в записи этого числа будет максимальным? 
Если таких оснований несколько, то укажите максимальное из них.
'''
# https://prnt.sc/DN-zV0gzidjt


def func(number, foundation):
    count, number_s = 0, ''

    while number:
        number_s += str(number % foundation)
        number //= foundation

    number_s = number_s[::-1]

    for i in number_s:
        if int(i) % 2 != 0:
            count += 1

    return count


array = [func(456, j) for j in range(2, 10+1)][::-1]
print(10 - array.index(max(array)))
