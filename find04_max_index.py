def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    i = 0 
    mx = data[0]
    while i < len(data):
        if mx < data[i]:
            mx = data[i]
        i += 1
    idx = data.index(mx)
    return idx
print(find_max_index(data=[1,2,4,5,6,4]))
