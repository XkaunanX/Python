#TODO: Validar que me ingrese un estado de urgencia
#ID invalido (no lo encontro o el caracter es invalido)
#Sacar en intervalo horario la barrita de estado de urgencia

#LIBRERIA EXPRESIONES REGULARES
import re

#LIBRERIAS TIPO DE DATO
import datetime

#TADs
from TADs import TADPaciente
from TADs import TADClinica
from TADs import TADCola

#LIBRERIAS PARA INTERFAZ
import tkinter
from tkinter import messagebox
import customtkinter
from tkcalendar import Calendar

#SETEO LA APARIENCIA DE LA INTERFAZ
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

#INICIALIZAR LISTA DE ESPERA PRINCIPAL
ListaDeEspera = TADClinica.CrearlistaDeEspera()

#INICIALIZAR LISTA DE ESPERA SEGUN FECHA Y HORARIO
ListaDeEsperaSegunFechaHorario = TADClinica.CrearlistaDeEspera()

#CREO Y INICIALIZO LA APLICACION
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #INICIALIZAR IDs
        self.IDs = 0
    
        #INICIALIZAR LISTADO DE ERRORES
        self.ERRORES = []
    
        #CONFIGURO LA VENTANA
        self.title("Sistema Clinica")
        self.geometry(f"{1100}x{580}")
        self.resizable(width = False, height= False)

        #CONFIGURAR EL GRID DEL LAYOUT
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0,weight=1)
        
        #TABVIEW | SELF 
        self.tabview = customtkinter.CTkTabview(self, command= lambda: self.COMMAND_ListarPacientes())#lambda event: self.COMMAND_ListarPacientes()
        self.tabview.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.tabview.add("Recepcion")
        self.tabview.add("Listado Pacientes")
        self.tabview.add("Prioridad segun Edad")
        self.tabview.add("Eliminar segun Consulta")
        self.tabview.add("Alta prioridad")
        self.tabview.add("Intervalo horario")
        
        #TAB (RECEPCION) | TABVIEW 
        self.tabview.tab("Recepcion").grid_columnconfigure(4, weight=0)
        self.tabview.tab("Recepcion").grid_rowconfigure(10, weight=1)
        
        #INGRESAR
        #--------------------------
        self.lbl_ing = customtkinter.CTkLabel(self.tabview.tab("Recepcion"),font=customtkinter.CTkFont(size=20) ,text= "Nuevo paciente", height=40, width=300)
        self.lbl_ing.grid(row=0, column=0, sticky="nsew", pady=(20,0), padx=(15,0))
        
        self.lbl_espacio = customtkinter.CTkLabel(self.tabview.tab("Recepcion"),font=customtkinter.CTkFont(size=10, weight="bold") ,text= "______________________________________________________________", height=40, width=300)
        self.lbl_espacio.grid(row=1, column=0, sticky="nsew", pady=(5,0), padx=(15,0))
           
        self.lbl_nom_ing = customtkinter.CTkLabel(self.tabview.tab("Recepcion"),font=customtkinter.CTkFont(size=13) ,text= "Nombre", height=40)
        self.lbl_nom_ing.grid(row=2, column=0, sticky="nsew", pady=(0,0), padx=(15,0))
        self.txtbox_nom_ing = customtkinter.CTkTextbox(self.tabview.tab("Recepcion"),font=customtkinter.CTkFont(size=18),height=40,)
        self.txtbox_nom_ing.grid(row=3, column=0, sticky="nsew", pady=(3,0), padx=(15,0))
        
        self.lbl_tipcon = customtkinter.CTkLabel(self.tabview.tab("Recepcion"),font=customtkinter.CTkFont(size=13) ,text="Tipo de consulta", height=40)
        self.lbl_tipcon.grid(row=4, column=0, sticky="nsew", pady=(0,0), padx=(15,0))
        self.txtbox_tipcon_ing = customtkinter.CTkTextbox(self.tabview.tab("Recepcion"),font=customtkinter.CTkFont(size=18),height=40)
        self.txtbox_tipcon_ing.grid(row=5, column=0, sticky="nsew", pady=(3,0), padx=(15,0))
        
        self.lbl_eda = customtkinter.CTkLabel(self.tabview.tab("Recepcion"),font=customtkinter.CTkFont(size=13) ,text= "Edad", height=40)
        self.lbl_eda.grid(row=6, column=0, sticky="nsew", pady=(0,0), padx=(15,0))
        self.txtbox_eda_ing = customtkinter.CTkTextbox(self.tabview.tab("Recepcion"),font=customtkinter.CTkFont(size=18),height=40)
        self.txtbox_eda_ing.grid(row=7, column=0, sticky="nsew", pady=(3,0), padx=(15,0))
        
        self.combox_esturg_ing = customtkinter.CTkComboBox(self.tabview.tab("Recepcion"),values=["baja", "media", "alta"],height=40)
        self.combox_esturg_ing.grid(row=8, column=0, sticky="nsew", pady=(20,0), padx=(15,0))
        self.combox_esturg_ing.set("Estado de urgencia")
        
        self.btn_AGREGARPACIENTE = customtkinter.CTkButton(self.tabview.tab("Recepcion"),height=40,text="Agregar", command= lambda: self.COMMAND_AgregarPaciente())
        self.btn_AGREGARPACIENTE.grid(row=9, column=0, pady=(20,0))
        #-------------------------- 
        
        #MODIFICAR
        #--------------------------
        self.lbl_mod = customtkinter.CTkLabel(self.tabview.tab("Recepcion"),font=customtkinter.CTkFont(size=20) ,text= "Modificar Urgencia", height=40, width=300)
        self.lbl_mod.grid(row=0, column=1, sticky="nsew", pady=(20,0))
        
        self.lbl_espacio = customtkinter.CTkLabel(self.tabview.tab("Recepcion"),font=customtkinter.CTkFont(size=10, weight="bold") ,text= "______________________________________________________________", height=40, width=300)
        self.lbl_espacio.grid(row=1, column=1, sticky="nsew", pady=(5,0))
        
        self.lbl_ID_mod = customtkinter.CTkLabel(self.tabview.tab("Recepcion"),font=customtkinter.CTkFont(size=13) ,text= "ID", height=40, width=300)
        self.lbl_ID_mod.grid(row=2, column=1, sticky="nsew", pady=(3,0), padx=(15,0))
        
        self.txtbox_ID_mod = customtkinter.CTkTextbox(self.tabview.tab("Recepcion"),font=customtkinter.CTkFont(size=18),height=40)
        self.txtbox_ID_mod.grid(row=3, column=1, sticky="nsew", pady=(3,0), padx=(15,0))
        
        self.lbl_combox_esturg_mod = customtkinter.CTkLabel(self.tabview.tab("Recepcion"),font=customtkinter.CTkFont(size=13) ,text= "Cambiar Estado De Emergencia", height=40, width=300)
        self.lbl_combox_esturg_mod.grid(row=4, column=1, sticky="nsew", pady=(3,0), padx=(15,0))
        
        self.combox_esturg_mod = customtkinter.CTkComboBox(self.tabview.tab("Recepcion"),values=["baja", "media", "alta"],height=40)
        self.combox_esturg_mod.grid(row=5, column=1, sticky="nsew", pady=(3,0), padx=(15,0))
           
        self.btn_MODIFICARESTADOURGENCIA = customtkinter.CTkButton(self.tabview.tab("Recepcion"),height=40,text="Modificar", command= lambda: self.COMMAND_ModificarUrgenciaPorID())
        self.btn_MODIFICARESTADOURGENCIA.grid(row=7, column=1)
        #--------------------------
        
        #ELIMINAR
        #--------------------------
        self.lbl_eli = customtkinter.CTkLabel(self.tabview.tab("Recepcion"),font=customtkinter.CTkFont(size=20) ,text= "Eliminar de la Lista", height=40, width=300)
        self.lbl_eli.grid(row=0, column=2, sticky="nsew", pady=(20,0), padx=(15,0))
        
        self.lbl_espacio = customtkinter.CTkLabel(self.tabview.tab("Recepcion"),font=customtkinter.CTkFont(size=10, weight="bold") ,text= "______________________________________________________________", height=40, width=300)
        self.lbl_espacio.grid(row=1, column=2, sticky="nsew", pady=(5,0), padx=(15,0))
        
        self.lbl_ID_eli = customtkinter.CTkLabel(self.tabview.tab("Recepcion"),font=customtkinter.CTkFont(size=13) ,text= "ID", height=40, width=300)
        self.lbl_ID_eli.grid(row=2, column=2, sticky="nsew", pady=(3,0), padx=(15,0))
        
        self.txtbox_ID_eli = customtkinter.CTkTextbox(self.tabview.tab("Recepcion"),font=customtkinter.CTkFont(size=18),height=40)
        self.txtbox_ID_eli.grid(row=3, column=2, sticky="nsew", pady=(3,0), padx=(15,0))
        
        self.btn_ELIMINARPACIENTE = customtkinter.CTkButton(self.tabview.tab("Recepcion"),height=40,text="Eliminar", command= lambda: self.COMMAND_EliminarSegunElID())
        self.btn_ELIMINARPACIENTE.grid(row=5, column=2)
        #--------------------------
        
        #TAB (LISTADO PACIENTES) | TABVIEW
        self.tabview.tab("Listado Pacientes").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Listado Pacientes").grid_rowconfigure(2, weight=1)
        
        #LISTAR PACIENTES
        #-------------------------
        self.lbl_pacientes = customtkinter.CTkLabel(self.tabview.tab("Listado Pacientes"),font=customtkinter.CTkFont(size=20) ,text= "Listados De Pacientes", height=40, width=300)
        self.lbl_pacientes .grid(row=0, column=0, sticky="nsew", pady=(20,0), padx=(15,0))
        
        self.lbl_espacio = customtkinter.CTkLabel(self.tabview.tab("Listado Pacientes"),font=customtkinter.CTkFont(size=10, weight="bold") ,text= "______________________________________________________________", height=40, width=300)
        self.lbl_espacio.grid(row=1, column=0, sticky="nsew", pady=(5,0), padx=(15,0))
        
        self.txtbox_listado = customtkinter.CTkTextbox(self.tabview.tab("Listado Pacientes"),font=customtkinter.CTkFont(family="Cascadia Code",size=13, weight="bold"), fg_color="black")
        self.txtbox_listado.grid(row=2, column=0, sticky="nsew", pady=(5,0), padx=(100,100))
        self.txtbox_listado.insert("0.0", "Salida:\n\n" + "Esperando al usuario...")
        #------------------------
        
        #TAB (PRIORIDAD SEGUN EDAD) | TABVIEW
        self.tabview.tab("Prioridad segun Edad").grid_columnconfigure(4, weight=1)
        self.tabview.tab("Prioridad segun Edad").grid_rowconfigure(10, weight=1)
        
        #MODIFICAR URGENCIA POR EDAD
        #------------------------
        self.lbl_prioridad_eda = customtkinter.CTkLabel(self.tabview.tab("Prioridad segun Edad"),font=customtkinter.CTkFont(size=20) ,text= "Urgencia Por Edad", height=40, width=300)
        self.lbl_prioridad_eda .grid(row=0, column=0, sticky="nsew", pady=(20,0), padx=(15,0))
        
        self.lbl_espacio = customtkinter.CTkLabel(self.tabview.tab("Prioridad segun Edad"),font=customtkinter.CTkFont(size=10, weight="bold") ,text= "______________________________________________________________", height=40, width=300)
        self.lbl_espacio.grid(row=1, column=0, sticky="nsew", pady=(5,0), padx=(15,0))
        
        self.lbl_edadmin = customtkinter.CTkLabel(self.tabview.tab("Prioridad segun Edad"),font=customtkinter.CTkFont(size=13) ,text= "Edad min", height=40, width=300)
        self.lbl_edadmin.grid(row=2, column=0, sticky="nsew", pady=(5,0), padx=(15,0))
        
        self.txtbox_edadmin = customtkinter.CTkTextbox(self.tabview.tab("Prioridad segun Edad"),font=customtkinter.CTkFont(size=18), height=40, width=300)
        self.txtbox_edadmin.grid(row=3, column=0, sticky="nsew", pady=(5,0), padx=(15,0))
        
        self.lbl_edadmax = customtkinter.CTkLabel(self.tabview.tab("Prioridad segun Edad"),font=customtkinter.CTkFont(size=13) ,text= "Edad max", height=40, width=300)
        self.lbl_edadmax.grid(row=4, column=0, sticky="nsew", pady=(5,0), padx=(15,0))

        self.txtbox_edadmax = customtkinter.CTkTextbox(self.tabview.tab("Prioridad segun Edad"),font=customtkinter.CTkFont(size=18, weight="bold"), height=40, width=300)
        self.txtbox_edadmax.grid(row=5, column=0, sticky="nsew", pady=(5,0), padx=(15,0))        

        self.lbl_estado_edad = customtkinter.CTkLabel(self.tabview.tab("Prioridad segun Edad"),font=customtkinter.CTkFont(size=10, weight="bold") ,text= "Estado de urgencia", height=40, width=300)
        self.lbl_estado_edad.grid(row=6, column=0, sticky="nsew", pady=(5,0), padx=(15,0))

        self.combox_estado_edad = customtkinter.CTkComboBox(self.tabview.tab("Prioridad segun Edad"),values=["baja", "media", "alta"],height=40)
        self.combox_estado_edad.grid(row=7, column=0, sticky="nsew", pady=(5,0), padx=(15,0))
        
        self.btn_MODIFICARURGENCIAEDAD = customtkinter.CTkButton(self.tabview.tab("Prioridad segun Edad"),height=40,text="Cambiar Prioridad En El Rango", command= lambda: self.COMMAND_ModificarUrgenciaPorRangoEdad())
        self.btn_MODIFICARURGENCIAEDAD.grid(row=8, column=0, pady=(30,0))
        
        self.txtbox_listado_edad = customtkinter.CTkTextbox(self.tabview.tab("Prioridad segun Edad"),font=customtkinter.CTkFont(family="Cascadia Code",size=13, weight="bold"), height=40, width=300,fg_color="black")
        self.txtbox_listado_edad.grid(row=0, column=1, sticky="nsew", pady=(5,0), padx=(15,0), rowspan=9, columnspan=4)
        self.txtbox_listado_edad.insert("0.0", "/User > \n\nModificar urgencia de pacientes por edad: \n\n")
        #------------------------
            
        #TAB (ELIMINAR SEGUN TIPO DE CONSULTA) | TABVIEW
        self.tabview.tab("Eliminar segun Consulta").grid_columnconfigure(4, weight=1)
        self.tabview.tab("Eliminar segun Consulta").grid_rowconfigure(10, weight=1)    
        
        #ELIMINAR SEGUN TIPO DE CONSULTA
        #------------------------
        self.lbl_eliminar_tipconsulta = customtkinter.CTkLabel(self.tabview.tab("Eliminar segun Consulta"),font=customtkinter.CTkFont(size=20) ,text= "Eliminar Segun Consulta", height=40, width=300)
        self.lbl_eliminar_tipconsulta.grid(row=0, column=0, sticky="nsew", pady=(20,0), padx=(15,0))
        
        self.lbl_espacio = customtkinter.CTkLabel(self.tabview.tab("Eliminar segun Consulta"),font=customtkinter.CTkFont(size=10, weight="bold") ,text= "______________________________________________________________", height=40, width=300)
        self.lbl_espacio.grid(row=1, column=0, sticky="nsew", pady=(5,0), padx=(15,0))
        
        self.lbl_eli_tipconsulta = customtkinter.CTkLabel(self.tabview.tab("Eliminar segun Consulta"),font=customtkinter.CTkFont(size=13) ,text= "Describa el Tipo de consulta a Eliminar", height=40, width=300)
        self.lbl_eli_tipconsulta.grid(row=2, column=0, sticky="nsew", pady=(5,0), padx=(15,0))
        
        self.txtbox_eli_tipconsulta = customtkinter.CTkTextbox(self.tabview.tab("Eliminar segun Consulta"),font=customtkinter.CTkFont(family="Cascadia Code",size=15), height=40)
        self.txtbox_eli_tipconsulta.grid(row=5, column=0, sticky="nsew", pady=(5,0), padx=(15,0))
        
        self.btn_ELIMINARPORTIPOCONSULTA = customtkinter.CTkButton(self.tabview.tab("Eliminar segun Consulta"),height=40,text="Eliminar Por Tipo De Consulta", command= lambda: self.COMMAND_EliminarSegunConsulta())
        self.btn_ELIMINARPORTIPOCONSULTA.grid(row=8, column=0, pady=(30,0))
        
        self.txtbox_listado_Eliminados = customtkinter.CTkTextbox(self.tabview.tab("Eliminar segun Consulta"),font=customtkinter.CTkFont(family="Cascadia Code",size=13, weight="bold"), height=500,width=300, fg_color="black")
        self.txtbox_listado_Eliminados.grid(row=0, column=1, sticky="nsew", pady=(5,0), padx=(15,0), rowspan=10, columnspan=4)
        self.txtbox_listado_Eliminados.insert("0.0", "/User > \n\nEliminar paciente. Motivo, Tipo de consulta:")
        #------------------------
        
        #TAB (ALTA PRIORIDAD) | TABVIEW
        self.tabview.tab("Alta prioridad").grid_columnconfigure(4, weight=1)
        self.tabview.tab("Alta prioridad").grid_rowconfigure(10, weight=1) 
        
        #GENERAR COLA DE ALTA PRIORIDAD
        #------------------------------
        self.lbl_generar_cola_prioridad = customtkinter.CTkLabel(self.tabview.tab("Alta prioridad"),font=customtkinter.CTkFont(size=20) ,text= "Generar Cola De Alta Prioridad", height=40, width=300)
        self.lbl_generar_cola_prioridad .grid(row=0, column=0, sticky="nsew", pady=(20,0), padx=(15,0))
        
        self.lbl_espacio = customtkinter.CTkLabel(self.tabview.tab("Alta prioridad"),font=customtkinter.CTkFont(size=10, weight="bold") ,text= "______________________________________________________________", height=40, width=300)
        self.lbl_espacio.grid(row=1, column=0, sticky="nsew", pady=(5,0), padx=(15,0))
        
        self.btn_GENERARCOLA = customtkinter.CTkButton(self.tabview.tab("Alta prioridad"),height=40,text="Generar Cola Alta Prioridad", command= lambda: self.COMMAND_ListarColaPrioridad())
        self.btn_GENERARCOLA.grid(row=8, column=0, pady=(30,0))
        
        self.txtbox_listado_cola = customtkinter.CTkTextbox(self.tabview.tab("Alta prioridad"),font=customtkinter.CTkFont(family="Cascadia Code",size=13, weight="bold"), height=500,width=300, fg_color="black")
        self.txtbox_listado_cola.grid(row=0, column=1, sticky="nsew", pady=(5,0), padx=(15,0), rowspan=10, columnspan=4)
        self.txtbox_listado_cola.insert("0.0", "/User > \n\nCola De Alta Prioridad. Motivo, Estado De Urgencia:")
        #------------------------------
        
        #TAB (INTERVALO HORARIO) | TABVIEW
        self.tabview.tab("Intervalo horario").grid_columnconfigure(4, weight=1)
        self.tabview.tab("Intervalo horario").grid_rowconfigure(10, weight=1) 
        
        #GENERAR LISTA DE ESPERA CON RANGO HORARIO
        #------------------------------
        self.lbl_lista_espera = customtkinter.CTkLabel(self.tabview.tab("Intervalo horario"),font=customtkinter.CTkFont(size=20) ,text= "Nueva Lista", height=40, width=300)
        self.lbl_lista_espera .grid(row=0, column=0, sticky="nsew", pady=(20,0), padx=(15,0))
        
        self.lbl_espacio = customtkinter.CTkLabel(self.tabview.tab("Intervalo horario"),font=customtkinter.CTkFont(size=10, weight="bold") ,text= "______________________________________________________________", height=40, width=300)
        self.lbl_espacio.grid(row=1, column=0, sticky="nsew", pady=(0,0), padx=(15,0))
        
        self.lbl_horariomin = customtkinter.CTkLabel(self.tabview.tab("Intervalo horario"),font=customtkinter.CTkFont(size=13) ,text= "Horario min", height=40, width=300)
        self.lbl_horariomin.grid(row=2, column=0, sticky="nsew", pady=(5,0), padx=(15,0))
        
        self.txtbox_horariomin = customtkinter.CTkTextbox(self.tabview.tab("Intervalo horario"),font=customtkinter.CTkFont(size=18), height=40, width=300)
        self.txtbox_horariomin.grid(row=3, column=0, sticky="nsew", pady=(5,0), padx=(15,0))
        
        self.lbl_horariomax = customtkinter.CTkLabel(self.tabview.tab("Intervalo horario"),font=customtkinter.CTkFont(size=13) ,text= "Horario max", height=40, width=300)
        self.lbl_horariomax.grid(row=4, column=0, sticky="nsew", pady=(5,0), padx=(15,0))

        self.txtbox_horariomax = customtkinter.CTkTextbox(self.tabview.tab("Intervalo horario"),font=customtkinter.CTkFont(size=18), height=40, width=300)
        self.txtbox_horariomax.grid(row=5, column=0, sticky="nsew", pady=(5,0), padx=(15,0))        

        self.combox_estado_horario = customtkinter.CTkComboBox(self.tabview.tab("Intervalo horario"),values=["baja", "media", "alta"],height=50)
        self.combox_estado_horario.grid(row=3, column=1, sticky="nsew", pady=(0,0), padx=(15,0))
        
        self.btn_GENERARLISTAESPERAHORARIO = customtkinter.CTkButton(self.tabview.tab("Intervalo horario"),height=50,text="Generar Lista De Espera", command= lambda: self.COMMAND_PrioridadPorFechaHorario())
        self.btn_GENERARLISTAESPERAHORARIO.grid(row=5, column=1, pady=(0,0))
        
        self.txtbox_listado_intervalo_horario = customtkinter.CTkTextbox(self.tabview.tab("Intervalo horario"),font=customtkinter.CTkFont(family="Cascadia Code",size=13, weight="bold"), height=450,width=300, fg_color="black")#text_color="#16C60C"
        self.txtbox_listado_intervalo_horario.grid(row=0, column=2, sticky="nsew", pady=(5,0), padx=(15,0), rowspan=10, columnspan=4)
        self.txtbox_listado_intervalo_horario.insert("0.0", "/User > \n\nListado Segun Fecha y Rango Horario: \n\n")
        
        self.calendar = Calendar(self.tabview.tab("Intervalo horario"), selectmode='day', year=2024, month=1, day=1)
        self.calendar.grid(row=1, column=1, sticky="nsew", pady=(80,0), padx=(15,0))
        #------------------------------
    
    #FUNCION QUE DEVUELVE TRUE SI NO HAY CARACTERES INVALIDOS
    def CaracterInvalido(self, cadena):
        if cadena == '\n':
            return True
        # Definir una expresión regular que busca dígitos o caracteres especiales
        patron = re.compile(r'[\d@#$%^&*()_+\-=\[\]{};\'\\:"|<,./<>?]')    
        # Buscar coincidencias en el nombre
        if patron.search(cadena):
            return True
        else:
            return False
    
    #BLOQUE DE CONVERSION DE TEXTO A DATETIME
    def convertir_cadena_a_datetime(self, cadena, formato):
        fecha_y_hora = datetime.datetime.strptime(cadena, formato)
        return fecha_y_hora
        
    def ValidacionId(self, ID):
        #LISTA DE ERRORES
        self.ERRORES = []  
        if ID < 0:                  
            self.ERRORES.append("La ID no puede ser negativa")            
        #SI HAY ERRORES  LANZO EL CARTEL CON CADA UNO DE LOS ERRORES  
        if self.ERRORES:
            raise ValueError("Errores de validación: " + "; ".join(self.ERRORES))
    
    def ValidacionNombre(self, Nombre):
        #LISTA DE ERRORES
        self.ERRORES = []  
         #VERIFICO CARACTERES INVALIDOS EN EL NOMBRE
        if self.CaracterInvalido(Nombre) == True:
            self.ERRORES.append("Caracter inválido en el nombre o Vacio")        
        #SI HAY ERRORES  LANZO EL CARTEL CON CADA UNO DE LOS ERRORES  
        if self.ERRORES:
            raise ValueError("Errores de validación: " + "; ".join(self.ERRORES))
        
    def ValidacionConsulta(self, TipoDeConsulta):
        #LISTA DE ERRORES
        self.ERRORES = []  
        #VERIFICO CARACTERES INVALIDOS EN EL NOMBRE
        if self.CaracterInvalido(TipoDeConsulta) == True:
            self.ERRORES.append("Caracter inválido en el Tipo de Consulta")        
        #SI HAY ERRORES  LANZO EL CARTEL CON CADA UNO DE LOS ERRORES  
        if self.ERRORES:
            raise ValueError("Errores de validación: " + "; ".join(self.ERRORES))
    
    def ValidacionEdad(self, Edad):
        #VERIFICO SI LA EDAD ES NUMERICO
        patron = re.compile(r'^\d+$')
        Flag = bool(patron.match(Edad))
        if Flag == False:
            self.ERRORES.append("La Edad es Numerica")
         #SI HAY ERRORES  LANZO EL CARTEL CON CADA UNO DE LOS ERRORES  
        if self.ERRORES:
            raise ValueError("Errores de validación: " + "; ".join(self.ERRORES))
                  
    #ACTUALIZA LA PROXIMA ID A ASIGNAR
    def INCREMENTAR_ID(self):
        self.IDs += 1
    
    #COMANDO VINCULADO AL BOTON AGREGAR PACIENTE
    def COMMAND_AgregarPaciente(self):        
        #OBTENGO ID PARA EL PACIENTE
        ID = self.IDs
        #OBTENGO VALORES DE LOS TEXTBOX CON SU METODO .get "OBTENGO EL STRING DEL WIDGET DESDE LA POSICION C=0 y F=0 DE LA CADENA"
        Nombre = self.txtbox_nom_ing.get("0.0", "end")
        TipoDeConsulta = self.txtbox_tipcon_ing.get("0.0", "end")
        Edad = self.txtbox_eda_ing.get("0.0", "end")
        #OBTENGO EL VALOR DE EL COMBOBOX CON SU METODO .get "OBTENGO EL STRING DEL WIDGET EN SU MENU DE ELECCION MULTIPLE"
        EstadoDeUrgencia = self.combox_esturg_ing.get()
        #GENERO A TRAVEZ DE LA LIBRERIA DATETIME LA FECHA Y HORA ACTUAL EN LA QUE SE EJECUTA LA INSTRUCCION
        FechaDeIngreso = datetime.datetime.today().strftime("%Y-%m-%d")
        HoraDeIngreso = datetime.datetime.now().strftime('%H:%M')
        #VALIDACION DE LA ENTRADA
        try:
            #BLOQUE DE VALIDACIONES
            self.ValidacionId(ID)
            self.ValidacionNombre(Nombre)
            self.ValidacionConsulta(TipoDeConsulta)
            self.ValidacionEdad(Edad)
            #1ro INICIALIZAR PACIENTE
            Paciente = TADPaciente.CrearPaciente()
            #2do ASIGNAR DATOS AL PACIENTE
            TADPaciente.CargarPaciente(Paciente, ID, Nombre, TipoDeConsulta, Edad, EstadoDeUrgencia, FechaDeIngreso, HoraDeIngreso)
            #3ro DAR DE ALTA AL PACIENTE EN LA LISTA DE ESPERA
            TADClinica.AgregarPaciente(ListaDeEspera, Paciente)        
            #INCREMENTO ID 
            self.INCREMENTAR_ID()
            messagebox.showinfo(message="Paciente Generado", title="Sistema clinica")
        except ValueError as e:
            #SI OCURRE UNA EXCEPCION DEVUELVE CADA UNO DE LOS ERRORES QUE OCURRIERON
            messagebox.showerror("Error", f"TypeError: {str(e)}")
        #LIMPIO LA LISTA DE ERRORES
        self.ERRORES = []          
    
    #COMANDO VINCULADO AL EVENTO DE CAMBIAR DE PESTAÑA
    def COMMAND_ListarPacientes(self):
        #INICIALIZO EL TEXTO QUE REFLEJARA EL LISTADO DE LOS PACIENTES
        Text = ""
        #COMO DEBO CONTAR PACIENTE POR PACIENTE, NECESITO SABER CUAL ES EL LIMITE HASTA DONDE DEBO CONTAR
        CantidadPacientes = TADClinica.Tamano(ListaDeEspera)   
        #OBSERVO CADA UNO DE LOS PACIENTES HASTA LA QUE LLEGUE AL PACIENTE QUE ES IGUAL A LA CANTIDAD DE PACIENTES
        for i in range(CantidadPacientes):   
            #RECUPERO EL PACIENTE                  
            Paciente = TADClinica.RecuperarPaciente(ListaDeEspera, i)
            #RELLENO EL TEXTO CON LOS DATOS DE UN PACIENTE  
            ID = TADPaciente.VerID(Paciente)    
            ID = "ID: " + str(ID)
            Nombre = "Nombre: " + TADPaciente.VerNombre(Paciente)
            TipoDeConsulta = "Tipo de Consulta: " + TADPaciente.VerTipoDeConsulta(Paciente)
            Edad = "Edad: " + TADPaciente.VerEdad(Paciente)
            EstadoDeUrgencia = "Estado De Urgencia: " + TADPaciente.VerEstadoDeUrgencia(Paciente)
            FechaDeIngreso = "Fecha De Ingreso: " + TADPaciente.VerFechaDeIngreso(Paciente)
            HorarioDeIngreso = "Horario De Ingreso: " + TADPaciente.VerHorarioDeIngreso(Paciente)           
            Text +=  ID + "\n\n    ." + Nombre + "\n    ." + TipoDeConsulta + "\n    ." + Edad + "\n    ." + EstadoDeUrgencia + "\n\n    ." + FechaDeIngreso + "\n\n    ." + HorarioDeIngreso + "\n\n"         
        #LIMPIO LA PANTALLA
        self.txtbox_listado.delete("0.0", "end")
        #INSERTO EL TEXTO
        self.txtbox_listado.insert("0.0", "/User > \n\nPacientes: \n\n" + Text)
    
    #COMANDO VINCULADO AL BOTON MODIFICAR SEGUN NOMBRE 
    def COMMAND_ModificarUrgenciaPorID(self):
        #OBTENGO VALORES DE LOS TEXTBOX CON SU METODO .get "OBTENGO EL STRING DEL WIDGET DESDE LA POSICION C=0 y F=0 DE LA CADENA"
        ID = int(self.txtbox_ID_mod.get("0.0", "end"))
        try:
            self.ValidacionId(ID)
            #OBTENGO EL VALOR DE EL COMBOBOX CON SU METODO .get "OBTENGO EL STRING DEL WIDGET EN SU MENU DE ELECCION MULTIPLE"
            EstadoDeUrgencia = self.combox_esturg_mod.get()
            #SI NECESITO CONTAR UNO POR UNO LOS PACIENTES PARA VER SI ES LA ID QUE BUSCO NECESITO SABER HASTA DONDE CONTAR
            CantidadPacientes = TADClinica.Tamano(ListaDeEspera)
            #VOY VIENDO UNO POR UNO SUS DATOS DONDE I REPRESENTA COMO VOY ENUMERANDO
            for i in range(CantidadPacientes):
                #RECUPERAR UN PACIENTE
                Paciente = TADClinica.RecuperarPaciente(ListaDeEspera, i)
                #SI ES LA ID DEL PACIENTE
                if TADPaciente.VerID(Paciente) == ID:
                    #MODIFICO SU ESTADO DE URGENCIA
                    TADPaciente.ModificarTipoUrgencia(Paciente, EstadoDeUrgencia)
            messagebox.showinfo(message="Paciente Modificado", title="Sistema clinica")
        except ValueError as e:
            #SI OCURRE UNA EXCEPCION DEVUELVE CADA UNO DE LOS ERRORES QUE OCURRIERON
            messagebox.showerror("Error", f"TypeError: {str(e)}")
        #LIMPIO LA LISTA DE ERRORES
        self.ERRORES = [] 
    
    #COMANDO VINCULADO AL BOTON ELIMINAR SEGUN NOMBRE           
    def COMMAND_EliminarSegunElID(self):
        #OBTENGO VALORES DE LOS TEXTBOX CON SU METODO .get "OBTENGO EL STRING DEL WIDGET DESDE LA POSICION C=0 y F=0 DE LA CADENA"
        ID = int(self.txtbox_ID_eli.get("0.0", "end"))
        try:
            #SI NECESITO VER UNO POR UNO UNA UNICA VEZ, LA CANTIDAD DE PACIENTES QUE VOY A TENER QUE VER VA A SER IGUAL A LA CANTIDAD DE PACIENTES
            CantidadPacientes = TADClinica.Tamano(ListaDeEspera)
            #OBSERVO UNO POR UNO
            nro = 1            
            while nro <= CantidadPacientes:
                #RECUPERAR UN PACIENTE
                Paciente = TADClinica.RecuperarPaciente(ListaDeEspera, nro)
                #SI ES SU ID
                if TADPaciente.VerID(Paciente) == ID:
                    #ELIMINO ESE PACIENTE
                    TADClinica.EliminarPaciente(ListaDeEspera, Paciente)
                    break
                else:
                    nro += 1
            messagebox.showinfo(message="Paciente Eliminado", title="Sistema clinica")
        except ValueError as e:
            #SI OCURRE UNA EXCEPCION DEVUELVE CADA UNO DE LOS ERRORES QUE OCURRIERON
            messagebox.showerror("Error", f"TypeError: {str(e)}")
        #LIMPIO LA LISTA DE ERRORES
        self.ERRORES = []
        
    #COMANDO VINCULADO AL BOTON MODIFICAR URGENCIA POR RANGO DE EDAD
    def COMMAND_ModificarUrgenciaPorRangoEdad(self):
        #INICIALIZO EL TEXTO QUE REFLEJARA EL LISTADO DE LOS PACIENTES EN LOS QUE MODIFIQUE SU ESTADO DE URGENCIA
        Text = ""
        #OBTENGO VALORES DE LOS TEXTBOX CON SU METODO .get "OBTENGO EL STRING DEL WIDGET DESDE LA POSICION C=0 y F=0 DE LA CADENA"
        EdadMin = self.txtbox_edadmin.get("0.0", "end")
        EdadMax = self.txtbox_edadmax.get("0.0", "end")
        #OBTENGO EL VALOR DE EL COMBOBOX CON SU METODO .get "OBTENGO EL STRING DEL WIDGET EN SU MENU DE ELECCION MULTIPLE"
        EstadoDeUrgencia = self.combox_estado_edad.get()
        #SI DEBO ENUMERAR DENTRO DE UN CONJUNTO NECESITO SABER CUANTOS ELEMENTOS HAY EN ESE CONJUNTO
        CantidadPacientes = TADClinica.Tamano(ListaDeEspera)
        try:
            self.ValidacionEdad(EdadMin)
            self.ValidacionEdad(EdadMax)
            #ASOCIO UN NUMERO ALEATORIO PERO NO REPETIDO A CADA PACIENTE Y LOS ENUMERO
            for i in range(CantidadPacientes):
                #RECUPERO UN PACIENTE
                Paciente = TADClinica.RecuperarPaciente(ListaDeEspera, i)
                EdadPac = TADPaciente.VerEdad(Paciente)
                #SI LA EDAD DE ESE PACIENTE ESTA EN EL RANGO
                if int(EdadPac) >= int(EdadMin) and int(EdadPac) <= int(EdadMax):
                    #MODIFICO SU ESTADO DE URGENCIA               
                    TADPaciente.ModificarTipoUrgencia(Paciente, EstadoDeUrgencia)
                    Text += TADPaciente.VerNombre(Paciente) + "Modificado, Nuevo estado de urgencia: " + EstadoDeUrgencia + "\n\n"
            #LIMPIO LA PANTALLA
            self.txtbox_listado_edad.delete("0.0", "end")
            #INSERTO EL TEXTO
            self.txtbox_listado_edad.insert("0.0", "/User > \n\nModificar urgencia de pacientes por edad: \n\n" + Text)
        except ValueError as e:
            #SI OCURRE UNA EXCEPCION DEVUELVE CADA UNO DE LOS ERRORES QUE OCURRIERON
            messagebox.showerror("Error", f"TypeError: {str(e)}")
        #LIMPIO LA LISTA DE ERRORES
        self.ERRORES = []       
        
    #COMANDO VINCULADO AL BOTON ELIMINAR SEGUN TIPO DE CONSULTA    
    def COMMAND_EliminarSegunConsulta(self):
        #INICIALIZO EL TEXTO QUE REFLEJARA EL LISTADO DE LOS PACIENTES EN LOS QUE ELIMINARE SEGUN SU TIPO DE CONSULTA
        Text = ""
        #OBTENGO VALORES DE LOS TEXTBOX CON SU METODO .get "OBTENGO EL STRING DEL WIDGET DESDE LA POSICION C=0 y F=0 DE LA CADENA"
        TipoDeConsulta = self.txtbox_eli_tipconsulta.get("0.0", "end")
        #NECESITO SABER CUANTOS POSIBLES A ELIMINAR SON
        CantidadPacientes = TADClinica.Tamano(ListaDeEspera)
        nro = 1
        try:
            self.ValidacionConsulta(TipoDeConsulta)
            #ENUMERO UNO POR UNO
            while nro <= CantidadPacientes:
                #RECUPERAR UN PACIENTE
                Paciente = TADClinica.RecuperarPaciente(ListaDeEspera, nro)
                ConsultaPaciente = TADPaciente.VerTipoDeConsulta(Paciente)
                #ESTA CONSULTA EL LA QUE SE DESEA ELIMINAR
                if TipoDeConsulta == ConsultaPaciente:
                    TADClinica.EliminarPaciente(ListaDeEspera, Paciente)
                    Text += TADPaciente.VerNombre(Paciente) + "Eliminado, Su Consulta era: " + TipoDeConsulta + "\n\n"
                    CantidadPacientes = TADClinica.Tamano(ListaDeEspera)
                else:
                    nro += 1                       
            #LIMPIO LA PANTALLA
            self.txtbox_listado_Eliminados.delete("0.0", "end")
            #INSERTO EL TEXTO
            self.txtbox_listado_Eliminados.insert("0.0", "/User > \n\nEliminar paciente. Motivo, Tipo de consulta: \n\n" + Text)
        except ValueError as e:
            #SI OCURRE UNA EXCEPCION DEVUELVE CADA UNO DE LOS ERRORES QUE OCURRIERON
            messagebox.showerror("Error", f"TypeError: {str(e)}")
        #LIMPIO LA LISTA DE ERRORES
        self.ERRORES = []
        
    #COMANDO VINCULADO AL BOTON LISTAR COLA DE ALTA PRIORIDAD
    def COMMAND_ListarColaPrioridad(self):
        ColaPrioridad = TADCola.CrearCola()      
        ColaAuxiliar = TADCola.CrearCola()
        #INICIALIZO EL TEXTO QUE REFLEJARA EL LISTADO DE LOS PACIENTES QUE ESTAN EN ALTA PRIORIDAD
        Text = ""
        CantidadPacientes = TADClinica.Tamano(ListaDeEspera)
        #RELLENO LA COLA ALTA PRIORIDAD
        for i in range(CantidadPacientes):
            Paciente = TADClinica.RecuperarPaciente(ListaDeEspera, i)
            if TADPaciente.VerEstadoDeUrgencia(Paciente) == 'alta':
                TADCola.Queue(ColaPrioridad, Paciente)
        #COPIO LA COLA
        TADCola.CopiarCola(ColaPrioridad, ColaAuxiliar)
        #DESENCOLA LA COLA HASTA QUE ESTE VACIA
        while TADCola.IsEmpty(ColaAuxiliar) == False:
            Paciente = TADCola.EnQueue(ColaAuxiliar)
            #RESGUARDO LOS DATOS DEL PACIENTE
            ID = TADPaciente.VerID(Paciente)    
            ID = "ID: " + str(ID) 
            Nombre = "Nombre: " + TADPaciente.VerNombre(Paciente)
            TipoDeConsulta = "Tipo de Consulta: " + TADPaciente.VerTipoDeConsulta(Paciente)
            Edad = "Edad: " + TADPaciente.VerEdad(Paciente)
            EstadoDeUrgencia = "Estado De Urgencia: " + TADPaciente.VerEstadoDeUrgencia(Paciente)
            FechaDeIngreso = "Fecha De Ingreso: " + TADPaciente.VerFechaDeIngreso(Paciente)
            HorarioDeIngreso = "Horario De Ingreso: " + TADPaciente.VerHorarioDeIngreso(Paciente)           
            #GUARDO LOS DATOS DEL PACIENTE EN EL TEXTO A REFLEJAR
            Text +=  ID + "\n\n    ." + Nombre + "\n    ." + TipoDeConsulta + "\n    ." + Edad + "\n    ." + EstadoDeUrgencia + "\n\n    ." + FechaDeIngreso + "\n\n    ." + HorarioDeIngreso + "\n\n"
        #LIMPIO LA PANTALLA
        self.txtbox_listado_cola.delete("0.0", "end")
        #INSERTO EL TEXTO
        self.txtbox_listado_cola.insert("0.0", "/User > \n\nCola De Alta Prioridad. Motivo, Estado De Urgencia: \n\n" + Text)
        
    #COMANDO VINCULADO AL BOTON GENERAR NUEVA LISTA DE ESPERA SEGUN FECHA Y HORARIO       
    def COMMAND_PrioridadPorFechaHorario(self):
        #INICIALIZO EL TEXTO QUE REFLEJARA EL LISTADO DE LOS PACIENTES SEGUN LA FECHA Y HORARIO
        Text = ""
        #NECESITO MIRAR UNO POR UNO SI ESTA EN LA FECHA Y SI ESTA EN EL INTERVALO HORARIO
        CantidadPacientes = TADClinica.Tamano(ListaDeEspera)
        #OBTENGO VALORES DE LOS TEXTBOX CON SU METODO .get "OBTENGO EL STRING DEL WIDGET DESDE LA POSICION C=0 y F=0 DE LA CADENA"
        HorarioMinimo = self.txtbox_horariomin.get("0.0", "end")
        HorarioMaximo = self.txtbox_horariomax.get("0.0", "end")
        try:
            #OBTENGO EL VALOR DE EL COMBOBOX CON SU METODO .get "OBTENGO EL STRING DEL WIDGET EN SU MENU DE ELECCION MULTIPLE"
            EstadoDeUrgencia = self.combox_estado_edad.get()
            #OBTENGO EL VALOR DE EL CALENDAR CON SU METODO SELECTION_GET "OBTENGO LA FECHA SELECCIONADA EN EL WIDGET"
            FechaIngreso = self.calendar.selection_get() #<W
            #CONVIERTO EN DATETIME        
            HorarioMinimoOBJ = self.convertir_cadena_a_datetime(HorarioMinimo.strip(), '%H:%M') #<w
            HorarioMaximoOBJ =  self.convertir_cadena_a_datetime(HorarioMaximo.strip(), '%H:%M') #<w
            for i in range(CantidadPacientes):
                #RECUPERO AL PACIENTE
                Paciente = TADClinica.RecuperarPaciente(ListaDeEspera, i)
                #OBTENGO FECHA DE INGRESO Y HORARIO DE INGRESO
                FechaPac = datetime.datetime.strptime(TADPaciente.VerFechaDeIngreso(Paciente), '%Y-%m-%d')                
                HorarioPac = datetime.datetime.strptime(TADPaciente.VerHorarioDeIngreso(Paciente), '%H:%M')
                #SI ES LA FECHA Y ADEMAS ESTA EN EL RANGO HORARIO
                if FechaPac.date() == FechaIngreso and HorarioPac >= HorarioMinimoOBJ and HorarioPac <= HorarioMaximoOBJ:
                    #SI SE CUMPLEN LAS CONDICIONES LO AGREGO A LA LISTA DE ESPERA SEGUN FECHA Y HORARIO
                    TADClinica.AgregarPaciente(ListaDeEsperaSegunFechaHorario, Paciente)
                    #RESGUARDO LOS DATOS DEL PACIENTE
                    ID = TADPaciente.VerID(Paciente)    
                    ID = "ID: " + str(ID)
                    Nombre = "Nombre: " + TADPaciente.VerNombre(Paciente)
                    TipoDeConsulta = "Tipo de Consulta: " + TADPaciente.VerTipoDeConsulta(Paciente)
                    Edad = "Edad: " + TADPaciente.VerEdad(Paciente)
                    EstadoDeUrgencia = "Estado De Urgencia: " + TADPaciente.VerEstadoDeUrgencia(Paciente)
                    FechaDeIngreso = "Fecha De Ingreso: " + TADPaciente.VerFechaDeIngreso(Paciente)
                    HorarioDeIngreso = "Horario De Ingreso: " + TADPaciente.VerHorarioDeIngreso(Paciente)     
                    #GUARDO LOS DATOS DEL PACIENTE EN EL TEXTO A REFLEJAR
                    Text += ID + "\n\n    ." + Nombre + "\n    ." + TipoDeConsulta + "\n    ." + Edad + "\n    ." + EstadoDeUrgencia + "\n\n    ." + FechaDeIngreso + "\n\n    ." + HorarioDeIngreso + "\n\n"            
            #LIMPIO LA PANTALLA
            self.txtbox_listado_intervalo_horario.delete("0.0", "end")
            #INSERTO EL TEXTO
            self.txtbox_listado_intervalo_horario.insert("0.0", "/User > \n\nListado Segun Fecha y Rango Horario: \n\n" + Text)                
        except ValueError as e:
            #SI OCURRE UNA EXCEPCION DEVUELVE CADA UNO DE LOS ERRORES QUE OCURRIERON
            messagebox.showerror("Error", f"TypeError: {str(e)}")
        #LIMPIO LA LISTA DE ERRORES
        self.ERRORES = []
                            
if __name__ == "__main__":
    app = App()
    app.mainloop()