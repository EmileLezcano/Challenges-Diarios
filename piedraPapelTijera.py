import random # libreria para la eleccion aleatoria

def juego_humano():
    eleccion = input("¿Qué eliges, piedra, papel o tijeras?: ").lower() #lower() para validar las mayusculas y minusculas
    while eleccion not in ['piedra', 'papel', 'tijeras']:
        print("Error: Elige nuevamente.")
        eleccion = input("¿Piedra, papel o tijeras?: ").lower()
    return eleccion

def juego_maquina():
    elecciones = ['piedra', 'papel', 'tijeras']
    return random.choice(elecciones)

def determinar_ganador(humano, maquina):
    if humano == maquina:
        return "¡EMPATE!"
    elif (humano == 'piedra' and maquina == 'tijeras') or \
         (humano == 'papel' and maquina == 'piedra') or \
         (humano == 'tijeras' and maquina == 'papel'):
        return "¡GANASTE! ╰(*°▽°*)╯"
    else:
        return "¡PERDISTE! (┬┬﹏┬┬)"

def jugar():
    while True:
        humano = juego_humano()
        maquina = juego_maquina()

        print(f"Tu elección: {humano}")
        print(f"Elección de la máquina: {maquina}")

        resultado = determinar_ganador(humano, maquina)
        print(resultado)

        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            print("¡Gracias por jugar! Hasta la próxima.")
            break

# Iniciar el juego
jugar()
