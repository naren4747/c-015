import math 
import csv

with open(r"std.csv",newline='') as f:
    reader=csv.reader(f)
    Data=list(reader)


def mean(data):
    n=len(data)
    total=0

    for x in data:
        total+=int(x)

    mean=total/n
    return mean

squaredList=[]

for i in Data:
    a=int(i)-mean(Data)
    a=a**2
    squaredList.append(a)

sum=0

for y in squaredList:
    sum=sum+y

total=sum/len(Data)-1

sd=math.sqrt(total)

print(sd)

    