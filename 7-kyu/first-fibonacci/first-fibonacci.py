def solution(first, second):
    
    while True:
        temp = first
        if second - first > first:
            break
        
        first = second - first
        second = temp
        
    
    return (first, second)