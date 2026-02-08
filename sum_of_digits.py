a = int(input('Enter the  numbers'))
sum = 0
while a>0:
    b=a%10
    sum = sum+b
    a=a//10
print('Sum of the number is ',sum)