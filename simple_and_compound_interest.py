p = int(input('Enter principle amount: '))
b = p
r = float(input('Enter interest: '))
t = int(input('Enter time period(in years): '))
# simple interest
a = (p*t*r)/100
print("Simple interest: ",a)
# compound interest
for i in range (t):
    p = p + (r/100)*p
c = p - b
print("Compound interest: ",c)