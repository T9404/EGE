f = open('26-73.txt')
n = int(f.readline())


field = [set() for _ in range(641)]


for i in range(n):
    row, place = map(int, f.readline().split())
    field[row].add(place)


def check_len(d):
    # поиск максимальной длины непрерывной цепочки

    if not d:
        return 0

    max_len, l = 1, 1

    for i in range(1, len(d)):
        if d[i-1] + 1 == d[i]:
            l += 1
            max_len = max(l, max_len)
        else:
            l = 1

    return max_len


answer = 0

for j, d in enumerate(field):

    d = sorted(d)
    max_len = check_len(d)

    if max_len >= answer:
        answer = max_len
        number = j


print(answer, number)
