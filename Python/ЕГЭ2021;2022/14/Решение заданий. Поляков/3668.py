'''
Число 1988 записали в системах счисления с основаниями от 2 до 10 включительно. 
При каких основаниях в записи этого числа нет двух одинаковых цифр, стоящих рядом? 
В ответе укажите сумму всех подходящих оснований.
'''
# https://prnt.sc/CefJntKJKU5E


def f(number, foundation):
    number_found = ''

    while number:
        number_found += str(number % foundation)
        number //= foundation

    d = [str(i) * 2 for i in range(foundation)]
    for i in d:
        if i in number_found:
            return False

    return True


count = 0

for i in range(2, 10+1):
    if f(1988, i):
        count += i

print(count)
