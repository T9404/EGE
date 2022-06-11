# Условие: https://prnt.sc/1dl8yk0


# (I) Способ

f = open('24.txt')
string = 'A' + f.readline() + 'A'


def func(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False

    return True


min_need = float('-inf')


for i in range(1, len(string)):
    if (string[i] in '1234567890') and (string[i-1] in 'ABC'):
        answer = ''

        while (string[i] in '1234567890'):
            answer += string[i]
            i += 1

        if ((string[i] in 'ABC') and (answer[0] != '0') and (func(int(answer)))):
            min_need = max(min_need, int(answer))

print(min_need)


# 2) Способ

f = open('24.txt')
s = f.readline()


s = s.replace('A', ' ', 1)
s = s.replace('B', ' ', 1)
s = s.replace('C', ' ', 1)


a = [int(x) for x in s.split()]


answer = max(x for x in a if (
    all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))))
    
print(answer)
