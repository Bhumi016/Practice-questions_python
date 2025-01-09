n=1
while n<=100:
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print(n,"is prime number")

    n+=1                