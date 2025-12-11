
# 1. Search character in string
text=input("Enter text:")
ch=input("Enter char:") 
f=0
for a in range(len(text)):
    if text[a]==ch:
        f+=1
        break
if f>0:
    print("Found")
else:
    print("Not found")
    
    
    # text=input("Enter text:")
# ch=input("Enter char:")
# f=0
# for i in text:
#     if i==ch:
#         f+=1
#         break
# if f>0:
#     print("found")
# else:
#     print("not found")
# I/p:
# text = "python"
# ch = "a"
# O/p: not found

# i/p: 
# text = "python"
# ch = "o”
# O/p: found


    


