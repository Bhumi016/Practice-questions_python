vovwels=["a","e","i","o","u"]
word="programming"
count=0
l=[]
for char in word:
    if char not in vovwels:
        count+=1
        l.append(char)
print(count)  
print(l)      