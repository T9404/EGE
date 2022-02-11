'''
Необходимо выбрать из каждой пары одно число так, чтобы сумма
выбранных чисел была максимально возможной и не делилась на 5,
при этом сумма невыбранных чисел не делилась на 3. 
'''

f = open('27-66b.txt')
n = int(f.readline())

def get():
    return list(map(int, f.readline().split()))

smax = 0

s = [0]

for i in range(n): #типичный МЧС
    pair = [x for x in get()] 
    smax+=sum(pair) # считываем сумму всех чисел для того чтобы сразу найти вторую сумму

    cmb = [a+b for a in s for b in pair]
    s = {x % 5: x for x in sorted(cmb)}.values()                                  #(cmb, reverse=True) для мин, догадайтесь почему


m = max(x for x in s if (smax - x ) % 3 != 0 and x % 5 !=0)
print(m)



    
