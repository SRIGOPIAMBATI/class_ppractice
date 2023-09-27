#addition of 2 numbers
#1st method dynamic model
num1=10
num2=23
ad=num1+num2
print(ad)
# 2nd method user input method
n1=eval(input(" enter 1st number "))
n2=eval(input(" enter 2st number "))
a= int(n1)+int(n2)
print("{n1}+{n2}sum is {a}",a)
#3rd method  ---  by using function.
def add(x,y):
    return x+y
a=12
s=33
sum=add(a,s)
print(sum)

# imported module.
#4th method.
import operator
su=operator.add(a,s)
print(su)
#5th method  -- lambda function
a=lambda x,y:x+y
n1=eval(input("enter the 1st number to sum "))
n2=eval(input("enter the 2st number to sum "))
s=a(n1,n2)
print(s)
# 6th model  ---recursive modelf
def recursive(x,y):
    if y == 0:
        return x
    else:
       return  recursive(x+1, y-1)
n1=eval(input("enter 1st recrsive values "))
n2=eval(input("enter 2st recrsive values "))
r=recursive(n1, n2)
print(r)


# Define a recursive function to add two numbers geekforgeek
def add_numbers_recursive(x, y):
	if y == 0:
		return x
	else:
		return add_numbers_recursive(x + 1, y - 1)
# Take input from the user
num1 = 1
num2 = 2
# Call the recursive function to add the two numbers
result = add_numbers_recursive(num1, num2)
# Print the result
print("The sum of", num1, "and", num2, "is", result)













































