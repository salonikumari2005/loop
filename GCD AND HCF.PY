num1=int(input("enter the number"))
num2=int(input("enter the number"))
i=1
while num1%num2!=0:
    a=num1%num2
    num1=num2
    num2=a
    i+=1
print(num2,"is the HCF of input number")