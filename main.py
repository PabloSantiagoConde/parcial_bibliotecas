from Package_Funciones import *
from Package_Matrix import *
from Package_Input import *
from Package_Arrays import validar_lista , lista_string , rango ,valor_max,valor_min,validar_lista_existente

## yo quiero una/muchas funciones de tal carpeta 
##El from te dice de donde "from Package_Input"
## import significa que funciones queres 
## * significa todas         ## from Package_Funciones import biblioteca

def biblioteca_conde():
    lista = []                                      ##Necesario para 2) 3)
    
    while True:
        opcion = get_int("Bienvenido a la biblioteca conde. Seleccione la opción que solicita. \n 1.Generar lista de numeros aleatorios \n 2.Ordenar la lista previamente creada \n 3.Buscar por rango \n 4.Ver el máximo y minimo de los numeros del rango solicitado \n 5.Generar la matriz biblioteca \n 6.Salir \n Ingrese su opción 1-6:","Error, opcion inexistente",1,6,50)

        match opcion:
            case 1:                                 ##Necesario para 2) 3)
                lista = lista_aleatorios()
                print(f" \n La lista de numero aleatorios es: {lista} \n ") 
            case 2:
                if validar_lista_existente(lista):
                    orientacion = get_str("Ingrese la orientación de la lista 'ASC' para Ascendente o 'DESC' para Descendente: ","Error, opcion inexistente",4).upper()
                    print(f" \n La lista de numeros ordenados es: {ordenar_vector(lista,orientacion)} \n")
            case 3:
                if validar_lista_existente(lista):    
                    cota_inf = get_int("\n Ingrese el valor de la cota inferior 1-100: \n","\n Error, el valor tiene que esta entre 1 y 100 \n",1,100,50)
                    cota_sup = get_int("\n Ingrese el valor de la cota superior 1-100: \n","\n Error, el valor tiene que esta entre 1 y 100 \n",1,100,50)
                    print(f"\n Los valores dentro del rango solicitado son: {rango(cota_inf,cota_sup,lista)} \n")
            case 4:
                if validar_lista_existente(lista):
                    print(f"El valor máximo es {valor_max(rango(cota_inf,cota_sup,lista))} y el valor minimo es {valor_min(rango(cota_inf,cota_sup,lista))}")
            case 5:
                imprimir_matriz(biblioteca())
            case 6:
                break

biblioteca_conde()