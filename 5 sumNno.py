
#Write a program to calculate the sum of first n  natural
# numbers.Use formula or loop to sum from 1 to n. 
# Input: n = 5  

n=5
sum=0
for i in range(n+1):
    sum+=i
print(sum)

# Output: 15
n=int(input("Enter no:"))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print(sum)
    
