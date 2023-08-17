#1)Write a Python script to concatenate the following dictionaries to create a new one.
#Sample Dictionary :
#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}

# d1={1:2,3:4}
# d2={6:7,8:9}
# d3={21:54,65:67}
# d4={2:4,5:6}
# d5={}
# for d in (d1,d2,d3,d4):
#     d5.update(d)
# print(d5)

# output:
#{1: 2, 3: 4, 6: 7, 8: 9, 21: 54, 65: 67, 2: 4, 5: 6}

#2) x={'A':1,'B':'5'} o/p :{1:'A','5':'B'} interchange the keys and values

# a={'s':2,'b':3,'c':4,'d':5}
# a_swap={v:k for k,v in a.items()}
# print(a_swap)
# output:
# {2: 's', 3: 'b', 4: 'c', 5: 'd'}


#3) x= {'1':['a','b'], '2':['c','d']} Expected Output: ['ac','ad','bc','bd']
#
# x= {'1':['a','b'], '2':['c','d']}
# print(x.values())
# for v in x.values():
#     print(v)
#
# #4. Write a Python program to print all distinct values in a dictionary.

# s= [{"V":"S001"}, {"V": "S002"}, {"V": "S001"}, {"V": "S005"}, {"V":"S005"}, {"V":"S009"},{"V":"S007"}]
# print(s)
# v=set(val for dic in s for val in dic.values())
# print(v)
# output:{'S005', 'S001', 'S009', 'S002', 'S007'}
#
#5. x={'A':3,'B':5,'C':4,'D':2,'E':1} Arrange keys and values as per ascending order of values
#o/p : {'E':1,'D':2,'A':3,'C':4,'B':5}
#
# x={'a':3,'b':5,'c':4,'d':2,'e':1}
# # a=sorted(x)
# # print(a)
# # b=list(x.keys())
# # b.sort()
# #s=lambda(k,v):((k,v)(v,k))
# #print(s)
# # y={}
# a=dict(sorted(x.items(),key=lambda x:x[-1]))
# print(a)
# # for i in sorted(x):
# #    y[i]=x[i]
# # print(y,end=' ')
#
#6.{'A': 'Red' , 'D': None 'B': 'Green', 'C': None} New Dictionary after dropping None items
#  o/p :{'A': 'Red', 'B': 'Green'}
#
# x={1:'red',2:'None', 3:' green',4: 'None'}
# print(x.pop(2))
# print(x.pop(4))
# print(x)

#7.
#x={'A':123,'B':100} check key is exits or not in dic  , key= take key from input use eval fun
# x={'a':123,'b':100}
# if x.get("b")==None:
#     if x.get("a")==None:
#      print(" not present")               --> its not correct
# else:
#      print(" present")

#8. x='Hello PYTHON who ARE YOU'
# o/p : {'H':'HELLO','P':'PYTHON','W':'WHO','A':'ARE','Y':'YOU'}

#x='Hello PYTHON who ARE YOU'---->idont know
#9){'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]} reverse the list values in the dictionary:
#{'C1': [30,20,10], 'C2': [40,30,20], 'C3': [34,12]}



#{1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
#Length of dictionary values: o/p : {'red': 3, 'green': 5, 'black': 5, 'white': 5}

x={1:'red',2:'green',3:'black',4:'white',5:'black'}
print(len(x))



























