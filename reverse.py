# i=int(input("enter the number"))
# rev=0
# while i>0:
#     rev=(rev*10)+(i%10)
#     i=i//10
# print("revers=",rev)

#0 se start reverse number:
# i=int(input("enter the number"))
# rev=0
# while i>0:
#     rev=(rev*10)+(i%10)
#     i=i//10
#     print("reverse=",rev//10*10)

n=[64,32,78,63,23,12,45,11,8,7,6,5,4,3,2,1]
i=0
while i<len(n):
    j=i+1
    while j<len(n):
        if n[i]> n[j]:
            n[i],n[j]=n[j],n[i]
print(n)