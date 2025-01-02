from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Crear un chatbot
chatbot = ChatBot(
    'MiChatBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation'
    ],
    database_uri='sqlite:///database.db'
)

# Entrenamiento con el corpus de ChatterBot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.spanish')

# Función para interactuar con el chatbot
def interactuar():
    print("Hola, soy tu chatbot. Escribe 'salir' para terminar.")
    
    while True:
        try:
            entrada_usuario = input("Tú: ")
            if entrada_usuario.lower() == 'salir':
                print("Adiós!")
                break
            
            respuesta = chatbot.get_response(entrada_usuario)
            print(f"ChatBot: {respuesta}")
        
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

# Iniciar la interacción
interactuar()