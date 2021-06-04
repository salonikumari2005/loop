start=int(input("enter the start year:"))
end=int(input("enter the end year:"))
if start<end:
    print("here is a list of leap year between"+str(start)+"and"+str(end)+":")
    while start<end:
        if start%4==0 and start%100!=0:
            print(start)
        if start%100==0 and start%400==0:
            print(start)
        start+=1
    if start>=end:
        print("check your year input again.")