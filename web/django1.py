# mi_app/views.py

from django.http import HttpResponse

# Vista simple que responde con un mensaje
def home(request):
    return HttpResponse("¡Hola, Mundo con Django!")
