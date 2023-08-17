
#1 Write a fun sum of given numbers pass 1,2,3 n return result is 6
# adding two number by using function
# def add(x,y,z):
#     result=x+y+z
#     return result
# n1=int(input(" enter the  1st number"))
# n2=int(input(" enter the 2nd number"))
# n3=int(input(" enter the 3rd number"))
# result=add(n1,n2,n3)
# print(result)

#2.
#write a fun to print even and odd num in list -> pass list to fun
#x = list(range(1, 11))->(1, 10)
#i=int(input(" enter the input"))
# its my logic but small problem

# a=[]
# n=int(input(" enter the upper limit:"))
# #def even_number(even,odd):
# even=[]
# odd=[]
# for i in range(1,10):
#    if i%2==0:
#        even.append(i)
#    else:
#        odd.append(i)
#     #b=int(input(" enter the element"))
#     #a.append(b)
#  # even=[]
#  # odd=[]
#  # for j in a:
#  #  if j%2==0:
#  #    even.append(j)
#  #  else:
#  #     odd.append(j)
# print(" print the even",even)
# print(" print the odd ",odd)
# my wone logic
# a=[]
# n=int(input(" enter the number of range:"))
# def even_number(n):
#  for i in range(n+1):
#     b= int(input(" enter the elements:"))
#     a.append(b)
# even=[]
# odd=[]
# for j in a:
#  if j%2==0:
#   even.append(a)
#  else:
#    odd.append(a)
#
#
# print(even_number(even))
# print(even_number(odd))
"""it is refer from the google "
#a=[]
#n=int(input("Enter number of elements:"))
#for i in range(1,n+1):
#    b=int(input("Enter element:"))
#    a.append(b)
#even=[]
#odd=[]
#for j in a:
#    if(j%2==0):
#        even.append(j)
#    else:
#        odd.append(j)
# print("The even list",even)
# print("The odd list",odd)
"""

#3.
#write a program for default args and return result
# def defalut_argument(a="0",b="0"):
#     print("values",a,b," sum is",a+b)
# #  sum=a+b
#     return a+b
#defalut_argument(6666,1234252362)

#4.
#write a  fun to print multiplication table  # pass n from keyboard
# 5*1=5
# 5*2=10
# 5*3=15
# 5*4=20
# 5*5=25
# 5*6=30
# 5*7=35
# 5*8=40
# 5*9=45
# 5*10=50
#n=5
#n=int(input(" enter the number for multiplication"))

# def multipilication_table(n):
#  for i in range(1,11):
#    print(n," *",i,' =',n*i)
# n = int(input(" enter the number for multiplication"))
# print(multipilication_table(n))


#5.
# write a function pass n of args and return list using variable len args
# def sum(*n):
# 2) total=0
# 3) for n1 in n:
# 4) total=total+n1
# 5) print("The Sum=",total)
# 7) sum()
# 8) sum(10)
# 9) sum(10,20)
# 10) sum(10,20,30,40)

#
# def sum(*n):
#  total=0
#  for i in n:
#   total=total+i
#  print(" the num ",total)
#
#
# sum(1,2,3)
# sum(10,20,30,40,90)
# sum(56649846514,32464789,5468789456,654646452)

# 6 write a function pass keyword args nd return dict (a=10,b,20,c=30)  -> {a:100,b:400,c:900}
# def argu(a,b,c):
# # #dict={ }
# #    #numbers=dict(a,b,c)
# # #keys=(a,b,c)
#   print(dict(a=a,b= b,c= c))
# #
# #argu(keys,values
# argu( a =1,b=2,c= 3)
# argu(a="1000",b="2093209",c="284982059")
#


#7.
# #write a function to fetch first word from list elements x=["PYTHION IS GOOd","JAVA IS GOOD"]  # ["PYTHON","JAVA]
# n=["python is good","java is good"]
# print(n)
# string=' '.join(n)
# print(string)
# #a=string[0:6]
# #b=string[15:20]
# #a=n[0]
# if type(string)==str:
#     print ("True")
# else:
#     pass
# print(list(string[0:6]))
#print(list(string[15:19]))

#def fun(n):
#  ' '.join(n.spilit())
# for i in n:
#     i=" python"
#     print(i)
#     for j in n:
#       j=" java"
#       print(j)
#       break
# print(fun(n))
# # test_list=["yes","no","yes","no"]
# # sub_list=" python"," java"
# # for ele,val in zip(n,test_list):
# #  if sub_list in val:
# #   print(ele,end=' ')
# #


