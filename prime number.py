# num=int(input("enter the number"))
# f=0
# i=2
# while i<=num/2:
#     if num%i==0:
#         f=1
#         break
#     i=i+1
# if f==0:
#     print("is a prime number")
# else:
#     print("not a prime number")

#prime number
# i=1
# while i<=100:
#     j=2
#     count=0
#     while j<=i-1:
#         if i%j==0:
#             count=count+1
#         j=j+1
#     if i!=1 and count==0:
#         print(i,"prime number")
#     else:
#         print("not prime numbe")
#     i=i+1

n=int(input("enter the number"))
count=0
i=1
while i<=n:
    if n%i==0:
        count=count+1
    i=i+1
if count==2:
    print("prime number")
else:
    print("not prime number")
