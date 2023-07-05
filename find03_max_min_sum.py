def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    i = 0 
    mx = data[0]
    res = data[0]
    while i < len(data):
        if mx <= data[i]:
            mx = data[i]
        i += 1
    k = 0
    while k < len(data):
        if res > data[k]:
            res = data[k]
        k +=1
 

    
    return mx+res
print(find_max_min_sum(data=[1,2,4,6,5,6,4]))
