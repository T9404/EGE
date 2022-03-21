from itertools import *



def ok(x):  # реализация через функцию, удобно, используйте
    if x.count('С') == 1:
        return True
    else:
        return False


s_waw = 'СЛОН'
m = {x for x in product(s_waw, repeat=5) if ok(x)}  # генератор

print(len(m))
