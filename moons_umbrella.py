def get_substr_count(Str, target):
     
    no_of_match = 0
    len_str = len(Str)
     
    count = 0
    for i in range(len_str):
        if (Str[i] == target[no_of_match]):
            no_of_match += 1
        if (no_of_match == len(target)):
            count+=1
            no_of_match = 0
    return count

def get_best_of_cj(the_string, prev_char, after_char, cj_cost, jc_cost):
    c_cost = 0
    j_cost = 0
    if(prev_char+'C'=='JC'):
        c_cost += jc_cost
    if('C'+after_char=='CJ'):
        c_cost += cj_cost
    if(prev_char+'J'=='CJ'):
        j_cost += cj_cost
    if('J'+after_char=='JC'):
        j_cost += jc_cost
    # print(c_cost,j_cost)
    if(c_cost==0 and j_cost==0):
        c_count = get_substr_count(the_string, 'C')
        j_count = get_substr_count(the_string, 'J')
        return 'C' if c_count>j_count else 'J'
    if(c_cost>j_cost):
        return 'J'
    else:
        return 'C'
def get_best_of_cj_after(the_string, after_char, cj_cost, jc_cost):
    c_cost = 0
    j_cost = 0
    if('C'+after_char=='CJ'):
        c_cost += cj_cost
    if('J'+after_char=='JC'):
        j_cost += jc_cost
    # print(c_cost,j_cost)
    if(c_cost==0 and j_cost==0):
        c_count = get_substr_count(the_string, 'C')
        j_count = get_substr_count(the_string, 'J')
        return 'C' if c_count>j_count else 'J'
    if(c_cost>j_cost):
        return 'J'
    else:
        return 'C'

def get_best_of_cj_prev(the_string, prev_char, cj_cost, jc_cost):
    c_cost = 0
    j_cost = 0
    if(prev_char+'C'=='JC'):
        c_cost += jc_cost
    if(prev_char+'J'=='CJ'):
        j_cost += cj_cost
    # print(c_cost,j_cost)
    if(c_cost==0 and j_cost==0):
        c_count = get_substr_count(the_string, 'C')
        j_count = get_substr_count(the_string, 'J')
        return 'C' if c_count>j_count else 'J'
    if(c_cost>j_cost):
        return 'J'
    else:
        return 'C'

def get_final_string(S, cj_cost, jc_cost):
    if(len(S)<2):
        return S
    for i, val in enumerate(S):
        if(val!='?'):
            continue
        temp_cost = 0
        if(i==0):
            best_of_cj = get_best_of_cj_after(S, S[i+1], cj_cost, jc_cost)
            S = list(S)
            S[i] = best_of_cj
            S = "".join(S)
            # print(S)
        elif(i!=0 and i!=len(S)-1):
            best_of_cj = get_best_of_cj(S, S[i-1], S[i+1], cj_cost, jc_cost)
            S = list(S)
            S[i] = best_of_cj
            S = "".join(S)
            # print(S)
        elif(i==len(S)-1):
            best_of_cj = get_best_of_cj_prev(S, S[i-1], cj_cost, jc_cost)
            S = list(S)
            S[i] = best_of_cj
            S = "".join(S)
            # print(S)
    return S



def process_each_test_case():

    test_case = input()
    test_case = test_case.split(' ')
    cj_jc_cost_list = list(map(int,test_case[0:2]))
    cj_cost = cj_jc_cost_list[0]
    jc_cost = cj_jc_cost_list[1]
    mural_string = test_case[2]
 
    final_string = get_final_string(mural_string, cj_cost, jc_cost)
    no_of_cj = get_substr_count(final_string, "CJ")
    no_of_jc = get_substr_count(final_string, "JC")
    total_cost = no_of_cj*cj_cost+no_of_jc*jc_cost
    return total_cost


def theMain():

    test_cases = int(input())
    result = []
    for i in range(test_cases):
        result.append(process_each_test_case())
    for index, val in enumerate(result):
        print("Case #%d: "%(index+1),val)
 
theMain()

# get_final_string('??J???', 2, 5)