from rsa import *

option = ''

menu()
while option !=4:
    option = int(input())
    if option == 1:
        a = GenerarClaves()
        print('Publica: ',a[0])
        print('Privada: ',a[1])
        menu()

    if option == 2:
        m = input('Ingrese mensaje: ')
        llavePublica = input('Ingrese llave publica: ')
        enc = encriptar(llavePublica,m)

        print('Encriptado: ',enc)
        menu()

    if option == 3:
        d = input('Ingrese mensaje encriptado: ')
        llavePrivada = input('Ingrese llave privada: ')
        dec = desencriptar(llavePrivada,d)
        print('Decriptado: ',dec)
        menu()