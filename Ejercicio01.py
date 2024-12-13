'''Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt
    la tabla de multiplicar de ese número, donde n es el número introducido.
'''
a = int(input('Dime un número entero entre el 1 y 10 '))
with open('tabla-' + str(a) + '.txt', 'w') as file:
    for i in range(11):
        file.write(str(i) + 'x' + str(a) +'=' + str(i*a) + '\n')
file.close