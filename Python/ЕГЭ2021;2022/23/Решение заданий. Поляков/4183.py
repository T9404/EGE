def f(start, end):
    if end > start:
        return 0
    elif start == end:
        return 1
    else:
        return f(start-8, end)+f(start//2, end)
    
print(f(102, 43)*f(43, 5))
