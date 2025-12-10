
#Check if a number is a strong number.
# Sum of factorial of digits equals the number. 
input=int(input("enter num:"))
temp=input
sum=0
while temp>0:
    last=temp%10
    fact=1
    for i in range(last,0,-1):
        fact*=i
    sum+=fact
    temp//=10
print(sum)
if sum==input:
    print("Strong number")
else:
    print("Not a strong number")
# Input: 145 
# Output: Strong number

