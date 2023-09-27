# factorial -- recursive function
# 1st method
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)
m=int(input(" enter factorial value"))
print(m,factorial(m))

# 2nd method
#iterative approach
def factorial(n):
    if n<0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -=1
        return fact
num=6
print((num),
factorial(num))
# same method another model
def factorial(n):
    r=1
    for i in range(2,n+1):
        r*=i
    return r
num=8
print(num,factorial(num))

#ternery opretor
# 3rd method
def factorial(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1)
n=9
print(n,factorial(n))

#importing module --- built in function
#method -4
import math
def factorial(n):
    return(math.factorial(n))
n=3
print(n,factorial(n))


#
#method-5


