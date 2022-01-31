f = open('test.txt')
s, n = map(int, f.readline().split())

values = sorted([int(x) for x in f.readlines()])
disk = []

i = 0
j = len(values) - 1

while ( i < len(values)//2+1):

    if sum(disk)+values[j] <= s:
        disk.append(values[j])
        if sum(disk)+values[i] <= s:  
            disk.append(values[i])

    i += 1
    j -= 1
    

print(len(disk), disk[-1])
