numero = int(input('Ingresa un numero para crear la tabla de multiplicar: '))

contador = 1 #se inicializa el contador en 1

while contador <= 10: #se ejecuta el ciclo hasta que el contador llegue a 10
    resultado = numero*contador # se crea la variable resultado con la operacion correspondiente
    print(f"{numero} x {contador} = ",resultado) #se imprime cada resultado hasta llegar a 10
    contador = contador + 1 
