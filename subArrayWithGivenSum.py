#Given an unsorted array of integers, find a subarray which adds to a given number.
# If there are more than one subarrays with the sum as the given number, print any of them.
A = [1,4,20,3,10,5]

def subArray(A,sums):
    currentSum = 0
    maps = {}
    for i in range(len(A)):
        currentSum = currentSum + A[i]

        if currentSum == sums:
            return "The subArray sum is found between 0 and index", i

        if (currentSum - sums) in maps:
            return "SubArray sum found between index",maps[currentSum -sums] + 1, "to ", i
        maps[currentSum] = i
        print(maps)

print(subArray(A,33))




