


#  1


print('\nPunto 1 ----------------------------\n')

def histogram (lista):
    n=len (lista)
    for i in range(n):
        for j in range(lista[i]):
            print('x')
        print('\n')
histogram([1,2,3])


#  2

print('\nPunto 2 ----------------------------\n')

def MasLarga(lista):
    n=len(lista)
    masLarga=''
    for i in range(n):
        if (len(lista[i]) > len(masLarga)):
            masLarga= lista[i]
    return masLarga

print(MasLarga(['perro','gato','cuervo']))
        


#  3

print('\nPunto 3 ----------------------------\n')

txt = "hello, my name is Peter, I am 26 years old"

x = txt.split()
def NumMayus(string):
    numMayus=0
    listaDePalapras=string.split()
    for i in range(len(listaDePalapras)):
        palabra=listaDePalapras[i]
        letras=[]
        for j in range(len(palabra)):
            letras.append(palabra[j])
        for k in range(len(letras)):
            if (letras[k].isupper()):
                numMayus+=1
    return numMayus


print(NumMayus(txt))



#  4

print('\nPunto 4 ----------------------------\n')
import math

def BinaryToDecimal(binaryNumber):
    n=len(binaryNumber)
    decimalNumber=0
    for i in range(-n,-0):
        decimalNumber+=int(binaryNumber[i])*pow(2,(-i-1))
    return decimalNumber

print(BinaryToDecimal('011'))



#  5


print('\nPunto 5 ----------------------------\n')
def ContarVocales(palabra):
    vocales = dict(
            a=0,
            e=0,
            i=0,
            o=0,
            u=0
            )
    for j in range(len(palabra)):
        letra=palabra[j]
        if (letra=='a'):
            vocales['a']+=1
        if (letra=='e'):
            vocales['e']+=1
        if (letra=='i'):
            vocales['i']+=1
        if (letra=='o'):
            vocales['o']+=1
        if (letra=='u'):
            vocales['u']+=1

    return vocales
print(ContarVocales('mimamamemima'))



#  6

print('\nPunto 6 ----------------------------\n')
def Bisiesto(year):
    if (year%400 == 0):
        return True
    if (not(year%100 == 0) and year%4 == 0 ):
        return True
    else:
        return False

print(Bisiesto(2022))


#  7
print('\nPunto 7 ----------------------------\n')
def isRima(word1,word2):
    rima = [word1[-1]+word1[-2]+word1[-3],word2[-1]+word2[-2]+word2[-3]]
    semirima = [word1[-1]+word1[-2],word2[-1]+word2[-2]]
    if (rima[0]== rima[1]):
        return 'rima'
    if (semirima[0] == semirima[1]):
        return 'semirima'
    else:
        return'no rima'
print(
        isRima('roca','coma')
        )


#  8

print('\nPunto 8 ----------------------------\n')
def CalcularCapital(cInicial, interes, years):
    interes_ = pow(1+(interes/100),years)
    cFinal = cInicial*interes_
    return cFinal
print(
        CalcularCapital(10000, 4.5, 20)
        )


#  9
#  9.1
#  me dio pereza, no quiero hacer más >c 
