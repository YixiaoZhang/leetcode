
x = 9
min = 0
max = 9

while(True):
    middle = int(min+max/2)
    middleSquare = middle*middle
    middlePlus1Square = (middle+1)*(middle+1)
    print(min,max,middle,middleSquare,middlePlus1Square)
    if(middleSquare<=x and middlePlus1Square>x):
        print(middle) 
        break
    if(middleSquare>x):
        max = middle
    else:
        min = middle