#Check if a number is perfect.Sum of proper divisors equals the number. 
# Input: 28 - Output: Perfect number
# 1+2+4+7+14
num=int(input("Enter num:"))
sum=0
for a in range(1,num):
    if num%a==0:
        sum+=a
print(sum)
if num==sum:
    print("perfect number")
else:
    print("Not a perfect number")
