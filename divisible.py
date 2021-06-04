num=int(input("enter the number"))
num=1
while num<=100:
    if num%3==0 and num%7==0:
        print("navgurukul",num)
    elif num%7==0:
        print("gurukul",num)
    elif num%3==0:
        print("nav",num)
    else:
        print(num)
    num=num+1