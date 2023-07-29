import numpy as np 


arrrr = [[0, 1, 0, 0,],[1, 1, 0, 0,], [0, 0, 0, 0,], [0, 0, 0, 0,],]
arr = np.array([[0, 0, 1, 0,],
                [0, 0, 1, 0,], 
                [0, 1, 1, 1,], 
                [0, 0, 0, 0,],])


x = 3
y= 2

outarr = arr
outarr[x][y] = 5



point = arr[x][y]
print()
print(outarr)
print()
print(f"Point(5) Location: {x},{y}")
print()


def up(x,y):  #FOOLPROOF FLAWLESS
    logs = []
    for i in range(x):

        if arr[i][y] == 1:
            logs.append("True")
        else:
            logs.append("False")
    lsl = (list(set(logs)))
    if len(lsl) > 1:
        return False
    elif lsl[0] == "True":
        return True
    elif lsl[0] == "False":
        return False
    
    
def down(x,y): #FOOLPROOF
    logs = []
    for i in range(len(arr)-(x+1)):

        if arr[x + i+1][y] == 1:
            logs.append("True")
        else:
            logs.append("False")
            
    lsl = (list(set(logs)))
    if len(lsl) > 1:
        return False
    elif len(lsl) == 0:
        return False
    elif lsl[0] == "True":
        return True
    elif lsl[0] == "False":
        return False
    
def left(x,y): #FOOLPROOF
    logs = []
    
    for i in range(y):

        if arr[x][i] == 1:
            logs.append("True")
        else:
            logs.append("False")
            
    lsl = (list(set(logs)))
    if len(lsl) > 1:
        return False
    elif len(lsl) == 0:
        return False
    elif lsl[0] == "True":
        return True
    elif lsl[0] == "False":
        return False
    
    
    
def right(x,y):
    logs = []
    for i in range(len(arr[x])-(y+1)):  

        if arr[x][y+i+1] == 1:
            logs.append("True")
        else:
            logs.append("False")
    
    lsl = (list(set(logs)))
    if len(lsl) > 1:
        return False
    elif len(lsl) == 0:
        return False
    elif lsl[0] == "True":
        return True
    elif lsl[0] == "False":
        return False
    
    
def check(x,y):
    for i in range(len(arr[0]) * 4):
        if [x,y] in [[0, i], [i, 0], [i, len(arr[0])]]:
            return True
    
    
print(f"UP: {up(x,y)}")
print()
print(f"DOWN: {down(x,y)}")
print()
print(f"LEFT: {left(x,y)}")
print()
print(f"RIGHT: {right(x,y)}")
print()

if up(x,y) == True:
    print("The Point Touches the Edge")
elif down(x,y) == True:
    print("The Point Touches the Edge")
elif left(x,y) == True:
    print("The Point Touches the Edge")
elif right(x,y) == True:
    print("The Point Touches the Edge")
elif check(x,y) == True:
    print("The Point Touches the Edge")

print()