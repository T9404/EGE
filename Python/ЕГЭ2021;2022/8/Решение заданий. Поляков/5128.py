k = 0

for i in range(int('100000', 16), int('1000000', 16)): # граница 6-ти значных 
    m = hex(i)[2:]
    if m[0] not in '01' and m[-2:] == 'ab': # регистр
        k += 1
        
print(k)
        
