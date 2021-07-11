def big_fibonacci(n):
    if n < 0:
        return 0
    
    current = 1
    a = 1
    b = 1
    
    while len(str(current)) < n:
        current = sum(a, b)
        a = b
        b = current
    
    return current
