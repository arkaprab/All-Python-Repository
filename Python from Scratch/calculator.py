a=int(input('Enter first number:'))
b=int(input('Enter second number:'))

def summation(a,b):
    sum=0
    sum=a+b
    print("Sum:" , sum)

def difference(a,b):
    if(a>b):
        diff=a-b
        print("Difference:" ,diff)
    elif(b>a):
        diff=b-a
        print("Difference:" ,diff)
    else:
        diff=0
        print("Difference:", diff)
def multiply(a,b):
    product=(a*b)
    print("Product:", product)
def division(a,b):
    div=(a/b)
    print("Division:" , div)
    
print("Press 1 to perform additon.")
print('Press 2 to perform substraction.')
print("Press 3 to perform multiplication.")
print('Press 4 to perform division.')

print("")       
choice=int(input("Enter your choice:"))
if(choice==1):
    summation(a,b)
elif(choice==2):
    difference(a,b)
elif(choice==3):
    multiply(a,b)
elif(choice==4):
    division(a,b)
else:
    print("Wrong choice.")