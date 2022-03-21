stroka = '7' * 120

while '8887' in stroka or '77' in stroka:
    if '8887' in stroka:
        stroka = stroka.replace('8887', '8', 1) 
    else:
        stroka = stroka.replace('77', '8', 1)
        
print(stroka)
