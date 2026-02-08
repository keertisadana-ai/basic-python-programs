a = int(input('Enter the  numbers '))
lar = 0
small = 0
while a>0:
    b=a%10
    if lar<b:
        lar = b
    else:
        small = b
    a=a//10
print('largest number is',lar)
print('smallest number is',small)