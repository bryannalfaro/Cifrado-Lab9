import numpy as np
import random
import base64

def gcd(a,b):
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def egcd(a, b):
    xp  = 0
    yp = 1
    if a == 0:
        return b, xp, yp
    else:
        gcd, x, y = egcd(b % a, a)
        xp = y - (b // a) * x
        yp = x
        return gcd,xp, yp


def modInverse(a,n):

    g,x,y =egcd(a,n)
    if(g!=1):
        return 'No existe inverso'
    else:
        res = x%n
        return res
def binpow(a,b):
    if b==0:
        return 1
    result = binpow(a,b//2)
    if b % 2:
        return result * result *a
    else:
        return result*result

def testFermat(n,k):
    prime = True
    pruebas = []
    for i in range(0,k):
        a = np.random.randint(2,n-2)
        pruebas.append(a)
        if (binpow(a,n-1)%n)!=1:
            prime = False
    if prime:
        return prime,pruebas
    else:
        return prime,a

def generatorPrimes(longitud,cantidad):
    numb = '2'+(longitud-1)*'0'
    numb = int(numb)
    primos = []
    while len(primos) < cantidad:
        numero = np.random.randint(numb, numb*10-1000)
        if testFermat(numero,5)[0]==True:
            primos.append(numero)
        else:
            pass

    if primos[0]==primos[1]:
        generatorPrimes(longitud,cantidad)
    else:
        return primos
def GenerarClaves():
    primos = generatorPrimes(3,2)
    p =primos[0]
    q =primos[1]
    N = p*q
    phi = (p-1)*(q-1)
    e = random.randint(1,phi)
    g  = gcd(e,phi)
    while g!=1:
        e = random.randint(1,phi)
        g  = gcd(e,phi)
    d = modInverse(e,phi)
    public = str(str(e)+'.'+str(N)).encode('ascii')
    publickey = base64.b64encode(public).decode()
    private = str(str(d)+'.'+str(N)).encode('ascii')
    privatekey = base64.b64encode(private).decode()
    return publickey,privatekey

#Encriptacion utilizando la formula : c = m^e%N
def encriptar(pk, mensaje):
    po = base64.b64decode(pk).decode('ascii').split('.')

    llavePMensaje = ""

    for i in mensaje:
        m = ord(i)

        llavePMensaje += str(pow(m,int(po[0]),int(po[1]))) + " "
    return llavePMensaje

#Desencriptacion utilizando la formula : m = c^d%N
def desencriptar(prk,encriptado):
    po = base64.b64decode(prk).decode('ascii').split('.')
    mensajeDesencriptado = ""

    partes = encriptado.split()
    for j in partes:
        if j:
            c = int(j)
            mensajeDesencriptado += chr(pow(c,int(po[0]),int(po[1])))+ ""
    return mensajeDesencriptado

def menu():
    print("Ingrese la opcion:")
    print('1. Generar claves')
    print('2. Encriptar mensaje')
    print('3. Decriptar mensaje')
    print('4. Salir')


