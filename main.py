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
        enc = encriptar(a[0],m)

        print('Encriptado: ',enc)
        menu()

    if option == 3:
        d = input('Ingrese mensaje encriptado: ')
        dec = desencriptar(a[1],d)
        print('Decriptado: ',dec)
        menu()