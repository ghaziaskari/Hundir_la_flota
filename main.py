import time
import os
from funciones import generar_coordenada_aleatoria, disparar, inicializar_tablero, inicializar_barcos, mostrar_tablero_visible, mostrar_tablero

def main():
    # Limpiar la pantalla
    os.system('cls')

    # Bienvenida
    print("Bienvenido al juego de Hundir la Flota")
    print("Tienes que hundir todos los barcos para ganar.")
    time.sleep(2)

    # Inicializar tableros
    jugador = inicializar_tablero("Jugador")
    maquina = inicializar_tablero("Máquina")

    # Mantener un seguimiento de las coordenadas disparadas
    disparos_realizados_jugador = set()
    disparos_realizados_maquina = set()

    # Simular juego
    turno_jugador = True

    while jugador['barcos_restantes'] > 0 and maquina['barcos_restantes'] > 0:
        # os.system('cls')
        if turno_jugador:
            print("\nTú:")
            mostrar_tablero_visible(maquina)
            print("\nMáquina:")
            mostrar_tablero_visible(jugador)
            while True:
                fila_input = input("Introduce fila (1-10): ")
                columna_input = input("Introduce columna (1-10): ")
                if fila_input.isdigit() and columna_input.isdigit():
                    fila = int(fila_input) - 1
                    columna = int(columna_input) - 1
                    if 0 <= fila <= 9 and 0 <= columna <= 9:
                        if (fila, columna) not in disparos_realizados_jugador:#no repita disparos en las mismas coordenadas
                            disparos_realizados_jugador.add((fila, columna))
                            break
                        else:
                            print("Ya has disparado a esa coordenada. Inténtalo de nuevo.")
                    else:
                        print("Por favor, introduce números entre 1 y 10.")
                else:
                    print("Entrada inválida. Introduce números entre 1 y 10.")

            éxito = disparar(maquina, fila, columna)
            if éxito:
                print("¡tuviste éxito! Vuelve a disparar.")
            else:
                print("Fallaste. Le toca a la máquina.")
                turno_jugador = False
        else:
            print("\nTurno de la máquina:")
            time.sleep(1)
            while True:
                fila, columna = generar_coordenada_aleatoria()
                if (fila, columna) not in disparos_realizados_maquina: #no repita disparos en las mismas coordenadas 
                    disparos_realizados_maquina.add((fila, columna))
                    break
            éxito = disparar(jugador, fila, columna)
            print(f"La máquina disparó a ({fila + 1}, {columna + 1}).")
            if éxito:
                print("¡La máquina tuvo éxito! Vuelve a disparar.")
            else:
                print("La máquina falló. Te toca a ti.")
                turno_jugador = True
            time.sleep(2)

    if jugador['barcos_restantes'] == 0:
        print("\n¡La máquina ha ganado!")
        mostrar_tablero_visible(maquina)
    else:
        print("\n¡Felicidades! Has ganado!")
        mostrar_tablero_visible(maquina)

if __name__ == "__main__":
    main()