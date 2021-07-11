def my_range(m, n):
    if n < m:
        return []
    
    result = []
    index = 0

    while index < n:
        result.append(m + index)
        index += 1

    return result

print(my_range(0, 5))