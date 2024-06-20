# Listas con las claves y los valores
claves = ['arriba','abajo','izquierda','derecha']
valores = [(-1,0),(1,0),(0,-1),(0,1)]

# Se inicializa el diccionario vacio
diccionario = {}

# Bucle for para recorrer ambas listas
for clave, valor in zip(claves, valores): #zip() para emparejar los elementos de las dos listas
    diccionario[clave] = valor

#Imprimir diccionario
print(diccionario)