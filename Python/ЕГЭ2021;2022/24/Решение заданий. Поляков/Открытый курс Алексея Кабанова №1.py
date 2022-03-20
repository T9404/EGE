# Условие: https://prnt.sc/1dl8yk0

# 1) Способ
f = open('24-zagl.txt')


def func(x):
    sqr = int(x**0.5)
    for i in range(2, sqr+1):
        if x % i == 0:
            return False

    return True


string = 'A' + f.readline() + 'A'
mina = float('-inf')

for i in range(1, len(string)):
    if string[i] in '1234567890' and string[i-1] in 'ABC':  # 0
        answer = ''

        while string[i] in '1234567890':
            answer += string[i]
            i += 1

        if string[i] in 'ABC' and answer[0] != '0':
            if func(int(answer)):
                mina = max(mina, int(answer))

print(mina)








# 2) Способ

f = open('24.txt')
s = f.readline()


def prime(x):
    sq = int(x**0.5)
    for i in range(2, sq+1):
        if x % i == 0:
            return False

    return True


s = s.replace('A', ' ', 1)
s = s.replace('B', ' ', 1)
s = s.replace('C', ' ', 1)

a = [int(x) for x in s.split()]

print(max(x for x in a if prime(x)))
