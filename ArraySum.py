#Given an array, find the integers that would add upto the sum which is passed as an argument tot he function
# For example:Given an input ([6,4,3,2,1,7], 9),find the numbers in the array that would add to 9

def hasPairWithSum(array,sums):
    compliment =0
    B={}
    for eachNumber in array:
        compliment = sums - eachNumber
        if eachNumber in B.keys():
            print(compliment,eachNumber)
            break
        else:
            B[compliment] =1


hasPairWithSum([6,4,5,1,3,6], 9)
