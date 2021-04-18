# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    min_num = min(A)
    max_num = max(A)
    if(len(A)==1):
        if(A[0]==1):
            return 2
        else:
            return 1
    if(min_num>1):
        return 1
    if(min_num<0 and max_num<0):
        return 1

    result = 'g'
    if(min_num<0 and max_num>0):
        min_num=1

    for num in range(min_num, max_num+1):
        if(num not in A ):
            result = num
            break
    if(result=='g'):
        result= max_num+1
        
    return result