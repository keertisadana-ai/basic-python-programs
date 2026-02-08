a = int(input('Enter the  numbers '))
c = a
rev = 0
while a>0:
    b=a%10
    rev = rev*10+b
    a=a//10
if rev == c:
    print('Given number is palindrome ')
else:
    print('Given number is not an palindrome ')