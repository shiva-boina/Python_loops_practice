#Count consonants in a string.Check for 
#alphabetic characters not vowels. 
s=input("Enter:")
vowels="aeiouAEIOU"
count_consonants=0
for ch in s:
     if ch>="a"and ch<="z" or ch>='A' and ch<='Z':
          if ch not in vowels:
                  count_consonants+=1
print(count_consonants)
#Input: “apple” 
# Output: 3
