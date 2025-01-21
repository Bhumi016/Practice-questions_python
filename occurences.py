word="programming"
char=input("Enter the character to count: ")
count=0
for i in word:
    if i==char:
        count+=1
print(count)        