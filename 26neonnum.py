
#Check if a number is a neon number.Square 
#the number, sum digits, match original. 
input=int(input("enter num:"))
sum=0
if input>0:
    sque=input**2
    while sque>0:
        rem=sque%10
        sum+=rem
        sque//=10
if input==sum:
    print("Neon number")
else:
    print("Not a Neon number")
#Input: 9 
#Output: Neon number



