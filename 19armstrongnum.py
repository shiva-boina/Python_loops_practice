
#Check if a number is an Armstrong number.
# Sum of cube of digits equals the number.  
# Input: 153 - Output: Armstrong number
input=int(input("Enter num:"))
temp=input
sum=0
while input>0:
    rem=input%10
    sum+=rem**3
    input//=10
if sum==temp:
    print("Armstrong number")
else:
    print("Not a Armstrong number")


