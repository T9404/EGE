d = []
def f(start, count):
    if count == 7 and start == 25:
        d.append(start)
        
    if count < 7:
        f(start+1,  count+1)
        f(start+3, count+1)
        f(start*2, count+1)

f(2, 0)
print(len(d))

