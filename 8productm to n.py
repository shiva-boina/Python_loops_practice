
#Write a program to find the product of numbers from m to n.
#Loop from m to n and multiply values.
# Input: m = 2, n = 4 

m=2
n=4
product=1
for m in range(m,n+1):
    product*=m
print(product)

# Output: 24
