n=int(input("enter the number "))
for i in range(0,n):
  print("*"*i)
  
o/p:  
*
**
***
****
*****
--------------------------------------
inverted triangle 
n=int(input("enter the number "))
for i in range(n,1,-1):
  print("*"*i)

o/p:
***** 
****
***
**
*
---------------------------------------------
n=int(input("enter the number "))
for i in range(0,n+1):
  print(" "*n+"* "*i)
  n=n-1
  
o/p:
    *
   * *
  * * *
 * * * *
------------------------------------------------
inverted pyramid
n=int(input("enter the number "))
m=0
for i in range(n+1,0,-1):
  print(" "*m+"* "*i)
  m=m+1
  
o/p:
* * * * * * 
 * * * * *
  * * * *
   * * *
    * *
     *
------------------------------------------------
n=int(input("enter the number "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
  
o/p: 
1
12
123
1234
12345
-----------------------------------------------------------
