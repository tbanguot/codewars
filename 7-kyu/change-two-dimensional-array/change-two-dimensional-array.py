def matrix(array): 
    # your code here
    for i in range(len(array)):
        if array[i][i] < 0:
            array[i][i] = 0
        else:
            array[i][i] = 1
            
    return array