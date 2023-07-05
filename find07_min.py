def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    i = 0 
    mn = data[0]
    while i < len(data):
        if mn > data[i]:
            mn = data[i]
        i += 1
    return mn
print(find_min(data=[1,2,4,5,6,4,-8]))