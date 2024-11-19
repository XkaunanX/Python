import requests
from bs4 import BeautifulSoup

# URL de la página que deseas scrapear
url = 'https://www.wikipedia.org/'

# Realizar la solicitud HTTP
response = requests.get(url)

# Parsear el contenido HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar todos los enlaces
links = soup.find_all('a')

# Imprimir los enlaces
for link in links:
    print(link.get('href'))