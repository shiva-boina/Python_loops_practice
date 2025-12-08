
#Calculate the product of digits.
# Multiply digits extracted from number. 

input=int(input("Enter num:"))
product=1
while input>0:
    rem=input%10
    product*=rem
    input//=10
print(product)
# Input: 123 
# Output: 6
