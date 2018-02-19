
from math import*
sum=0
x=input("give a number")
for i in range (1,x):
    print(i, "square is",i*i)
    sum = sum + (i*i)
    print "sum of first ", x-1 ,"square is" , sum
raw_input("press enter to exit")
