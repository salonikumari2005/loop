# from typing import get_origin


i=int(input("enter the number"))
orig=i
sum=0
while (i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if orig==sum:
    print("number is Armstrong")
else:
    print("number is not Armstrog")
