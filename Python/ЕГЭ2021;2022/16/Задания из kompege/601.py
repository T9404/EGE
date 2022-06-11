'''
Определите, сколько символов * выведет эта процедура при вызове F(40):
'''
# https://prnt.sc/5RQx6gSB2D47


count = 0


def f(n):
    global count
    count += 1
    
    if n >= 1:
        count += 1
        f(n - 1)
        f(n - 3)
        count += 1


f(40)
print(count)
