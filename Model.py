import math as m
import View

def voidGetDiv(position:int,index:int,case:int): 
    radPosition = int(m.sqrt(position))
    divisors = []
    i = 2
    while i <= radPosition:
        if position%i == 0:
            divisors.append(i)
            if int(position/i) != i:
                divisors.append(int(position/i))
        i = i+1
    divisors.append(position)
    divisors.sort()
    divisorsLen = len(divisors)
    if case == 1:
            return divisorsLen
    elif case == 2:
        if index > divisorsLen:
            return divisors[0]
        else:
            return divisors[index]
    elif case == 3:
        return divisors
    elif case == 4:
        if divisorsLen == 1:
            return str(True)
        else:
            return str(False)
    


def voidFindPrimeNum(number:int):
    for i in range(number-1):
        if i >1:
            x= number%i
            if x==0:
                return False
            else:
                    return True


def transportB10toB2(number: int):
    arrayNumB2 =[]
    while number >=2:
        arrayNumB2.append(number%2)
        number = int(number/2)
    arrayNumB2.append(number)
    reversedB2=[]
    for item in reversed(arrayNumB2):
        reversedB2.append(item)
    return reversedB2
 
def isNumber(number:object):
    try:
        y = int(number)
    except:
        return False
    
def anyBaseTodecimal(number: int, sistem:int):
    while number>=sistem:
        pass

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def mcm(a, b):
    while b:
        a, b=  b, a % b
        return a
