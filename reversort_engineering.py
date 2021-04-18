import itertools
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

def get_one_desired_list(original_list, desired_cost):
    perm_list_of_lists = []
    c=0
    all_possible_list = list(itertools.permutations(original_list))
    for j, val in enumerate(all_possible_list):
        one_list = list(val)
        temp = one_list.copy()
        cost = get_reversort_cost(one_list)
        if(cost==desired_cost):
            return temp
        c+=1
        if(c>10):
            break
    return None


def getList(size_of_list, desired_cost):
    temp_list = []
    for i in range(1,size_of_list+1):
        temp_list.append(i)
    # print(temp_list)
    return get_one_desired_list(temp_list,desired_cost)
 
def process_each_test_case():
    test_case = input()
    test_case = test_case.split(' ')
    test_case = list(map(int,test_case))
    return getList(test_case[0],test_case[1])

def theMain():
    test_cases = int(input())
    result = []
    for i in range(test_cases):
        result.append(process_each_test_case())
    for index, val in enumerate(result):
        if(val==None):
            print("Case #%d: "%(index+1),"IMPOSSIBLE")
        else:
            print("Case #%d: "%(index+1), " ".join(map(str,val)))

theMain()
# print(getList(20, 5))
