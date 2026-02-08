data = int(input('Enter the data (in GB): '))
amount = 0
if data > 1:
    data -= 1
else:
    data = 0
    
if data > 0:
    if data >= 2:
        amount += 2*50
        data -= 2
    else:
        amount += data*50
        data = 0
    
if data > 0:
    if data >= 3:
        amount += 3*75
        data -= 3
    else:
        amount += data*75
        data = 0
    
if data > 0:
    amount += data*100
print('The amount is ',amount)

    