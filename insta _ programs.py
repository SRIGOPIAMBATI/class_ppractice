# x,y =0,1
# while y<30:
#     x,y=y,x+y
#     print(y ,end=' ')             # ---> output : 1 2 3 5 8 13 21 34

# x=input(" enter data")
# y=input(" enter data")
# z=input(" enter data")
# print(x)
# print(y)
# print(z)                 #--------> i am srigopi ambati
#
#
# x,y,z=input(" enter the data ").split()
# print(x,y,z)                #---> i am srigopi ambati

# swapping of numbers in possible ways
#----> first way of approch by using temp (netive approch)
x=10
y=20
temp=x
x=y
y=temp
print(x,y)

#--> second way of approch( by usine coommma)
x=10
y=20
x,y=y,x
print(x,y)

#---> third way of approch(arithematic)
x=10
y=20
x=x+y
y=x-y
x=x-y
print(x,y)

#---> swapping of numbers by using xor opretion.
x=10
y=20
x=x^y
y=x^y
x=x^y
print(x,y)

# text printing multiple times.
for i in range(10):
    print(" hi")
#squres of numbers kby using recursive method.
def square(n):
    return n**2                                                #  [1]
x=[1,2,3,4,5,6,7,8,9]                                               #    [1, 4]
s=[]                                                  #    [1, 4, 9]
for i in x:                                                  #    [1, 4, 9, 16]
                                                   #---->    [1, 4, 9, 16, 25]
                                                    #-->    [1, 4, 9, 16, 25, 36]
                                                        #-->[1, 4, 9, 16, 25, 36, 49]
                                                       #-->[1, 4, 9, 16, 25, 36, 49, 64]
                                                       #-->[1, 4, 9, 16, 25, 36, 49, 64, 81]
    x=[1,2,3,4,5,6,7,8,9]
s=[]
for i in x:
    s.append(square(i))
    print(s)







