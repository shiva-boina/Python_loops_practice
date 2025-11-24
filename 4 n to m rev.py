
#Write a program to print numbers from n to m in reverse.
#Start from n and go down to m. 
#Input: n = 10, m = 6 
n=10
m=6
for n in range(n,m-1,-1):
    print(n,end=" ")

# Output: 10 9 8 7 6