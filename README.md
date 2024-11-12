# Hundir la Flota

Este repositorio contiene el código para el proyecto **Hundir la Flota**, un juego de Python modularizado en varios archivos para separar funciones, variables y el flujo principal del programa.

## Estructura del Proyecto

- `main.py`: El archivo principal donde se ejecuta el juego. Este archivo organiza y controla el flujo de la partida, utilizando funciones y variables definidas en otros módulos.
- `funciones.py`: Contiene todas las funciones necesarias para el juego. Aquí se definen la lógica y algoritmos del juego, que son llamados desde `main.py`.
- `variables.py`: Define variables globales y constantes utilizadas en el juego, permitiendo configurar valores iniciales de forma centralizada.

## Instrucciones de Uso

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/hundir-la-flota.git

2- Navega al directorio del proyecto:

cd tu_repositorio

3-Ejecuta el archivo principal:
python main.py

Descripción de Archivos
main.py
Este archivo inicia el programa y maneja el flujo principal. Importa funciones desde funciones.py y variables desde variables.py, lo que permite mantener un código limpio y organizado.

funciones.py
Aquí se definen las funciones utilizadas en main.py. Cada función tiene una descripción de su propósito y parámetros en los comentarios para facilitar su reutilización y mantenimiento.

variables.py
Contiene las variables globales y constantes necesarias para la ejecución del programa. Al tener un archivo de configuración centralizado, es fácil modificar valores sin afectar el código principal.

Contribución
Si deseas contribuir, por favor sigue estos pasos:

Haz un fork del proyecto.
Crea una nueva rama para tus cambios.
Realiza un pull request una vez que hayas terminado tus modificaciones.
