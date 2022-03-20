# Почему такие диапазоны? Давайте посмотрем на открывки чисел. https://i.imgur.com/CjocAaG.png

# print(int('200', 8)) #16 c.c. входит в этот промежуток
# print(int('300', 8))

count = 0
for u in range(128, 192):
    if u % 16 == 14 and u % 8 == 6:  # 'E' - 14
        count += 1
print(count)
