num1=int(input("Enter any number:"))
num2=int(input("Enter second number:"))
gcd=1
for i in range(1,min(num1,num2)):
    if num1%i==0 and num2%i==0:
        gcd=i
print(gcd)        
    