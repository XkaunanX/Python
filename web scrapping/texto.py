import requests
from bs4 import BeautifulSoup

# URL de la página que deseas scrapear
url = 'https://www.wikipedia.org/'

# Realizar la solicitud HTTP
response = requests.get(url)

# Parsear el contenido HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar el primer párrafo (<p>)
paragraph = soup.find('p')

# Imprimir el texto del párrafo
print(paragraph.get_text())