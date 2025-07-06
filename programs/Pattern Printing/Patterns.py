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
Floyd’s Triangle
n=int(input("enter the number "))
k=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(k,end=" ")
        k+=1
    print()

o/p:
1 
2 3
4 5 6
7 8 9 10
------------------------------------------------------------
n=int(input("enter the number "))
k=97
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(k),end=" ")
        k+=1
    print()

o/p:
a 
b c
d e f
g h i j
k l m n o
-----------------------------------------------------------
n=int(input("enter the number "))
k=97     #use k=65 for 'A'
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(k),end=" ")
    k+=1
    print()

o/p:
a 
b b
c c c
d d d d
---------------------------------------------------------------
learn pascal triangle 
1
11
121
1331
14641
-----------------------------------------------------------------
