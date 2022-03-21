def F(N):
    global amount
    amount += 1

    if N >= 1:
        amount += 1
        F(N-1)
        F(N//2)


amount = 0
F(140)

print(amount)
