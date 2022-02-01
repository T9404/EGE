f = open('2651.txt')
n = int(f.readline())

arr = [ (int('19'+f'{i}'), set()) for i in range(61, 91+1) ]


for _ in range(n):
    year, type_mark = map(int, f.readline().split())
    arr[year-1961][1].add(type_mark)


arr = [ i for i in arr if ( len(i[1]) != 0 )]
count_lack = sum([8-len(i[1]) for i in arr ])


arr.sort(reverse=True)
min_mark = min(arr, key=lambda x: len(x[1]))


print(count_lack, min_mark[0])