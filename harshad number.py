sum=0
n=int(input("enter the number"))
c=n
while c>0:
    r=c%10
    sum=sum+r
    c=c//10
if n%sum==0:
    print(n,"is harshad number")
else:
    print(n,"is not harshad number")