
#Check if a number is divisible by the sum of its digits.
#Calculate digit sum and check divisibility. 
input=int(input("enter num:"))
temp=input
sum=0
while input>0:
     last=input%10
     sum+=last
     input//=10
print(sum)
if temp%sum==0:
        print("Harshad number")
else:
      print("Not a Harshad number")
#Input: 18 
# Output: Harshad number
