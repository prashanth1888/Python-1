Check if the number is prime or not 
------------------------------------------------
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

num=int(input("enter numbers till large"))
st=int(input("enter minimum limit"))
for j in range(st,num+1):
    count=0
    for i in range(1,j+1):
        if(j%i==0):
            count=count+1
    if(count==2):
        print(i)

-----------------------------------------------------------
prime num using functions 

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
     
