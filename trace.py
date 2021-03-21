def get_diagonal_sum_and_duplicate_rows(matrix):
    diag_sum = 0
    no_duplicate_rows = 0
    for x, arr in enumerate(matrix):
        if(len(arr)!=len(set(arr))):
            no_duplicate_rows+=1
        for y, val in enumerate(arr):
            if(x==y):
                diag_sum+=val  
    return(diag_sum,no_duplicate_rows)     

def get_no_repeated_columns(matrix):
    no_duplicate_columns = 0
    for x, arr in enumerate(matrix):
        initial_val = None
        check_list = []
        for y, arr2 in enumerate(matrix):
            if(y==0):
                check_list.append(arr2[x])
                continue
            if(arr2[x] in check_list):
                no_duplicate_columns+=1
                break
            else:
                check_list.append(arr2[x]) 
    return no_duplicate_columns

def cal_Vestigium(matrix):
    temp = []
    t = get_diagonal_sum_and_duplicate_rows(matrix)
    u = get_no_repeated_columns(matrix)
    temp.append(t[0])
    temp.append(t[1])
    temp.append(u)
    return temp


def takeUserInput():
    matrix_test = []
    squire_matrix_index = int(input())
    row = []
    for i in range(squire_matrix_index):
        row = input()
        row = row.split(' ')
        row = list(map(int,row))
        if(len(row)!=squire_matrix_index):
            print('invalid input')
            break
        matrix_test.append(row)
    return cal_Vestigium(matrix_test)

def theMain():
    test_cases = int(input())
    result = []
    for i in range(test_cases):
        result.append(takeUserInput())
    for index, val in enumerate(result):
        print("Case #%d : "%(index+1),val[0]," ",val[1]," ",val[2])
 
theMain()





# Sample input
# 3
# 4
# 1 2 3 4
# 2 1 4 3
# 3 4 1 2
# 4 3 2 1
# 4
# 2 2 2 2
# 2 3 2 3
# 2 2 2 3
# 2 2 2 2
# 3
# 2 1 3
# 1 3 2
# 1 2 3