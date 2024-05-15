import requests
from bs4 import BeautifulSoup as bs
import re


def web_crawler( url ):
    elements_h1_and_p = {}

    # request
    response = requests.get(url)
    # obtener texto plano y dárselo a BeautifulSoup
    soup = bs(response.text, 'html.parser')  
    # buscamos todos los enlaces <a>
    enlaces = soup.find_all("a", href=re.compile("^https://"))

    for a in enlaces:
        # Obtenemos el atributo href
        a_url = a.get("href")
        if a_url not in elements_h1_and_p:
            elements_h1_and_p[a_url] = []

        # request de cada una de las url
        response_a = requests.get(a_url)
        # convertirlo en html
        soup_a = bs(response_a.text, 'html.parser')
        # obtenemos los elementos h1 y p
        h1_tags = soup_a.find_all('h1')
        p_tags = soup_a.find_all('p')

        # guardamos los elementos en el diccionario
        elements_h1_and_p[a_url].extend(h1_tags) 
        elements_h1_and_p[a_url].extend(p_tags)
        
    return elements_h1_and_p




print(web_crawler('https://commerce.nearform.com/open-source/victory/docs'))
