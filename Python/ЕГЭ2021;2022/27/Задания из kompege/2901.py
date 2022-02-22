f = open('27B.txt')
n = int(f.readline())


count_seq = [0] * 666
answer, s = 0, 0


for _ in range(n):
    x = int(f.readline())
    s += x

    if s % 666 == 0:
        answer += 1

    answer += count_seq[s % 666]

    count_seq[s % 666] += 1


print(answer)
