number=5
i=1
while i<=5:
    guess=int(input("enter a number"))
    if guess<number:
        print("your guess is to low")
    if guess>number:
        print("your guess is to high")
    if guess==5:
        print("congratulation!your guess is correct")
        break
    i=i+1
if i>5:
    print("your guess is wrong")


# i=0
# str1='python'
# while (i<len(str1)
#     if str[1]=='y' or str[1]=='h':
#         i=i+1
#         continue
#         print("counter letter:,str[1]")
#     i=i+1
'''count=0
i=1
while i<=100:
    num=int(input("enter the number"))
    if i^2==0:
        print("square of number is",)''' 