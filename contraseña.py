import random #para generar números aleatorios
import string #para acceder a conjuntos predefinidos de caracteres.

# función que toma como argumento la longitud deseada de la contraseña
def generar_contrasena(longitud):
    # Definir los caracteres posibles
    mayusculas = string.ascii_uppercase #módulo string para obtener los diferentes tipos de caracteres
    minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation

    # Asegurar que la contraseña tenga al menos un caracter de cada tipo
    contrasena = [
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    # Llenar el resto de la contraseña
    for _ in range(longitud - 4):
        contrasena.append(random.choice(mayusculas + minusculas + numeros + simbolos))

    # Mezclar la contraseña
    random.shuffle(contrasena)

    # Convertir la lista de caracteres en una cadena
    return ''.join(contrasena)

# Generar una contraseña de longitud aleatoria entre 8 y 16 caracteres
longitud = random.randint(8, 16)
contrasena_segura = generar_contrasena(longitud)

print(f"Contraseña segura de {longitud} caracteres: {contrasena_segura}")