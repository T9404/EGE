f = open('26-73.txt')
n = int(f.readline())


field = [[0 for _ in range(480+1)] for _ in range(640+1)]


for _ in range(n):
    a, b = map(int, f.readline().split())
    field[a][b] = 1


count, max_len = 0, 0

# Считаем длину с помощью лампочек (точек).
# "Группа начинается и заканчивается светлой точкой"
# max_len = lamp * 2 - 1

for row in range(640):

    lamp = 0
    switch = False

    for place in range(480):

        if field[row][place] == 1 and switch == False:
            lamp += 1
            switch = True

        elif field[row][place] == 0 and switch == True:
            switch = False

        else:
            if max_len < lamp * 2 - 1:
                max_len = lamp * 2 - 1
                count, number, = lamp, row

            lamp = 0
            switch = False


print(count, number)
