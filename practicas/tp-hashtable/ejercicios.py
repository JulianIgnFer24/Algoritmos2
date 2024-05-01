import math
"""
ejercicio 2
"""
def functionHashMetodoMultiplicacion(k):
    m = 1000
    A = math.sqrt(5)-1/2
    hashnumber = math.floor(m * (k * A % 1))
    return hashnumber


"""
ejercicio 4
"""
def ejercicio4():
    #el orden de complejidad es O(n) donde n es la longitud de la cadena
    text1 = "hola"
    text2 = "alkh"
    suma1 = 0
    suma2 = 0
    if len(text1) != len(text2):
        return False
    for i in range (0,len(text1)):
        suma1 = suma1 + ord(text1[i]) * ord(text1[i])
        suma2 = suma2 + ord(text2[i]) * ord(text2[i])
    
    if suma1 == suma2:
        return True
    else:
        return False

"""
ejercicio 5
"""
def ejercicio5(L):
    #el orden de complejidad es O(nlogn) donde n es la longitud de la lista
    L = sorted(L)
    for i in range(0,len(L)-1):
        if L[i] == L[i+1]:
            return False

"""
ejercicio 6
"""
def hashCodigoPostal(codigo):
    hashnumber = 0
    m = 1000
    A = math.sqrt(5)-1/2
    for i in range(0,len(codigo)):
        hashnumber += math.floor(m * (ord(codigo[i]) - (math.pi * ord(codigo[i]) - math.e * ord(codigo[i])) * A) % 1000) - ord("A")
    return abs(hashnumber) % 1000

    
#print("codigo postal",hashCodigoPostal("A000AAA"))

#codigosPostales = ["ABS123ABC","CDE456CDE","FGH789FGH","IJK012IJK","LMN345LMN","OPQ678OPQ","RST901RST","UVW234UVW","XYZ567XYZ","ABC890ABC","DEF123DEF","GHI456GHI","P111PPP","A0000AAA"]
#for i in range(0,len(codigosPostales)):
#    print("codigo postal ",codigosPostales[i],": ",hashCodigoPostal(codigosPostales[i]))

"""
ejercicio 7
"""
def compressString(s):
    compress = ""
    cont = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            cont = cont + 1
        else:
            compress = compress + s[i] + str(cont)
            cont = 1
    compress += s[len(s)-1] + str(cont) #el ultimo paso lo hago afuera porque dentro del bucle no tengo para comparar con el siguiente caracter
            
    if len(compress) < len(s):
        return compress
    else:
        return s


#print(compressString("aaabbbbcddddddeeeeffff"))

"""
ejercicio 8
"""
def patronNum(s):
    numPatron = 0
    for i in range(0,len(s)):
        numPatron = numPatron + ord(s[i])*i
    return numPatron

def ocurrencia(s,substring):
    #el orden de complediad es O(n*m) para el peor de los casos donde n es la longitud de la cadena y m la longitud de la subcadena pero seria de O(n-m+1) en el caso promedio
    patronSubString = patronNum(substring) #le asigno un numero a la subcadena
    
    for i in range(0,len(s)-len(substring)+1):
        if patronSubString == patronNum(s[i:i+len(substring)]):
            return i
        
print(ocurrencia("hola","ol"))

"""
ejercicio 9
"""
def included(conjunto1,conjunto2):
    if len(conjunto1) > len(conjunto2):
        return False
    #else:
        
    