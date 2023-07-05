def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    i = 0 
    mx = data[0]
    while i < len(data):
        if mx < data[i]:
            if data[i]%2!=0:
                mx = data[i]
        i += 1
    return mx
print(find_max_odd(data=[1,2,4,5,6,4,7]))