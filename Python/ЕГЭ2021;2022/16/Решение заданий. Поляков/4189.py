def vol(n):
    if n == 0:
        return 2
    elif 0 < n <= 15:
        return vol(n-1)
    elif 15 < n < 95:
        return 1.6 * vol(n-3)
    elif n >= 95:
        return 3.3*vol(n-2)


print(int(vol(33)))  # ответ 3
