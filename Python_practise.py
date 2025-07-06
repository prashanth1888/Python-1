Prime number or not
----------------------------------------------------
num=int(input("enter numbers greater than 1"))
count=0
if(num==2):
    print("is prime number")
elif(num>2):
    for i in range(1,num-1):
        if(num%(num-i)==0):
            count=count+1

    if(count>0):
        print("it is not a prime num")
    else: 
        print("prime number")

--------------------------------------------------------
