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
Fibonacci series 
--------------------------------------------------------
num=int(input())
f1=0
f2=1
print(f1)
print(f2)
c=0
for i in range(0,num+1):
    c=f1+f2
    print(c)
    f1=f2
    f2=c
--------------------------------------------------------
Armstrong number 
--------------------------------------------------------
num=input("enter the number to check")
sum=0
result=int(num)
for i in range(0,len(num)):
    a=int(num[i])
    sum=a*a*a+sum
    
print(sum)
if(sum==result):
    print(num+"is Armstrong num")
    
-------------------------------------------------
Is it Palindrome or not 
-------------------------------------------------
str=input("enter the strig to check palindrome")
rev=str[::-1]
if(str==rev):
 print("is palindrome")
else:
    print("not palindrome ")














----------------------------------------------------------
