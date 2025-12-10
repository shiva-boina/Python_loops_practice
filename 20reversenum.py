#Reverse the digits of a number.
#Use loop with % and // to reverse. 
#Input: 123 - Output: 321
reverse=0
input=int(input("Enter num:"))
while input>0:
    rem=input%10
    reverse=reverse*10+rem
    input//=10
print(reverse)