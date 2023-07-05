def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    list = []
    k = 0
    while k < len(data):
        if data[k]%2 != 0:
            list.append(data[k])
        k +=1

    i = 0 
    mx = list[0]
    while i < len(list):
        if mx < list[i]:
            if list[i]%2!=0:
                mx = list[i]
        i += 1
    return mx
print(find_max_odd(data=[1,2,4,5,6,4,7]))