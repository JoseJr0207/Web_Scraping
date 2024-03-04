from bs4 import BeautifulSoup
import requests

def scrape_website(url):
    resposta = requests.get(url)
    if resposta.status_code == 200:
        conteudo = resposta.content
        soup = BeautifulSoup(conteudo, 'html.parser')
        links = soup.find_all('a')
        return [link.get_text() for link in links]
    else:
        print("Não foi possível acessar a página.")
        return []
