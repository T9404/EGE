'''
Иван коллекционирует старые марки. Он собирает все марки, которые ему удаётся найти, 
которые были выпущены в его стране за определённые годы. Иван знает, что в эти годы 
каждый год выпускалось 8 различных типов марок. Иван решил проверить свою коллекцию и понять, 
скольких видов марок ему не хватает и для какого самого позднего года ему не хватает наибольшего 
количества марок до полного набора.
'''
# https://prnt.sc/qiNCV-QU7zIV


f = open('26.txt')
n = int(f.readline())


arr = [(int('19' + f'{i}'), set()) for i in range(61, 91 + 1)]


for _ in range(n):
    year, type_mark = map(int, f.readline().split())
    arr[year-1961][1].add(type_mark)


arr = [i for i in arr if (len(i[1]) != 0)]
count_lack = sum([8 - len(i[1]) for i in arr])


arr.sort(reverse=True)
min_mark = min(arr, key=lambda x: len(x[1]))


print(count_lack, min_mark[0])
