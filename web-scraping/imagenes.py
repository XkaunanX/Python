import requests
from bs4 import BeautifulSoup

# URL de la página que deseas scrapear
url = 'https://www.wikipedia.org/'

# Realizar la solicitud HTTP
response = requests.get(url)

# Parsear el contenido HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar todas las imágenes
images = soup.find_all('img')

# Imprimir las URLs de las imágenes
for image in images:
    img_url = image.get('src')
    print(f'URL de la imagen: {img_url}')