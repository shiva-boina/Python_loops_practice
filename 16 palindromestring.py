
#Check if a string is a palindrome. 
#Compare string with its reverse. 
# Input: “madam” 

input=input("Enter name:")
reverse=""
for ch in input:
    reverse=ch+reverse
if reverse==input:
    print("palindrome")
else:
    print("Not a palindrome")
# Output: Palindrome