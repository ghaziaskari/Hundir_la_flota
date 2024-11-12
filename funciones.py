import random
from variables import FILAS, COLUMNAS, AGUA, BARCO,IMPACTO, FALLO, BARCOS

# imprimir el tablero
def print_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

# Crea un tablero vacío usando una comprensión de lista
def crear_tablero_vacio():
    return [[AGUA for _ in range(COLUMNAS)] for _ in range(FILAS)]

# Genera una coordenada aleatoria en el tablero
def generar_coordenada_aleatoria():
   fila = random.randint(0, FILAS - 1)
   columna = random.randint(0, COLUMNAS - 1)
   return fila, columna

# Intenta ubicar un barco en random position, verificando si cabe y no se ponga con otros barcos
def colocar_barco(tablero, eslora):
    orientacion = random.choice(['H', 'V'])
    while True:
        fila, columna = generar_coordenada_aleatoria()
        if orientacion == 'H' and columna + eslora <= COLUMNAS and all(tablero[fila][columna + i] == AGUA for i in range(eslora)):
            for i in range(eslora):
                tablero[fila][columna + i] = BARCO
            break
        elif orientacion == 'V' and fila + eslora <= FILAS and all(tablero[fila + i][columna] == AGUA for i in range(eslora)):
            for i in range(eslora):
                tablero[fila + i][columna] = BARCO
            break

# Disparar a una coordenada
def disparar(tablero_data, fila, columna):
    if tablero_data['tablero'][fila][columna] == BARCO:
       tablero_data['tablero'][fila][columna] = IMPACTO
       tablero_data['tablero_visible'][fila][columna] = IMPACTO
       tablero_data['barcos_restantes'] -= 1
       return True
    else:
        tablero_data['tablero_visible'][fila][columna] = FALLO
        return False

# Inicializar los tableros y barcos restantes
def inicializar_tablero(id_jugador):
    tablero = crear_tablero_vacio()
    tablero_visible = crear_tablero_vacio()
    barcos_restantes = sum(BARCOS.values())
    tablero_data = {
        'id_jugador': id_jugador,
        'tablero': tablero,
        'tablero_visible': tablero_visible,
        'barcos_restantes': barcos_restantes
    }

    inicializar_barcos(tablero_data)
    
    # Copiar barcos al tablero visible del jugador
    if id_jugador == "Jugador":
        for i in range(FILAS):
            for j in range(COLUMNAS):
                if tablero[i][j] == BARCO:
                    tablero_visible[i][j] = BARCO
    return tablero_data

# Colocar los barcos en el tablero
def inicializar_barcos(tablero_data):
    for eslora in BARCOS.values ():
        colocar_barco(tablero_data['tablero'], eslora)
    
# Mostrar tablero visible
def mostrar_tablero_visible (tablero_data):
      print_tablero(tablero_data['tablero_visible'])
      
# Mostrar tablero completo
def mostrar_tablero (tablero_data):
      print_tablero(tablero_data['tablero'])