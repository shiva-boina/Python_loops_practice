
#Check if a number is prime.A number is 
#prime if it has exactly 2 factors.

n=int(input("Enter num:"))
if n<2:
    print("Not a prime")
else:
   count=0
   for i in range(1,n+1):
       if n%i==0:
          count+=1
   if count==2:
       print("prime")
   else:
     print("Not prime")

#Input: n = 7  
#Output: Prime