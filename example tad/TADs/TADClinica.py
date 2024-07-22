#CREO UNA LISTA DE ESPERA QUE CONTIENE {Paciente 1, Paciente 2, ..., Paciente n}
def CrearlistaDeEspera():
    ListaDeEspera = []
    return ListaDeEspera

#DAR DE ALTA A UN PACIENTE
def AgregarPaciente(ListaDeEspera, paciente):
    ListaDeEspera.append(paciente)

#DAR DE BAJA A UN ESTUDIANTE
def EliminarPaciente(ListaDeEspera, paciente):
    ListaDeEspera.remove(paciente)
 
#OBTENER TAMAÑO DEL CURSO
def Tamano(ListaDeEspera):
    return len(ListaDeEspera)

#DEVOLVER EL I-ESIMO PACIENTE
def RecuperarPaciente(ListaDeEspera, i):
    return ListaDeEspera[i-1]

#DEVUELVE BOOLEANO SI ESTA VACIA O NO
def ExisteListaDeEspera(ListaDeEspera):
    return len(ListaDeEspera)==0

