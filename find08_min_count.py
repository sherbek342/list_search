def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    i = 0 
    mn = data[0]
    while i < len(data):
        if mn >= data[i]:
            mn = data[i]
        i += 1
    res = data.count(mn)
    return res
print(find_min_count(data=[1,2,4,5,6,4,1]))
