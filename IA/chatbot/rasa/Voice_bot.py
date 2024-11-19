import requests
import speech_recognition as sr     # importar la biblioteca
import subprocess
from gtts import gTTS

# sender = input("¿Cuál es tu nombre?\n")

bot_message = ""
message=""

r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})

print("El bot dice, ", end=' ')
for i in r.json():
    bot_message = i['text']
    print(f"{bot_message}")

myobj = gTTS(text=bot_message)
myobj.save("welcome.mp3")
print('guardado')
# Reproducir el archivo convertido
subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])

while bot_message != "Bye" or bot_message != 'thanks':

    r = sr.Recognizer()  # inicializar el reconocedor
    with sr.Microphone() as source:  # especificar la fuente, puede ser el micrófono o archivos de audio
        print("Habla algo :")
        audio = r.listen(source)  # escuchar desde la fuente
        try:
            message = r.recognize_google(audio)  # usar el reconocedor para convertir el audio a texto
            print("Dijiste : {}".format(message))

        except:
            print("Lo siento, no pude reconocer tu voz")  # En caso de que no se reconozca claramente la voz
    if len(message) == 0:
        continue
    print("Enviando el mensaje ahora...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

    print("El bot dice, ", end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

    myobj = gTTS(text=bot_message)
    myobj.save("welcome.mp3")
    print('guardado')
    # Reproducir el archivo convertido
    subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])