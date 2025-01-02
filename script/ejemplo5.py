import requests
from bs4 import BeautifulSoup
import csv

# URL del sitio web
url = "https://example.com"

# Obtener el contenido de la página
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extraer datos (ejemplo: obtener todos los encabezados de la página)
headers = [header.text.strip() for header in soup.find_all('h1')]

# Guardar los datos en un archivo CSV
with open("encabezados.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Encabezado"])  # Escribir encabezado de la columna
    for header in headers:
        writer.writerow([header])

print("Datos extraídos y guardados en encabezados.csv")
