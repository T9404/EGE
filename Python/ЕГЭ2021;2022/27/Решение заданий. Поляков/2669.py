f = open('27-9b.txt')
n = int(f.readline())


para = [int(f.readline()) for x in range(6)] # промежуток
mina = float('inf')

for _ in range(n-6):
    x  = int(f.readline()) 
    d = min([i for i in para if i % 2 == 1]) #берем минимальное нечетное число из 'para'
    
    para.append(x) #добавляем новое число
    
    if  x % 2 == 1: # если наше число нечетное( нечет*нечет = нечет)
            mina = min(d*x, mina)
            
    para = sorted([i for i in para if i % 2 == 1]) #сортируем нечетные числа из расстояния 6 и более
    para = [para[0]] #берем минимальное число
    
print(mina)
    
    

