from itertools import permutations


#1 Решение

a = []
word = 'ТИКТОК'

for i in permutations(word, r=6):
    w = ''.join(i)
    if ('ТТ' not in w) and ('КК' not in w):
        a.append(w)
                   
a1 = list(set(a))
print(len(a1))






#2 Решение

a = []
word = 'ТИКТОК'

count = 0
for i in permutations(word, r=6):
    w = ''.join(i)
    if ('ТТ' not in w) and ('КК' not in w):
        count+=1
            
print(count//4)



