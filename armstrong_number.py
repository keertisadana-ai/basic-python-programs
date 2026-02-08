a = int(input('Enter the  numbers '))
c = a
num = 0
while a>0:
    num = num+1
    a=a//10
arm = 0
while c>0:
    b=c%10
    arm += b**num
    c=c//10
print('Armstrong number is ',arm)