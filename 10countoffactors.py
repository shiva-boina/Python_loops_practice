
#Write a program to count how many factors a number has.
# Increment count when divisible. 
n=int(input("Enter no.:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
print(count,end=" ")
     
# Enter no.:6
# output:1 2 3 4 