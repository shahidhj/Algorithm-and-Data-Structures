# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#Input: [-2,1,-3,4,-1,2,1,-5,4],
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.


#Brute force
Array1 = [-2,1,-3,4,-1,2,1,-5,4]

Array2=[]
for i in range(0,len(Array1),1):
    for j in range(i,len(Array1)+1,1):
        for k in range(j,len(Array1)+1,1):
            Array2.append(sum(Array1[j:k]))
            #print(Array1[j:k])
print(max(Array2))
#O(n^3)


sums=0
#O(n^2) solution
for i in range(0,len(Array1)+1):

    for j in range(len(Array1)+1):
        currentSum = sum(Array1[i:j])
        #print(currentSum)
        if currentSum > sums:
            sums=currentSum
print(sums)

#Divide and conquer O(n)
Array2=[]
Array1 = [-2,1,-3,4,-1,2,1,-5,4]
for i in range(len(Array1)):
    sums= sums + Array1[i]
    if Array1[i] > sums:
        sums = Array1[i]
    Array2.append(sums)

print(max(Array2))