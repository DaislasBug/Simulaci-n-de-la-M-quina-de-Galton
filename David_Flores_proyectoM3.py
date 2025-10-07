# NOMBRE_APELLIDO_proyectoM3.py

import numpy as np
import matplotlib.pyplot as plt


NUM_CANICAS = 3000  
NUM_NIVELES = 12     

# -----------------------------------------------------------------------------
# FUNCIÓN 1: Simulación de la Máquina de Galton
# -----------------------------------------------------------------------------
def simular_galton(num_canicas, num_niveles):
    """
    Simula la caída de canicas en la Máquina de Galton.

    El número final del contenedor es igual al número de veces que la canica
    se desvió a la derecha (equivalente a un 'éxito' en una distribución binomial).
    El número de contenedores será 'num_niveles + 1', y los índices irán de 0 a 'num_niveles'.

    Parámetros:
    - num_canicas (int): Cantidad de canicas a simular.
    - num_niveles (int): Cantidad de niveles de obstáculos (número de pasos aleatorios).

    Retorna:
    - resultados (numpy.ndarray): Un array con la posición final (índice del contenedor)
                                  de cada canica.
    """
    print(f"Iniciando simulación de {num_canicas} canicas con {num_niveles} niveles...")

    # Simular los 'num_niveles' rebotes para cada canica.
    # np.random.randint(0, 2, size=(num_canicas, num_niveles)) genera una matriz
    # donde cada elemento es 0 (izquierda) o 1 (derecha) con 50% de probabilidad.
    # 'size' crea una matriz de 'num_canicas' filas (una por canica) y 'num_niveles' columnas (una por rebote).
    movimientos = np.random.randint(0, 2, size=(num_canicas, num_niveles))

    # La posición final del contenedor es la suma de los movimientos a la derecha (los '1').
    # Si la canica cae 12 veces, y 5 veces va a la derecha (1), y 7 veces a la izquierda (0),
    # el resultado será 5. Este es el índice del contenedor final (empezando desde 0).
    resultados = np.sum(movimientos, axis=1)

    print("Simulación finalizada.")
    return resultados

# -----------------------------------------------------------------------------
# FUNCIÓN 2: Graficación de Resultados
# -----------------------------------------------------------------------------
def graficar_resultados(resultados, num_niveles):
    """
    Genera un histograma a partir de los resultados de la simulación.

    Parámetros:
    - resultados (numpy.ndarray): Array con la posición final de cada canica.
    - num_niveles (int): Cantidad de niveles, usado para definir los límites de los contenedores.
    """
    print("Generando histograma...")

    # Determinar el número de contenedores. Para 'N' niveles, hay 'N+1' contenedores.
    # Los valores de los contenedores van de 0 a 'num_niveles'.
    num_contenedores = num_niveles + 1
    # Definir los bordes (bins) para el histograma, para que cada contenedor
    # (0, 1, 2, ..., 12) tenga su propia barra centrada correctamente.
    bins = np.arange(num_contenedores + 1) - 0.5

    # Crear el gráfico de histograma
    plt.figure(figsize=(10, 6))
    
    # Graficar el histograma. 'bins' asegura que cada entero (0-12) tenga una barra.
    # 'rwidth=0.9' agrega un pequeño espacio entre las barras para claridad.
    plt.hist(resultados, bins=bins, rwidth=0.9)

    # Establecer título y etiquetas de ejes
    plt.title('Simulación de la Máquina de Galton', fontsize=16) # Título
    plt.xlabel('Distribución de canicas (Contenedor Final - 0 a 12)', fontsize=12) # Nombre del eje X
    plt.ylabel('Cantidad de canicas test', fontsize=12) # Nombre del eje Y

    # Ajustar los límites del eje X para que se vea similar al ejemplo
    #plt.xlim(-0.5, num_niveles + 0.5)


    # Imprimir el histograma
    plt.show()
    print("Histograma mostrado.")

# EJECUCIÓN DEL PROGRAMA PRINCIPAL
if __name__ == "__main__":
    # Calcular los resultados de la simulación
    posiciones_finales = simular_galton(NUM_CANICAS, NUM_NIVELES)

    #  Graficar el histograma
    graficar_resultados(posiciones_finales, NUM_NIVELES)
