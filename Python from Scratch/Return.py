def cubeit(num) :
    result=(num**3)
    return result

def squareit(num) :
    result=num**2
    return result

number=int(input('Enter a number:'))
print(cubeit(number))
print(cubeit(2))
print(cubeit(3))
print(cubeit(4))
print(cubeit(5))
print(cubeit(100))

m=int(input('Enter a number:'))
n=int(input('Enter another number:'))

print(cubeit(m))
print(cubeit(n))

a=int(input('Enter a number:'))
b=int(input('Enter second number:'))
c=int(input('Enter third number:'))
print(squareit(a))
print(squareit(b))
print(squareit(c))