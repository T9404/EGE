print('>>>>>>>')
#3132 К.Ю.Поляков
'''
Определите, сколько символов * выведет эта процедура при вызове F(140):

https://prnt.sc/1ar02t6

'''

def F(N):
    global amount
    amount+=1
    if N >= 1:
        amount+=1
        F(N-1)
        F(N//2)
amount = 0
print(F(140)) #None, все логично
print(amount)