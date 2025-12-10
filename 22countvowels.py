
#Count number of vowels in a string.
# Loop and check for a, e, i, o, u. 
s=input("Enter:")
vowels="aeiouAEIOU"
count=0
for ch in s:
     if ch>="a"and ch<="z" or ch>='A' and ch<='Z':
        if ch in vowels:
           count+=1
print(count)
# Input: “apple” 
# Output: 2