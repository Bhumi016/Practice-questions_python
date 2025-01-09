n=int(input("enter number: "))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10

if n==sum:
    print(f"the {n} is armstrong number")
else:
    print(f"the {n} is not armstrong number")        




   




