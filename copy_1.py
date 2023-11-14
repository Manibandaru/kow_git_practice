import copy

a= 2+3
# shallow copy
list_1 = [1, 2, [3, 5], 4]
list_2 = copy.copy(list_1)
print(list_2)
list_2[3]=8
list_2[2].append(6)
print(list_2)
print(list_1)
# deep copy
list_3 = copy.deepcopy(list_1)
print(list_3)
list_3[3] = 8
list_3[2].append(7)
print(list_3)
print(list_1)