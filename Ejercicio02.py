'''Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt
con la tabla de multiplicar de ese número, donde n es el número introducido, y la muestre por pantalla.
Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.'''
import os
a = int(input('Dime un número entero entre el 1 y 10 '))
file = 'tabla-' + str(a) + '.txt'
if os.path.isfile(file):
    l=open(file,'r')
    print(l.read())
else:
    print('No existe ')