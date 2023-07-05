def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    i = 0 
    mn = data[0]
    while i < len(data):
        if mn > data[i]:
            mn = data[i]
        i += 1
    idx = data.index(mn)
    return idx
print(find_min_index(data=[1,2,4,5,6,-2,4]))
