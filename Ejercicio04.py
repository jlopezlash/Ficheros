'''Escribir un programa que acceda al fichero de internet mediante la url indicada y
muestre por pantalla el número de palabras que contiene.'''
import urllib.request
url = 'http://textfiles.com/adventure/aencounter.txt'
file = urllib.request.urlopen(url)
for line in file:
    f = file.read()
    '''decoded_line = line.decode("utf-8")'''
    o = len(f.split())
    print(o)
    file.close()