a = int(input('Enter the  numbers'))
mul = 1
while a>0:
    b=a%10
    mul = mul*b
    a=a//10
print('product of the number is ',mul)
