# Метод частичных сумм
# К.Ю.Поляков 2670
f = open('27-10a.txt')
n = int(f.readline())


def get():  # функция для считывание тройки
    return list(map(int, f.readline().split()))


new_list = get()  # считывание первой тройки(от нее будем двигаться)

for _ in range(n-1):  # n-1 ОБЯЗАТЕЛЬНО!
    dinamic_list = get()  # динамично считываем тройку

    cmb = [a+b for a in new_list for b in dinamic_list] # генерация

    comparison = [float('-inf')]*4  # делимость на 4 спрашивают

    for number in cmb:
        if number > comparison[number % 4]:
            comparison[number % 4] = number

    ''' Почему работает так? Мы берем ПРЕДЫДУЩИЕ значения и новые, складываем
        Берем ост от деления на 4, т.к. делимость на 4 спрашивают
        Можно подумать и использовать алг для решения проблемы делимости в другой сс.
        например в 5 системе => % 5  '''


    new_list = [number_new for number_new in comparison if number_new != float(
        '-inf')]  # если значения не пустые



# можно реализовать иначе
mina = 0

for i in new_list:
    if i % 4 != 0:
        if i > mina:
            mina = i

print(mina)
