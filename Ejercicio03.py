'''Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt
con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero.
Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.'''
import os
a = int(input('Dime un número entero entre el 1 y 10 '))
b = int(input('Dime un número entero entre el 1 y 10 '))
file = 'tabla-' + str(a) + '.txt'
if os.path.isfile(file):
    l=open(file,'r')
    x = l.readlines()
    print(x)
    k = x[b]
    print(k)
    l.close()
else:
    print('No existe ')