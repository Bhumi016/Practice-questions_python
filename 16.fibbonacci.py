n=int(input("Enter any number: "))
n1,n2=0,1
count=0
if n<=0:
    print("Enter positive number")
elif n==1:
    print("fibonacci series upto:",n)
    print(n1)    
else:
    while count<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1   


















                  