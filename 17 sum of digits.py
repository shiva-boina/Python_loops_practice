

#Calculate the sum of digits of a number. 
#Use loop and % 10 to extract digits. 
n=int(input("enter num:"))
sum=0
while n>0:
    rem=n%10
    sum+=rem
    n//=10
print(sum)

# input: 123 
# Output: 6



    
