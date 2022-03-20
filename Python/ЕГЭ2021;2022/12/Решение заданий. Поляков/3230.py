number, min = 0, float('inf')

for i in range(81, 85+1):
    letter = '1' * i

    while '111' in letter:
        letter = letter.replace('111', '2', 1)
        letter = letter.replace('2222', '1', 1)


    if letter.count('1') < min:
        min = letter.count('1')
        number = i

print(min, number) 


# P.S. Задача с КОСЯЧНЫМ условием, в ней подразумевается, 
# что "содержащая минимально возможное количество единиц. " 0 единиц входит, 
# хотя по ссути при 0 НЕ СОДЕРЖИТ!!!
