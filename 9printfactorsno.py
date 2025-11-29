
#Write a program to print all factors of a given number. 
#Check divisibility of number from 1 to n. 
# Input: n = 6 

n=int(input("Enter n:"))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")

# Enter n:6
# output=1 2 3 6














# i=1
# while i<=10:
#     print(i)
#     i+=1

n=int(input("Enter a num:"))
m=1
while m<=10:
    print(f"{n}*{m}={n*m}")
    m+=1
  

