import os
import google.generativeai as genai

def limpiar_pantalla():
    # Verifica si el sistema operativo es Windows
    if os.name == 'nt':  # nt significa Windows
        os.system('cls')
    else:  # En otros sistemas, como Unix (Linux/macOS)
        os.system('clear')

genai.configure(api_key="AIzaSyD_UnXrnr9biQpWReZnBEVaQHzlHdyNpeQ")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

historial = []

modelo = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

while True:
    limpiar_pantalla()
    entrada = input("Tu: ")
    if entrada == "exit":
        break
    sesion = modelo.start_chat(history=historial)
    respuesta = sesion.send_message(entrada)
    respuesta_modelo = respuesta.text
    print(f'Bot: {respuesta_modelo}')   
    historial.append({"role": "user", "parts": [entrada]})
    historial.append({"role": "user", "parts": [entrada]})