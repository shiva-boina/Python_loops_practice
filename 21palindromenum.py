#Check if a number is a palindrome.
# Compare number with its reverse. 
# Input: 121 
# Output: Palindrome
input=int(input("Enter num:"))
temp=input
reverse=0
while input>0:
    rem=input%10
    reverse=reverse*10+rem
    input//=10
print(reverse)
if temp==reverse:
    print("palindrome")
else:
    print("Not a palindrome")