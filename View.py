def getInt():
    x  = int(input())
    return int(x)


def getFloat():
    x = float(input())
    return float(x)



def getString():
    x = input()
    return str(x)

def getArrayInt(index:int):
    for i in range(index):
        x=[]
        x[index] = input(int())

    return x


def getArrayFloat(index:int):
    for i in range(index):
        x=[]
        x[index] = input(float())

    return x

def getLenOfArray(array:object):
    x = int(array.len())
    return x
