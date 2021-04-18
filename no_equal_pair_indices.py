# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def getCount(A,val):
    c = 0
    for i, v in enumerate(A):
        if(val==v):
            c+=1
    return c



def solution(A):
    # write your code in Python 3.6
    c = 0
    original_list = A.copy()
    unique_list = list(set(A))
    print(original_list)
    print(unique_list)
    for item in unique_list:
        count = getCount(original_list, item)-1
        print(count)
        c+=count
    return c

test = [3,5,6,3,3,5]
# test = [3,3,3]
print(solution(test))
