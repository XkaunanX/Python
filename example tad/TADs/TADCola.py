#CREO MI REPRESENTACION INTERNA DE UNA COLA
def CrearCola():
    Cola = []
    return Cola

#DEVUELVE BOOLEANO DEPENDIENDO DE SI TIENE ELEMENTOS
def IsEmpty(Cola):
    return len(Cola)==0

#ENCOLAR
def Queue(Cola, Elemento):
    Cola.append(Elemento)

#DESENCOLAR    
def EnQueue(Cola):
    Elemento = Cola[0]
    del Cola[0]
    return Elemento

#DEVUELVE EL TAMAÑO DE LA COLA
def Tamano(Cola):
    return len(Cola)

#COPIAR COLA
def CopiarCola(Cola, Nuevacola):
    ColaAux = CrearCola()
    for i in range(Tamano(Cola)):
        Elemento = EnQueue(Cola)
        Queue(ColaAux, Elemento)
        Queue(Nuevacola, Elemento)
    for i in range(Tamano(ColaAux)):
        Elemento = EnQueue(ColaAux)
        Queue(Cola, Elemento)