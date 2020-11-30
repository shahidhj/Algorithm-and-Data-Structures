A = [2,5,1,2,3,5,1,2,4]
B = [2,1,1,2,3,5,1,2,4]
# Easy approach is to sort it and then loop through and raise a flag when the first recuring character is found
# Effecient way would be to loop over each element and add it to a dictonary and then check if the next element is already in dictionary, raise a flag

maps= {}
#
# for i in range(0,len(B)):
#     if B[i] in maps:
#         print(B[i])
#         break
#     else:
#         maps[B[i]]=1
#
# print(maps)

def recurringChar(A):
    for eachNum in A:
        if eachNum in maps.keys():
            return eachNum
        maps[eachNum] = 1

Ans = recurringChar(B)
print(Ans)
