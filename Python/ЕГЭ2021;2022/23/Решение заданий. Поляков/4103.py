def f(start, end):
    if start == end:
        return 1
    elif start > end:
        return 0
    else:
        return f(start+1, end)+f(start*2, end)+  f(start+(start % 2)+(start % 2)+( (start +1) % 2), end)
    
print(f(3, 9)*f(9, 17)*f(17, 25))
