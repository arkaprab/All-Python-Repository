a=float(input('Enter first number:'))
b=float(input('Enter second number:'))
operator=input('Enter operator :')

if(operator == '+'):
    sum=a+b
    print(sum)
elif(operator =='-'):
    diff=a-b
    print(diff)
elif(operator == '*'):
    pr=a*b
    print(pr)
elif(operator == "/"):
    div=a/b
    print(div)
elif(operator == "^"):
    exp=(a**b)
    print(exp)


