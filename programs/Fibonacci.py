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
  ----------------------------------
