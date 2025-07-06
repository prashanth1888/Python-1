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

----------------------------------------------------------
Prime numbers in the given range 
----------------------------------------------------------

num=int(input("enter numbers till large"))
st=int(input("enter minimum limit"))
for j in range(st,num+1):
    count=0
    for i in range(1,j+1):
        if(j%i==0):
            count=count+1
    if(count==2):
        print(i)

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


--------------------------------------------------
=> Some programs Using Functions
-----------------------------------------------------

	def factorial(n):
	    if n == 1:
	        return 1
	    return n * factorial(n - 1)
	print(factorial(5))  # Output: 120
	
	Check if it is a palindrome :
	def palindrome(s):
	    y=str(s)
	    x=y[::-1]
	    if(y==x):
	        print("is palindrome")
	    else:
	        print("not palindrome")
	palindrome(121)
	
	Reverse of a string
	def reverse(s):
	    x=s[::-1]
	    return x
	print(reverse("ravi"))
	
	Finding largest among three number
	def maxnum(a,b,c):
	    if(a>b):
	        if(a>c):
	           return print(a,"is largest")
	        else: 
	           return print(c,"is largest")
	    elif(b>c):
	        return  print(b,"is largest")
	        
	    else:
	        print(c,"is largest")
	maxnum(9,5,3)
	
	def maxnum(a,b,c):
	    if(a>b and a>c):
	        print(a)
	    elif(b>a and b>c):
	        print(b)
	    else:
	        print(c)
	    
	maxnum(9,15,23)
	
	Count no.of vowels 
	def vow(s):
	    count=0
	    for chaar in s:
	        if(chaar=='a' or chaar=='e' or chaar=='i' or chaar=='o' or chaar=='u' 
	        or chaar=='A' or chaar=='E' or chaar=='I' or chaar=='O' or chaar=='U'):
	            count=count+1
	    return count
	    
	print(vow("aeiAAaaou"))
	
	Check prime number 
	def prime(n):
	    count=0
	    for i in range(2,n):
	        if(n%i==0):
	            count=count+1
	    if(count==0 and n>2):
	        return "is prime"
	    else:
	        return "not prime"
	        
	print(prime(10))
	
	List of squares upto given number 
	def sqr(n):
	    x=[0]*(n)
	    for i in range(0,n):
	        x[i]=(i+1)*(i+1)
	        
	    return x 
	print(sqr(9))
	
	Armatrong only for  3 digit
	def am(n):
	    c=n%10
	    b=(n//10)%10
	    a=n//100
	    z=a*a*a+b*b*b+c*c*c
	    if(n==z):
	        return "is armstrong"
	    else:
	        return "not a amstrong nuber"
	print(am(153))
	
	for any armstrong number
	def am(n):
	    s=str(n)
	    add=0
	    for digit in s:
	        m=int(digit)
	        add=add+m*m*m
	    if(add==n):
	        return "is armstrong"
	    else:
	        return "not armstrong"
	print(am(153))
-------------------------------------------------------













----------------------------------------------------------
