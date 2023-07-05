def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    i = 0 
    mx = data[0]
    res = 0
    while i < len(data):
        if mx <= data[i]:
            mx = data[i]
        i += 1
    res = data.count(mx)
    return res
print(find_max_count(data=[1,2,4,6,5,6,4]))
