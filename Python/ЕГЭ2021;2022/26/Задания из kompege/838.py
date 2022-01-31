f = open('26.txt')
n = int(f.readline())

values = sorted([int(x) for x in f.readlines()])

arr_max = []
arr_min = []

i = 0
j = len(values) - 1
k = 0

while k < len(values):

    if sum(arr_max) > sum(arr_min):
        arr_min.append(values[i])
        i += 1

    else:
        arr_max.append(values[j])
        j -= 1

    k += 1


print(len(arr_max), len(arr_min))      