# without using third variable
a=10
b=20
a=a+b         
b=a-b         
a=a-b          
print("a=",a ,"b=",b)


# using third variable
a1=10
b1=20
temp=a1       #10
a1=b1         #a1=10
b1=temp
print("a1=",a1 ,"b1=",b1)