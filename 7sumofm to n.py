
#Write a program to find the sum of all numbers from m to n. 
#Explanation: Loop from m to n and add values.
# Input: m = 3, n = 6 

m=3
n=6
sum=0
for m in range(m,n+1):
    sum+=m
print(sum)

# Output: 18