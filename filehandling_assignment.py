# creating folder employe
import os
cwd=os.getcwd()
print("current working directory inside current directory",cwd)
#  this commander is used for creat the folder /direcotry
# os.mkdir("empolyee")
# os.mkdir("class practice")
# this command is used for remove folder /directory
# os.rmdir("class ppractice")
import csv
with open ("employe_data.csv","w") as file:
    writer_obj=csv.writer((file))
    writer_obj.writerow(["employename,departmentname,job, employenumber ,hiredate,loc,salary"])
    n=int(input(" enter number of employes:"))
    for i in range(n):
        employename=input(" enter employe name:")
        departmentname=input(" enter department name:")
        job=input("enter the job ")
        employenumber=input("employenumber")
        hiredate=input("hire date:")
        loc=input("loc")
        salary=input("salary")
        writer_obj.writerow([employename,departmentname,job,employenumber,loc,salary])
        print(writer_obj)
file =open("employe_data.csv","r")
reader_obj=csv.reader(file)
data=list(reader_obj)
for row in data:
    #print(line)
    for word in row:
        print(word,"\t",end=' ')
    print()
# OUTPUT:
# employename,departmentname,job, employenumber ,hiredate,loc,salary
#
# ravi 	 RESEARCH 	 CLEARK 	 1 	 HYD 	 2000
#
# RAMU 	 SALES 	 HYD 	 2 	 HYD 	 1000
#
# RAJU 	 ACCOUNTING 	 MANAGER 	 3 	 HYD 	 3000
#
# REMO 	 RESEARCH 	 CLERK 	 4 	 HYD 	 3500
#
# RANI 	 SALES 	 ANALYST 	 5 	 HYD 	 4000
#
# ROJA 	 SALES 	 CLERK 	 6 	 HYD 	 500
#
# import employe_data.csv as employ:
# from i in emplye_data:
if i>=3000:
    print(" names of empolyes:names")
else:
    print(" none")



