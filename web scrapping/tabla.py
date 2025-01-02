import requests
from bs4 import BeautifulSoup

# URL de la página que deseas scrapear
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'

# Realizar la solicitud HTTP
response = requests.get(url)

# Parsear el contenido HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar la tabla
table = soup.find('table', {'class': 'wikitable'})

# Extraer todas las filas de la tabla
rows = table.find_all('tr')

# Iterar sobre las filas y obtener los datos
for row in rows:
    columns = row.find_all('td')
    if columns:
        country = columns[1].get_text(strip=True)
        gdp = columns[2].get_text(strip=True)
        print(f'País: {country}, GDP: {gdp}')