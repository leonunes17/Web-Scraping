# Readme: Script de Download de Arquivos PDF de um Site

Este é um script Python simples que baixa arquivos PDF de um site e os compacta em um arquivo ZIP. Ele usa as bibliotecas `requests` para fazer requisições HTTP, `BeautifulSoup` para fazer parsing do HTML e extrair os links relevantes, e `zipfile` para criar o arquivo ZIP.

## Requisitos

- Python 3.x
- Bibliotecas Python: `requests`, `BeautifulSoup`

## Como usar

1. Certifique-se de ter o Python instalado em seu ambiente.

2. Instale as dependências necessárias executando o seguinte comando:
    ```
    pip install requests beautifulsoup4
    ```

3. Execute o script Python.

    ```bash
    python script.py
    ```

## Explicação do Script

O script é composto por duas funções principais:

### Função `download_file(link, local)`

Esta função faz o download de um arquivo do URL fornecido e salva-o localmente no local especificado. Ele faz uso da biblioteca `requests` para fazer a solicitação HTTP e salva o arquivo em chunks de 10 KB para economizar memória.

### Função `zip_file(nome_zip, files)`

Esta função cria um arquivo ZIP contendo uma lista de arquivos fornecida. Ele utiliza a biblioteca `zipfile` do Python para criar o arquivo ZIP e escrever os arquivos dentro dele.

O script também define uma URL de onde os arquivos PDF serão baixados e cria uma lista para armazenar os nomes dos arquivos PDF baixados.

Ele faz uma solicitação HTTP para a URL definida e, se a solicitação for bem-sucedida (código de status 200), utiliza `BeautifulSoup` para filtrar os links relevantes que apontam para arquivos PDF. Em seguida, itera sobre os links filtrados, extrai o URL e o nome do arquivo do link, adiciona o nome do arquivo à lista e chama a função `download_file()` para baixar o arquivo PDF.

Por fim, chama a função `zip_file()` para criar um arquivo ZIP contendo todos os arquivos PDF baixados.

## Notas

Este script foi criado para fins educacionais e pode precisar ser adaptado para atender às necessidades específicas do seu projeto. Certifique-se de obedecer às leis de direitos autorais ao fazer o download e usar conteúdo da web.
