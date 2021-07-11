def my_reverse(lst):
    # only use len
    if lst is None or len(lst) == 0:
        return []
    
    result = []
    index = len(lst) - 1
    
    while index >= 0:
        result.append(lst[index])
        index -= 1
    
    return result