# L = [4,2,1,3]
# L = [1,2]
# L = [7, 6, 5, 4, 3, 2, 1]
 

def reverse_sublist(L, i, j):
    while i<j:
        L[i], L[j]=L[j], L[i]
        i+=1
        j-=1
def get_reversort_cost(L):
    cost = 0
    for i, val in enumerate(L):
        if(i<len(L)-1):
            j = L.index(min(L[i:len(L)]))
            reverse_sublist(L, i, j)
            cost+= j-i+1
    return cost

def process_each_test_case():
    List_test = []
    list_length = int(input())
    List_test = input()
    List_test = List_test.split(' ')
    List_test = list(map(int,List_test))
    if(len(List_test)!=list_length):
        print('invalid input')
        return
    return get_reversort_cost(List_test)

def theMain():
    test_cases = int(input())
    result = []
    for i in range(test_cases):
        result.append(process_each_test_case())
    for index, val in enumerate(result):
        print("Case #%d: "%(index+1),val)
 
theMain()
