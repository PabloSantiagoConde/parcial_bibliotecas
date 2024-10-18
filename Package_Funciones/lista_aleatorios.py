import random

'''
DATOS IMPORTANTES: 

largo: 50
cant: 0 - 100

EJECUCIÓN: 
    1) crear variable lista e inicializarla (listo)
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    2) cargarle los elementos (Se requiere RECORRIDO -> bucle for )
        3)cada elemento tiene que ser un número aleatorio
    4) devolverme esa lista

'''

def lista_aleatorios():
    
    lista = [0] * 50

    for i in range(len(lista)):
        lista[i] = random.randint(1, 100)

    return lista
