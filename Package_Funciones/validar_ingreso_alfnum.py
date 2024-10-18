
'''
VALIDAR: 

                        Ver si hay error
-> si no hay                                    ->si hay
    no pasa nada                                    modificarlo

'''
## TRUE elemento = alpha, elemento = num, elemento = alnumeric 
def validar_ingreso_alfnum(elemento):
    return tiene_numero(elemento) and tiene_string(elemento)

def tiene_numero(elemento):
    flag = False
    for i in range(len(elemento)):
        if elemento[i].isnumeric():
            flag = True
    return flag

def tiene_string(elemento):
    flag = False
    for i in range(len(elemento)):
        if elemento[i].isalpha():
            flag = True
    return flag

