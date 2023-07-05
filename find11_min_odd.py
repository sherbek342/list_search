def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    
    list = []
    k = 0
    while k < len(data):
        if data[k]%2 != 0:
            list.append(data[k])
        k +=1

    i = 0 
    mn = list[0]
    while i < len(list):
        if mn > list[i]:
            if list[i]%2!=0:
                mn = list[i]
        i += 1
    return mn
print(find_min_odd(data=[22,3,4,5,6,4,7]))
