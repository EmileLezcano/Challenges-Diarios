texto = input('Ingresa la frase: ')
vocales = "aeiouAEIOU" # vocales en minusculas y mayusculas 

contador = 0

for i in texto: # recorre cada uno de los caracteres del texto ingresado
    if i in vocales: # evalua si los caracteres ingresados se encuentran en la variable vocales
        contador = contador +1

print(f"La frase tiene {contador} vocales")