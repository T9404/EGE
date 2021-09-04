#зАдАчА с открытого курса №2
#https://vk.com/doc18466579_608953613?hash=1b76b3eb7ac6b42203&dl=4762d7fe0023ac5615

f = open('17.txt')
d = []
while True: 
    x = f.readline()
    if not x: # нету x, тогда пока
        break
    else:
        d.append(x) #ок, берем его
        
k, mik = 0, float('inf')

for i in range(1, len(d)): # с 0 и 1го элементов начало
    
    a = int(d[i-1]); b = int(d[i]) # a и b будут с теми же знаками!
    
    if (a*b) > 0 and (abs(a+b)%7 == 0): #условие задачи
        
        mik = min(a*b, mik) # пиу-пяу
        k+=1
        
print(k, mik)

