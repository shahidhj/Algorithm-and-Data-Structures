#Finding fatorial of a number using recursion and iterative approach

def factorialIterative(number):
    fact =1
    if number == 0:
        return 1
    else:
        for i in range(number,1,-1):
            fact = fact * i
        return fact

def facctorialRecursive(number):
    if number <= 1:
        return 1
    else:
        return number * facctorialRecursive(number-1)

a =factorialIterative(5)
b = facctorialRecursive(5)
print(b)

