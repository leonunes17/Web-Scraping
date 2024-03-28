import os
import requests
from bs4 import BeautifulSoup, SoupStrainer
import re
import zipfile

def download_file(link, local):
    response = requests.get(link, stream=True) 
    if response.status_code == 200:
        with open(local, mode='wb') as file:
            for chunk in response.iter_content(chunk_size=10240): #10kb
                if(chunk):
                    file.write(chunk)

def zip_file(nome_zip, files):
    with zipfile.ZipFile(nome_zip, 'w') as zipf: 
        for arquivo in files:
            zipf.write(arquivo, os.path.basename(arquivo))

#definindo previamente uma variável para guardar a url do site
LINK = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

#definindo uma lista onde será adicionado os arquivos
list_files = []

response = requests.get(LINK)

if response.status_code == 200:
    filter_soup = SoupStrainer('a', href=re.compile(r'Anexo.*\.pdf$'))  #filtro para extrair somente links relevantes

    soup = BeautifulSoup(response.text, 'html.parser', parse_only=filter_soup) 
        
    for link in soup:  
        href = link.get('href') #atribuindo os atributos de href das tags em uma variável 'href'
        destino = link.string + '.pdf' 
        list_files.append(destino)
        download_file(href, destino)

    zip_file('Anexos.zip', list_files)
