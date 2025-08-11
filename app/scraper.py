import requests
from bs4 import BeautifulSoup

def buscar_noticias(termo):

    url = "https://g1.globo.com/tecnologia/"
    r = requests.get(url)

    if r.status_code != 200:
        return []
    
    soup = BeautifulSoup(r.text, 'html.parser')
    
    artigos = soup.find_all('div', class_="feed-post-body")
    resultados = []
    for artigo in artigos:
        titulo = artigo.find('div', class_='_evt').text
        resumo = artigo.find('div', class_='feed-post-body-resumo').text
        link = artigo.find('a')['href']

        if termo.lower() in titulo.lower() or termo.lower() in resumo.lower():
            resultados.append({"titulo": titulo, "resumo": resumo, "link": link})
    if not resultados:
        print(f"Não foi encontrado nada relacionado a '{termo}'")
        
    
        
    return resultados


for noticia in buscar_noticias("trump"):
    print(noticia)