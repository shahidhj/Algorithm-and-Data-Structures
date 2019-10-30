#Time complexity using recursive approach is expoennetial (2^n) and using iterative approach is O(n)


def fibonacciIterative(number):
    a=0
    b=1
    sum = 0
    if number == 0 :
        return a
    elif number == 1:
        return  b
    else:
        print(a)
        print(b)
        for i in range(2,number+1):
            sum = a + b
            a = b
            b = sum
            print(sum)

def fibonacciRecursive(number):
    if number <=1:
        return number
    else:
        #print(fibonacciRecursive(number-1) + fibonacciRecursive(number-2))
        return fibonacciRecursive(number-1) + fibonacciRecursive(number-2)

fibonacciIterative(3)

abc = fibonacciRecursive(6)
print(abc)