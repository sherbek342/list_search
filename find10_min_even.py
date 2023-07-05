def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    i = 0 
    mn = data[0]
    while i < len(data):
        if mn > data[i]:
            if data[i]%2==0:
                mn = data[i]
        i += 1
    return mn
print(find_min_even(data=[1,2,4,-5,6,4,7]))
