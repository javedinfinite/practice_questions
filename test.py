import itertools

temp_list = []
for i in range(1, 4):
    temp_list.append(i)

test = list(itertools.permutations(temp_list))

print(list(test[0]))