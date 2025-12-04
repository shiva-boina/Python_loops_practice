
#Count how many even and odd numbers are in the range m to n. 
#Use counters for even and odd.Input: m = 3, n = 7 
m=3
n=7
count_even=0
count_odd=0
for m in range(m,n+1):
    if m%2==0:
        count_even+=1
    else:
        count_odd+=1
print(f"Even={count_even},odd={count_odd}")

#Output: Even = 2, Odd = 3

    