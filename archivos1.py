from io import open

#1) Este lo usamos para crear el archivo
archivo_texto=open('nombres.txt','r')

#archivo_texto.write('\n datos en el archivo')


#print(archivo_texto.read())
#archivo_texto.seek(0)
#print(archivo_texto.read())

#print(archivo_texto.readline())

#print(archivo_texto.readlines())

for lineas in archivo_texto.readlines():
    print(lineas.rstrip())

archivo_texto.close()
