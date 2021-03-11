
theString =  "aabccbbcaa"

# def getUniqueChar(st):
#     uniq_char_list = []
#     for c in range(len(st)):
#         if st[c] not in uniq_char_list:
#             uniq_char_list.append(st[c]) 
#     return uniq_char_list

def getCount(substring, char):
    count = 0
    for c in range(len(substring)):
        if substring[c] == char:
            count +=1
    return count

def checkIfEvenChar(substring):
    for c in range(len(substring)):
        count = getCount(substring, substring[c])
        if(count!=0):
            if(int(count%2)!=0):
                return False
    return True
 
 

# getUniqueChar(theString)
def printSubstrings(theString):
    string_length = len(theString)
    #this loop is to iterate through the array
    no_even_substring = 0
    for i in range(string_length):
        end = i+1
        #this loop will print one set of sub arrays for the given end index of array
        # print("sequence........",i)
        for j in range(0,end):
            substring = theString[j:end]
            if(checkIfEvenChar(substring)):
                no_even_substring+=1
                # print(substring) 
    print("No. of possible even substrings are : ",no_even_substring)

given_string = input ("Enter string :") 
printSubstrings(given_string)































# def indexes(seq, start=0):
#     return (i for i,_ in enumerate(seq, start=start))

# def gen_all_substrings(s):
#     return (s[i:j] for i in indexes(s) for j in indexes(s[i:], i+1))

# def get_all_substrings(string):
#     return list(gen_all_substrings(string))

# print(get_all_substrings('abcde'))