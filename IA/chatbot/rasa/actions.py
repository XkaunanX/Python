# Este archivo contiene tus acciones personalizadas que se pueden usar para ejecutar
# código Python personalizado.
#
# Consulta esta guía sobre cómo implementar estas acciones:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# Este es un ejemplo simple de una acción personalizada que dice "¡Hola Mundo!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

detalles = {
    'ashish': '+91 8209829808',
    'innovate': '+91 9413995563'
}


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_your_num"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(text="¡Hola Mundo!")
        print(tracker.get_slot('num'))
        # dispatcher.utter_template('utter_your_num', tracker, number=detalles[str(tracker.get_slot('NAME')).lower()])
        return []


class ActionFormInfo(FormAction):
    def name(self) -> Text:
        """Identificador único del formulario"""

        return "form_info"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """Una lista de los slots requeridos que el formulario debe llenar"""

        return ["NAME", "BRAND"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define lo que el formulario debe hacer
            después de que todos los slots requeridos estén llenos"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit", name=tracker.get_slot('NAME'),
                                 headset=tracker.get_slot('BRAND'))
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """Un diccionario para mapear los slots requeridos a
            - una entidad extraída
            - pares de intentos: valor
            - un mensaje completo
            o una lista de ellos, donde se seleccionará la primera coincidencia"""

        return {
            "name": [self.from_entity(entity="NAME", intent='my_name_is'),
                     self.from_text()],
            "headset": [self.from_entity(entity="BRAND", intent="headset"),
                        self.from_text()],
        }

    @staticmethod
    def brand_db() -> List[Text]:
        """Base de datos de marcas de auriculares soportadas"""

        return [
            "samsung",
            "One plus",
            "I-phone",
        ]

    def validate_brand(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validar el valor de la marca."""
        print(value)
        if value.lower() in self.cuisine_db():
            # validación exitosa, establece el valor del slot "BRAND" a el valor
            return {"BRAND": value}
        else:
            print(value)
            dispatcher.utter_message(template="utter_wrong_value")
            # validación fallida, establece este slot como None, lo que significa que
            # se le pedirá al usuario nuevamente que ingrese el valor
            return {"BRAND": None}