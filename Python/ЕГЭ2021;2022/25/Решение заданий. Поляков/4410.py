'''
 Среди чисел, больших 520000, найти такие, для которых сумма всех нетривиальных 
 делителей (не считая единицы и самого числа) образует число-палиндром 
 (например, число 1221: если его «перевернуть», получается то же самое число). 
 Вывести первые пять чисел, удовлетворяющих вышеописанному условию, справа от 
 каждого числа вывести его максимальный нетривиальный делитель.
'''
# https://prnt.sc/kSbbWcj4WUzU


def condition(number):
    dividers = set()

    for i in range(2, int(number ** 0.5) + 1):
        if (number % i == 0):
            dividers.add(i)
            dividers.add(number // i)

    summ = sum(list(dividers))

    if (summ != 0) and (str(summ) == str(summ)[::-1]):
        return max(list(dividers))
    return 0


count = 0

for i in range(520001, 10000000):
    if condition(i) != 0:
        count += 1

        if (count <= 5):
            print(i, condition(i))
        else:
            break
