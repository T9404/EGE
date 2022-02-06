f = open('27-50b.txt')
n = int(f.readline())


zet = [0, 0]


min_razn, max_sum = float('inf'), 0

for _ in range(n):

    a, b = map(int, f.readline().split())
    max_sum += max(a, b)
    zet[(max(a, b)) % 2] += 1

    if (a % 2 != b % 2):
        min_razn = min(abs(a-b), min_razn)


if (max(zet) == zet[max_sum % 2]):
    print(max_sum-min_razn)

else:
    print(max_sum)
