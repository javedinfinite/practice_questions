# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def getIndexPositive(int_list):
    for idx, val in enumerate(int_list):
        if(val<5):
            int_list.insert(idx,5)
            return ''.join(str(e) for e in int_list)
    int_list.insert(idx+1,5)
    return ''.join(str(e) for e in int_list)

def getIndexNegative(int_list):
    for idx, val in enumerate(int_list):
        if(val>5):
            int_list.insert(idx,5)
            return ''.join(str(e) for e in int_list)
    int_list.insert(idx+1,5)
    return ''.join(str(e) for e in int_list)

def solution(N):
    # write your code in Python 3.6
 
    int_list = list(map(int, str(abs(N))))
    if(N>0 or N==0):
        latest_list = int(getIndexPositive(int_list))
    else:
        latest_list = int(getIndexNegative(int_list)) * -1
    return latest_list
