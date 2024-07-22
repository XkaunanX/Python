import datetime

#CREO UN REGISTRO PACIENTE
def CrearPaciente():
    #ID, NOMBRE, TIPO CONSULTA, EDAD, ESTADO DE URGENCIA, FECHA DE INGRESO
    pac = [0, "", "", "", "", datetime.time(), datetime.time()]
    return pac

#RECIBO UN TIPO PACIENTE Y ASIGNO VALORES EN SUS CAMPOS DEPENDIENDO DE LOS PARAMETROS
def CargarPaciente(pac, ID,Nombre, Consulta, Edad, Urgencia, Fecha, Hora):
    pac[0] = ID
    pac[1] = Nombre
    pac[2] = Consulta
    pac[3] = Edad
    pac[4] = Urgencia
    pac[5] = Fecha
    pac[6] = Hora
    
#SECCION VER CAMPOS (ALERT: TODOS SON NECESARIOS)
def VerID(pac):
    return pac[0]

def VerNombre(pac):
    return pac[1]

def VerTipoDeConsulta(pac):
    return pac[2]

def VerEdad(pac):
    return pac[3]

def VerEstadoDeUrgencia(pac):
    return pac[4]

def VerFechaDeIngreso(pac):
    return pac[5]

def VerHorarioDeIngreso(pac):
    return pac[6]

#RECIBO UN PACIENTE Y GENERO UNA COPIA EN EL PARAMETRO
def CopiarPaciente(original, copia):
    original[0] = copia[0]
    original[1] = copia[1]
    original[2] = copia[2]
    original[3] = copia[3]
    original[4] = copia[4]
    original[5] = copia[5]
    original[6] = copia[6]
    
#SECCION MODIFICAR (ALERT: TODOS SON NECESARIOS)
def ModificarID(pac, ID):
    pac[0] = ID

def ModificarNombre(pac, Nombre):
    pac[1] = Nombre
    
def ModificarTipoDeConsulta(pac, Consulta):
    pac[2] = Consulta
    
def ModificarEdad(pac, Edad):
    pac[3] = Edad
    
def ModificarTipoUrgencia(pac, Urgencia):
    pac[4] = Urgencia
 
def ModificarFechaIngreso(pac, Fecha):
    pac[5] = Fecha
    
def ModificarHorarioIngreso(pac, Hora):
    pac[6] = Hora