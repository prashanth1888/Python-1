Armstrong number 

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
	#Functions -Armatrong only for  3 digit
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
	
	#Functions - for any armstrong number
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
