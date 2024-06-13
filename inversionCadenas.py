cadena = input('Ingrese la cadena a invertir:')
candena_invertida = '' # Variable donde se va almacenar la nueva cadena invertida

#Este ciclo itera sobre cada caracter en la cadena original
for caracter in cadena:
    #En cada iteracion, el caracter actual se agrega al principio de 'cadena_invertida'
    candena_invertida = caracter + candena_invertida

print('La cadena invertida es:',candena_invertida)

