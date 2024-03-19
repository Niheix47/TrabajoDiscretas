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
        a, b = b, a % b
    return a
------
def numero_a_letra(numero):
    conversion = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g'}
    return conversion.get(numero, '')

def decimal(numero, base):
    if base < 2 or base > 16:
        print("Base no válida. Debe estar entre 2 y 16.")
        return

    resultado = ""
    while numero > 0:
        digit = numero % base
        # Convertir el dígito a letra si es necesario
        if digit >= 10:
            digit = numero_a_letra(digit)
        resultado = str(digit) + resultado
        numero //= base

    return resultado

def main():
    try:
        decimal_numero = int(input("Ingresa un número decimal: "))
        base_eleccion = int(input("Elige una base (2-16): "))

        base_resultado = decimal(decimal_numero, base_eleccion)
        print(f"El número {decimal_numero} en base {base_eleccion} es: {base_resultado}")

    except ValueError:
        print("Ingresa un número decimal válido.")

if _name_ == "_main_":
    main()
--------------------
