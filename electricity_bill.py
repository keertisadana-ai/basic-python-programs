unit=int(input('Enter the unit '))
bill = 0
if unit>100:
    unit-=100
else:
    unit = 0
# slab 1
if unit > 0:
    if unit >= 300:
        bill+=300*4.7
        unit-=300
    else:
        bill+=unit*4.7
        unit = 0
# slab 2
if unit > 0:
    if unit >= 100:
        bill+=100*6.3
        unit-=100
    else:
        bill+=unit*6.3
        unit = 0
# slab 3
if unit > 0:
    if unit >= 100:
        bill+=100*8.4
        unit-=100
    else:
        bill+=unit*8.4
        unit = 0
# slab 4
if unit > 0:
    if unit >= 200:
        bill+=200*9.45
        unit-=200
    else:
        bill+=unit*9.45
        unit = 0
# slab 5
if unit > 0:
    if unit >= 200:
        bill+=200*10.5
        unit-=200
    else:
        bill+=unit*10.5
        unit = 0
# slab 6
if unit > 0:
    if unit >= 1000:
        bill+=1000*11.55
        unit-=1000
    else:
        bill+=unit*11.55
        unit = 0
print(" The bill amount is ", bill)