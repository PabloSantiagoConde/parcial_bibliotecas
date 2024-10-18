import random
from Package_Matrix import inicializar_matriz,cargar_libros_aleatorios
'''2.   Generar una matriz de caracteres alfanuméricos: Desarrollar una función que genere de manera aleatoria una matriz de 6 filas por 15 columnas (6 listas de 15 elementos cada una), compuesta de caracteres alfanuméricos (letras y dígitos).
'''

def biblioteca():
    
    biblio = inicializar_matriz(6,15,"")
    cargar_libros_aleatorios(biblio)

    return biblio




