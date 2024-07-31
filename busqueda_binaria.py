
# Paso 3 Creamos una función y le pasamos los datos de la lista y el objetivo
def busquedaBinaria(lista,objetivo):
    # Creamos variables que representen la posición de los índices en los extremos.
    min = 0
    max = len(lista) -1

    while min <= max:
        # Calculamos el promedio de los extremos que se repetirá a lo largo del ciclo.
        suma = min + max 
        adivina = round(suma/2)
        # Creamos condicionales que devolverán la posición del elemento o darán nuevos valores a min y max para continuar con la búsqueda.
        if lista[adivina] == objetivo:
            return adivina
        elif lista[adivina] < objetivo:
            min = adivina + 1
        else:
            max = adivina - 1

    return -1 # Devolverá -1 en caso de que el objetivo no se encuentre en la lista.

# Paso 1 Creamos una lista de elementos cargada de números enteros.
lista = [2,3,3,5,7,10]

# Paso 2 Pedimos al usuario que ingrese el número que quiere buscar en la lista y validamos que no ingrese números negativos o caracteres.
while True:
    try:
        objetivo = int(input('Ingrese un número: '))
        if objetivo >= 0:
            break 
        else:
            print('Error: Deben ser números positivos')
            
    except ValueError:
        print('Error: Deben ser números ')

# Paso 4 Almacenamos los resultados de la función en una variable.
resultado = busquedaBinaria(lista,objetivo)

# Paso 5 Imprimimos la posición del objetivo en la lista o Imprimimos un mensaje indicando que el objetivo no se encuentra en la lista
# dependiendo de los resultados. 
if resultado != -1:
    print(f"El número {objetivo} se encuentra en la posición {resultado} de la lista")
else:
    print('El número no existe en la lista')
