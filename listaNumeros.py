#Lista vacia
lista = []

#Instrucciones
print('Ingrese numeros para la lista. Cuando termine escriba FIN para salir' )

while True:
  
  elemento = input('Ingrese los numeros que desea ordenar: ') 

  if elemento.lower() == 'fin': #.lower() es para validar la palabra fin tanto en mayusculas como en minusculas
    break
  
  try:
    numero = float(elemento) #pasar de cadena a entero
    lista.append(numero) #agregar el numero a la lista
  except ValueError:
    print('Error: ingrese un numero o escriba FIN para terminar')

#Mostrar enteros sin decimales
numerosEnteros = [int(num) if num.is_integer() else num for num in lista] 

#Ordenar lista
numerosEnteros.sort()

#lista ordenada
print('Lista ordenada de forma ascendente: ',numerosEnteros)