# 8 write a fun to change string lower to upper and upper to lower  and return the string  write fun to get only vowels from the list
# a=" i am here to help you"
# vowel=['a', 'e', 'i', 'o', 'u']
# def lower_upper(a):
#   vowel = ['a', 'e', 'i', 'o', 'u']
#   b=a.upper()
#   print(b,end=' \n')
#   c=b.lower()
#   print(c,end= ' \n ')
#
# #while True:
#   if  a in vowel:
#    return True
#   else:
#     return False
# out=list(filter(lower_upper,a))
# print(out)
#
# lower_upper(a)
# print(lower_upper(a))


# 9 x=["PYTHION IS GOOd","JAVA IS GOOD"]   ->[I,O,I,O,O,A,A,I,O O]  -> remove the duplicates -> ['I','O','A']

# i=["10,20,30,40,50,50,40,30,20,60"]
# l=[]
# final_list=[]
# for value in i:
#     if type(value)==str:
#         a=l.append(i)
#         print(a)
#         pass
# def remove_duplicates(l):
#  for elment in l:
#   if elment not in final_list:
#    print(elment)
#    final_list.append(elment)
#  return final_list
#
#
# remove_duplicates(final_list)
# out={ }
# for i in input :
#  if i in out.keys():
#   continue
# out=input.count(i)
# print(out)


# 10 write a function get the max num from list without using predefined fun max   x=[101,200,3000,400]  #max : 3000
# x=[1,2,34,56,75,787,9897,9898998]
# a=None
# for i in x:
#     if a is None  or a<i:
#         a=i
# print(a)
# print(x.index(a))


# 11 write a function to sort the list without using sort fun     hint: we can use sorted fun
# x=[9,8,6,7,2,1,-1,0,838,-989]
# y=[]
# while x:
#     minimum = x[0]
#     for i in x:
#       if i < minimum:
#         minimum = i
#     y.append(minimum)
#     x.remove(minimum)
# print(y)
# print(y[0])
# #print(y[:-1])
# #def sorrting_function():

# 12. Python Program to Check Prime Number
#def prime_number(number):
# n=int(input(" enter the number to check prime number or not :"))
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c=c+1
# if c==2:
#      print("% is prime ",n)
# else:
#     print(" is not number",n)


# 13. Python Program to Find Sum of Natural Numbers Using Recursion
# def sum_natural_number(n):
#     if n<=1:
#         return n
#     return n + sum_natural_number(n-1)
# n=5
# if n<0:
#  print(" netre a postive number")
# else:
#     print(" the sum is",sum_natural_number(n))


# 14.Python Program to Capitalize the First Character of a String

# x= "srigopi"
# y=x.title()
# print(y)

# 15. Python Program to Check If Two Strings are Anagram
#       Ex1: Race and Care are anagrams strings
#       Ex2: Sai and Ias are angram strings
#
# x=eval(input(" enter the input1 to check"))
# y=eval(input(" enter the input2 to check "))
# if  len(x)==len(y):
#  s=0
#  s1=0
# for i in x:
#     s=s+ord(i)
# for j in y:
#     s1=s1+ord(j)
# if s1==s:
#     print(" the given inputs are anagrams ")
# else:
#     print(" the given inputs are not anagrams")
#






# it is import freom git sir codes
# selected_option = input("Please select any one options below: "
#       "1.Aadhaar Card Numbers \n"
#       "2.Passport Numbers \n"
#       "3.Car Numbers \n"
#       "4.Mobile numbers \n"
#       )
# aadhar_numbers =set()
# passport_numbers=set()
# car_numbers=set()
# mobile_numbers=set()
#
# if selected_option == '1':
#     aadhaar_no = input("Enter your aadhar number:")
#     aadhar_numbers.add(aadhaar_no)
#     print("Aadhar number added successfully")
# elif selected_option == '2':
#     passport_no = input("Enter your passport number:")
#     passport_numbers.add(passport_no)
#     print("Passport number added successfully")
# elif selected_option == '3':
#     car_no = input("Enter your car number:")
#     car_numbers.add(car_no)
#     print("Car number added successfully")
# elif selected_option == '4':
#     mobile_no = input("Enter your mobile number:")
#     mobile_numbers.add(mobile_no)
#     print("Mobile number added successfully")
# else:
#     print("You have selected invalid operation, please try again")
#
# print(aadhar_numbers)
# print(car_numbers)
# print(mobile_numbers)
# print(passport_numbers)
#










