# Word Frequency Counter

## Descripción

- Proyecto desarrollado como prueba de código para Cart.com
- Este proyecto en Python cuenta la frecuencia de palabras en un archivo de texto. 
- Las palabras se consideran de manera insensible a mayúsculas y minúsculas
- Se ignora la puntuación y se ordenan las palabras por su frecuencia en orden descendente. 
- El código está estructurado en una clase y se incluye un conjunto de pruebas automatizadas.

## Estructura del Proyecto

- `src/word_frequency.py`: Archivo principal que contiene la clase `WordFrequencyCounter`.
- `tests/test_word_frequency.py`: Archivo de pruebas con `unittest` y `Faker` para probar distintos casos de uso.

## Requisitos

- Python 3.8 o superior
- Paquetes adicionales: 
  - `faker` (para generar textos aleatorios en las pruebas)
  - `unittest` (librería estándar de Python para pruebas)

### Configuración del Entorno Virtual
- Puedes crear un entorno virtual y activar el entorno usando los siguientes comandos (Linux):

    ```bash
    $ python3 -m venv env
    $ source env/bin/activate
    $ pip install -r requirements.txt

## Uso del programa
- Coloca el archivo de texto que quieres analizar en el directorio raíz del proyecto o en cualquier otra ubicación.
- Ejecuta el programa desde la línea de comandos, proporcionando la ruta al archivo de texto como argumento.
- Ejemplo:

    - Input
    $ python src/word_frequency.py src/sample.txt

    - Output
    test: 3
    a: 2
    is: 2
    this: 2
    only: 1

- Para ejecutar el script que genera palabras y párrafos de texto aleatorios, utiliza el siguiente comando en la terminal:

    ```bash
    $ python src/faker_util.py

## Pruebas
- Para ejecutar todas las pruebas, navega al directorio raíz del proyecto y usa el siguiente comando:
    $ python -m unittest discover tests