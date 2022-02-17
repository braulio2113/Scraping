import requests
from bs4 import BeautifulSoup

headers = {
    "user-agente":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36"
 } 

url = "https://www.animalpolitico.com/" 

respuesta = requests.get(url, headers = headers)
soup = BeautifulSoup(respuesta.text, features="lxml") 

contenedor_de_noticias = soup.find(class_="ap_desktop_first_extra_notes")
lista_de_noticias = contenedor_de_noticias.find_all('a', class_="ap_note_link")

for noticia in lista_de_noticias:
    print(noticia['href'])
    print(noticia.find('div', class_='ap_home_extra_data_title').text)
    print()