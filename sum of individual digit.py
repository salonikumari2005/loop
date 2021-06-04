i=int(input("enter a number to find sum of digit of given number"))
sum=0
while(i>0):
    sum=sum+i%10
    i=i//10
print("sum of digit=",sum)