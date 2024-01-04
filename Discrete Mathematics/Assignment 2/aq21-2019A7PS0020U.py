

def factorial(num):
    factorial = 1

    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
            return factorial
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
    return factorial

def combination(n,r):
    p=n
    q=n-r
    a1=factorial(p)
    a2=factorial(r)
    a3=factorial(q)
    
    final=(a1/(a2*a3))
    
    print("The number of r-combinations of n distinct objects is",final)
    
n=int(input("Enter value of n: "))
r=int(input("Enter value of r: "))
combination(n, r)