'''
3.  Ordenar una lista de números enteros: Desarrollar una función que ordene una lista de números enteros, recibiendo como parámetro el criterio de ordenamiento "ASC" o "DESC" (ascendente o descendente).

aclaración: Está hecha con bubble sort
'''

def ordenar_vector(lista,orientacion = "ASC"):

    if orientacion == "ASC":
        for i in range(len(lista)):
            for x in range(0, len(lista) - i - 1):
                if lista[x] > lista[x + 1]:
                    temp = lista[x]
                    lista[x] = lista[x + 1]
                    lista[x + 1] = temp
        return lista
    elif orientacion == "DESC":
        for i in range(len(lista)):
            for x in range(0, len(lista) - i - 1):
                if lista[x] < lista[x + 1]:
                    temp = lista[x]
                    lista[x] = lista[x + 1]
                    lista[x + 1] = temp
    return lista

