# Funcion para convertir de Celsius a Fahrenheit
def Cel_a_Fah(celsius):
    return(celsius*9/5) + 32 # Formula para la conversion

#Introducir temperatura en celsius
celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Convetir la temperatura a grados Fahrenheit
fahre = Cel_a_Fah(celsius)

# Imprimir resultado
print(f"{celsius} grados Celsius equivalen a {fahre} grados Fahrenheit.")
