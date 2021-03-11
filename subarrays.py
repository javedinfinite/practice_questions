#iterative approach

 

# main_array = [1,2,3,4]
# array_length = len(main_array)
# def printSubarrays(main_array):
#     #this loop is to iterate through the array
#     for i in range(array_length):
#         end = i+1
#         #this loop will print one set of sub arrays for the given end index of array
#         for j in range(0,end):
#             print(main_array[j:end]) 

# printSubarrays(main_array)


main_array = [1,2,3,4]
array_length = len(main_array)
def printSubarrays(main_array):
    #this loop is to iterate through the array
    for i in range(array_length):
        # end = i+1
        #this loop will print one set of sub arrays for the given end index of array
        # for j in range(0,i):
            print("index:....",i)
            print(main_array[0:i+1]) 
            if(i+1!=array_length):
                print(main_array[i+1:array_length])

printSubarrays(main_array)



#recursive approach