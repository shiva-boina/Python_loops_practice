n = int(input("Enter number of terms: "))
a=0
b=1
for i in range(n+1):
    c=a+b
    a=b
    b=c
    print(c,end=" ")

# a, b = 0, 1

# print("Fibonacci sequence:")
# for i in range(n+1):
#     print(a, end=" ")
#     a, b = b, a + b
