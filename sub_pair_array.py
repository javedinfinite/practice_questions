def pairs_gen(L):
    if len(L) == 2:
        yield [(L[0], L[1])]
    else:
        first = L.pop(0)
        for i, e in enumerate(L):
            second = L.pop(i)
            for list_of_pairs in pairs_gen(L):
                list_of_pairs.insert(0, (first, second))
                yield list_of_pairs
            L.insert(i, second)
        L.insert(0, first)

def cal_gcd(no_one, no_two):
    if(no_two==0):
        return no_one
    else:
        return cal_gcd(no_two, no_one % no_two)
 
def solve (N, A):
    all_pairs = list(pairs_gen(temp_list))
    result_list = []
    for sub_set in all_pairs:
        print(sub_set)
        temp_gcd_list = []
        round_cal = 0
        for pair in sub_set:
            temp_gcd_list.append(cal_gcd(pair[0],pair[1]))
        print(temp_gcd_list)
        temp_gcd_list.sort()
        print(temp_gcd_list)
        for index, val in enumerate(temp_gcd_list):
            round_cal+=val*(index+1)
        print(round_cal)
        result_list.append(round_cal)
     
    
    return max(result_list)
 
# N = int(input())
# A = list(map(int, input().split()))
# temp_list = [0, 1, 2, 3, 4, 5]
# temp_list = [1, 2, 3, 4]
# temp_list = [3, 4, 9, 5]
# temp_list = [3, 4, 9, 5]
# temp_list = [8,5,6,25,6,16]
temp_list = [34,102,45,102,45,102,34,12]
N = 4
 
 
out_ = solve(N, temp_list)
print (out_)
