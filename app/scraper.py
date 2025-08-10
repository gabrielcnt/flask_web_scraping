import requests
from bs4 import BeautifulSoup

def buscar_noticias(termo):

    url = "https://g1.globo.com/tecnologia/"