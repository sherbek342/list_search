def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    list = []
    k = 0
    while k < len(data):
        if data[k]%2 == 0:
            list.append(data[k])
        k +=1

    i = 1
    mx = list[0]
    while i < len(list):
        if list[i]%2==0:
            if mx < list[i]:
            
                mx = list[i]
        i += 1
    return mx
print(find_max_even(data=[111,2,4,5,6,4,7]))
