import pytesseract

#IMPORTO LIBRERIAS
import os
import sys
import tkinter
import tkinter.messagebox
from tkinter import filedialog
import customtkinter
from PIL import Image
import datetime

#RUTA RAIZ
program_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

#VARIABLES GUI
placeholder_image = program_directory + r'\resources\imagen.png'

#VARIABLES
image_directory = os.path.join(os.environ['USERPROFILE'], 'Pictures')
imagen = ""

#THEME
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

#CLASE APLICACION
class App(customtkinter.CTk):
    #DEFINO
    def __init__(self):
        super().__init__()

        #CONFIGURA LA VENTANA
        self.title("")
        self.geometry(f"{1100}x{580}")

        #CONFIGURAR EL GRID DEL LAYOUT
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1), weight=1)

        #CREO EL SIDEBAR FRAME CON LOS WIDGETS
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)
        #TITULO(LABEL)          | SIDEBAR
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Tesseract OCR", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        #BUTTON(ARCHIVO)        | SIDEBAR
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button1_event, text= "Seleccionar Archivo")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        #COMBOBOX(IDIOMA)       | SIDEBAR 
        self.combobox_1 = customtkinter.CTkComboBox(self.sidebar_frame,values=["Español", "Ingles"])
        self.combobox_1.grid(row=2, column=0, padx=20, pady=10)
        #COMBOBOX(OUTPUT)       | SIDEBAR
        self.combobox_2 = customtkinter.CTkComboBox(self.sidebar_frame,values=["Local", "Ruta"], command=lambda event: self.change_combobox2())
        self.combobox_2.grid(row=3, column=0, padx=20, pady=10)
        #BUTTON(RUTA)           | SIDEBAR
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button2_event)
        self.sidebar_button_2.grid(row=4, column=0, padx=20, pady=10)
        #LABEL(THEME)           | SIDEBAR   
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Theme:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        #OPTIONMENU(APPEARANCE) | SIDEBAR
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))
        #LABEL(SCALE)           | SIDEBAR
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Escala UI:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        #OPTIONMENU(SCALING)    | SIDEBAR
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))

        #ENTRY(NOMBRE SALIDA)   | SELF
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Ingrese El Nombre Del Archivo", state="readonly")
        self.entry.grid(row=3, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")
        #BUTTON(CONVERTIR)      | SELF
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), hover_color="green", text="Convertir", command=self.main_button)
        self.main_button_1.grid(row=3, column=2, padx=(100, 100), pady=(20, 20), sticky="nsew")
        #TEXTBOX(SALIDA)        | SELF
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1,rowspan = 2 ,padx=(20, 0), pady=(20, 0), sticky="nsew")

        #CREAR CONTEDOR IMAGEN
        self.container_image_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.container_image_frame.grid(row=0, column=2, rowspan= 3,padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.container_image_frame.grid_columnconfigure(0, weight=1)
        self.container_image_frame.grid_rowconfigure(0, weight=1)
        self.var_image_light = customtkinter.CTkImage(light_image = Image.open(placeholder_image), size=( 300,300))
        self.var_image_dark = customtkinter.CTkImage(dark_image = Image.open(placeholder_image), size=(300,300))
        self.image_label = customtkinter.CTkLabel(self.container_image_frame, image = self.var_image_dark, text="")
        self.image_label.grid(row = 0, column = 0, pady=0, padx=20, sticky="nsew")
        
        #SET VALORES PREDETERMINADOS | MISCELANEO
        self.sidebar_button_1.configure(state="enable")
        self.combobox_1.set("Español")
        self.combobox_2.set("Local")
        self.sidebar_button_2.configure(state="disabled", text="Seleccionar Ruta")       
        self.textbox.insert("0.0", "Salida:\n\n" + "Esperando al usuario...")
        self.textbox.configure(state="disable")       
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button1_event(self):
        global imagen
        file_path = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.jpg;*.jpeg;*.png")])
        imagen = file_path
        self.var_image_dark = customtkinter.CTkImage(dark_image = Image.open(imagen), size=(300,300))
        self.image_label.configure(image = self.var_image_dark)
                
    def sidebar_button2_event(self):
        folder_path = filedialog.askdirectory()
        
    def change_combobox1(self):
        lenguaje = self.combobox_1.get()
        
    def change_combobox2(self):
        tipo = self.combobox_2.get()
        if tipo == "Ruta":
            self.sidebar_button_2.configure(state="enable")
            self.entry.configure(state="normal")
            hora_actual = datetime.datetime.now()
            self.entry.insert(0,hora_actual)
        elif tipo == "Local":
            self.sidebar_button_2.configure(state="disabled")
            self.entry.delete(0,100)
            self.entry.configure(state="readonly")
            
    def main_button(self):
        if imagen != "":
            img = Image.open(imagen)
            string = pytesseract.obtener_texto(img)
            self.textbox.configure(state="normal")
            self.textbox.delete("0.0", "1000.0")
            self.textbox.insert("0.0", "Salida:\n\n" + string)        
        else:
            print("NULL")
            
        
        
            
#EJECUCION DE LA APLICACION
if __name__ == "__main__":
    app = App()
    app.mainloop()