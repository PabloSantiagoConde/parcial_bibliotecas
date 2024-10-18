from Package_Input import *
from Package_Arrays import lista_string
import random

def inicializar_matriz(filas,columnas,valor_inicial):
    matriz = []
    for i in range(filas):
        fila = [valor_inicial] * columnas

        matriz += [fila] 

    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
            print(fila) 
    print()

def cargar_libros_aleatorios(matriz):
    legajo = ""
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            
            legajo = lista_string(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",k=5))
            
            matriz[i][j] = legajo

    return matriz