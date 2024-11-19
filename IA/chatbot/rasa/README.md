# RasaCustomerService
Este es un bot conversacional que puede ser utilizado en el sector de telecomunicaciones para automatizar el proceso de atención al cliente a través de un bot de voz con la ayuda de este chatbot basado en Rasa.

Explicación sobre cómo está armado un proyecto utilizando Rasa
Un proyecto de Rasa generalmente consta de varios componentes para crear un bot de conversación. A continuación, te explico cómo se estructura y cómo se integran los elementos que mencionaste en los mensajes anteriores.

# 1. Estructura del Proyecto en Rasa
Un proyecto típico de Rasa tiene los siguientes archivos y carpetas:

## actions.py: Aquí se definen las acciones personalizadas que el bot puede ejecutar. Por ejemplo, acciones para consultar una base de datos o realizar alguna operación compleja.

## config.yml: 
Este archivo contiene la configuración del pipeline de procesamiento de lenguaje natural (NLP). En este archivo, se definen los componentes del pipeline que Rasa utilizará para procesar y entender los mensajes del usuario.

## domain.yml: 
Aquí se definen las entidades, intenciones (intents), acciones y respuestas del bot. Es el lugar donde defines los posibles mensajes del bot, las entidades que puede reconocer y las acciones que ejecutará.

## endpoints.yml: 
Contiene las configuraciones de los endpoints de la API del servidor de acciones personalizadas y el webhook de Rasa.

## nlu.md o nlu.yml: 
Define las intenciones y entidades que el bot puede entender. Aquí se entrenan los modelos de NLU (Natural Language Understanding) para que el bot pueda reconocer lo que el usuario dice.

## stories.md: 
Contiene los diálogos o historias que muestran cómo debe responder el bot a diferentes secuencias de mensajes. Esto ayuda a entrenar el modelo de diálogo.
## credentials.yml: 
Contiene las credenciales necesarias para integrar el bot con diferentes canales de comunicación como REST, Slack, Facebook, etc.

## rules.yml: 
Define reglas fijas para las conversaciones, por ejemplo, cómo responder ante ciertas intenciones.

2. # Componente de Voz en Rasa
El bot también puede integrarse con servicios de voz para interactuar con los usuarios utilizando la voz en lugar de texto. Para esto, se utilizan tecnologías como Google Text-to-Speech (gTTS) y Speech Recognition en Python, que permiten transformar el texto en audio y reconocer comandos de voz del usuario.

## Reconocimiento de voz: 
Utilizando la biblioteca speech_recognition en Python, el bot puede recibir comandos de voz de los usuarios. Luego, convierte el audio en texto que es procesado por Rasa.

## Respuesta en voz: 
El bot puede responder con voz utilizando la biblioteca gTTS (Google Text-to-Speech), que convierte el texto de la respuesta en un archivo de audio y lo reproduce para el usuario.

### Flujo básico de conversación:

- El bot escucha el mensaje del usuario mediante un micrófono.
- El mensaje se convierte en texto utilizando la tecnología de reconocimiento de voz.
- El texto se envía a Rasa para ser procesado y determinar la respuesta adecuada.
- La respuesta del bot se convierte en un archivo de audio y se reproduce para el usuario.

3. # Interacción con el Servidor de Rasa
Cuando el bot recibe un mensaje (ya sea escrito o hablado), se envía al servidor de Rasa a través de un webhook REST. El servidor de Rasa procesa el mensaje, determina la intención del usuario y genera una respuesta.

Para interactuar con el servidor de Rasa, se utilizan solicitudes HTTP, como las siguientes:

**r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})**

Esto envía el mensaje al servidor de Rasa, y luego se obtiene la respuesta para ser procesada.

4. # Archivos Clave
## endpoints.yml: 
Define el endpoint del servidor de acciones personalizadas y las configuraciones del webhook.


action_endpoint:
  url: "http://localhost:5055/webhook"

## credentials.yml: 
Contiene las credenciales para conectar el bot con diferentes plataformas de mensajería y voz. Por ejemplo:

rasa:
  url: "http://localhost:5002/api"
actions.py: Aquí se implementan acciones personalizadas, por ejemplo, responder con el número de teléfono de un usuario basado en su nombre.

5. # Componentes Clave en el Código
Acciones personalizadas: Estas acciones son funciones que se ejecutan cuando se necesita realizar algo más que solo enviar un mensaje (por ejemplo, consultar una base de datos o ejecutar un cálculo). En el código anterior, las acciones personalizadas están implementadas en la clase ActionHelloWorld.

Ejemplo de una acción personalizada:

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_your_num"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(tracker.get_slot('num'))
        return []

# Formularios: 
Los formularios permiten que el bot recoja información del usuario de manera estructurada. En el código proporcionado, la clase ActionFormInfo maneja un formulario para recoger el nombre y la marca preferida de los usuarios.

Ejemplo de un formulario:

class ActionFormInfo(FormAction):
    def name(self) -> Text:
        return "form_info"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["NAME", "BRAND"]

6. # Integración con Canales de Comunicación
Rasa se puede integrar con diferentes plataformas de mensajería como Facebook, Slack, y REST API para interactuar con los usuarios. Los comentarios en los archivos credentials.yml y endpoints.yml proporcionan los detalles para configurar estas integraciones.

# Resumen del Proyecto
Un proyecto con Rasa para atención al cliente en el sector de telecomunicaciones puede incluir varios componentes, como:

Procesamiento de lenguaje natural (NLP) para entender las intenciones de los usuarios.
Acciones personalizadas para realizar tareas específicas, como acceder a una base de datos de clientes.
Integración de voz para permitir que los usuarios interactúen con el bot usando su voz.
Formularios para obtener información del usuario de manera estructurada.
Integración con diferentes canales como REST, Slack o Facebook.
Este tipo de bot permite automatizar la atención al cliente en el sector de telecomunicaciones, manejando consultas, problemas de red, preguntas sobre SIMs 4G, entre otros temas.