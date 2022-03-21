x = 9 ** 81 + 27 ** 729 - 4

x_9 = []

while x:
    x_9.append(x % 9)
    x //= 9


answer, mak = max(x_9), 0

for i in x_9:
    if (i == mak) or (i == 0):
        answer += 1

print(answer)