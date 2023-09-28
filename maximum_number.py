# recursive model
# 1st method
# def maximum(x,y):
#     if x>=y:
#         return  x
#     else:
#         return y
# a=10
# b=24
# print(maximum(a,b))
#
#
# # by using max function
# 2nd method
# a=10
# b=3
# c=max(a,b)
# print(c)
#

#ternery opretor
# 3rd method
# a=int(input("enter 1st max mumber"))
# b=int(input("enter 2st max mumber"))
# print(a if a>=b else b) #--ternery opretor
#
#
# #by using lambda function    -- code is correcrt but ans is in another format.
# 4th method
a=75
b=8
print(lambda a,b:a if a>b else b)

# max of two numbers by using list comprehention
# 5ht method
# a=10
# b=20
# l=[a if a>b else b]
# print(l)
# 6th method
#sort()
z=[a,b]
z.sort()
print(z[-1])



















