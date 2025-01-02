import requests
from bs4 import BeautifulSoup

# URL de la página que deseas scrapear
url = 'https://www.wikipedia.org/'

# Realizar la solicitud HTTP
response = requests.get(url)

# Parsear el contenido HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Obtener el título de la página
title = soup.title.string

print(f"El título de la página es: {title}")
