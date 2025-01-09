n=int(input("Enter the number till when you want sum of: "))
if n<0:
    print("Enter positive number")
else:
    sum=0
    while n>0:
        sum=sum+n
        n=n-1
    print(sum)    
        
