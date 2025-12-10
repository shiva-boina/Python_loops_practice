
#vowels and consonants in input string.
#Maintain two counters. 
s=input("enter:")
count_vowels=0
count_cosonants=0
vowels="aeiouAEIOU"
for ch in s:
    if (ch>='a'and ch<='z') or (ch>='A' and ch<='Z'):
        if ch in vowels:
            count_vowels+=1
        else:
            count_cosonants+=1
print("vowels =",count_vowels)
print("consonants =",count_cosonants)

#Input: “apple” 
#Output: Vowels = 2, Consonants = 3


