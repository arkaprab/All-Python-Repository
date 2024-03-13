def biggestof(a,b,c):
    if(a >=b and a>=c):
        print(a," is the biggest number.")
    elif(b>=a and b>=c):
        print(b, " is the biggest number.")
    elif(c>=a and c>=b):
        print(c, " is the biggest number.")
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))
c=int(input('Enter the third number:'))

biggestof(a,b,c)
print(" ")
def smallestof(a,b,c):
    if(a<=b and a<=c):
        print(a ," is the smallest number.")
    elif(b<=a and b<=c):
        print(b ," is the smallest number.")
    elif(c<=a and c<=b):
        print(c, " is the smallest number.")
smallestof(a,b,c)