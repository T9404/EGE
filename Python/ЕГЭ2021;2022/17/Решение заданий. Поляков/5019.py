'''
В файле 17-278.txt содержится последовательность целых чисел. Элементы последовательности 
могут принимать целые значения от 0 до 1000. Определите сначала количество пар, в которых 
оба числа больше, чем сумма всех цифр «7» в восьмеричной записи всех чисел в файле, а затем 
минимальную из сумм таких пар. Под парой подразумевается два идущих подряд элемента последовательности.
'''
# https://prnt.sc/jtVJvzhC4Lh_


f = open('17-278.txt')
arr = [int(x) for x in f.readlines()]


sum_nums = sum([(oct(abs(i))[2:].count('7') * 7) for i in arr])

count, min_sum = 0, float('inf')


for i in range(len(arr)-1):
    if (arr[i] > sum_nums) and (arr[i+1] > sum_nums):
        count += 1
        min_sum = min(min_sum, arr[i] + arr[i+1])


print(count, min_sum)
