import requests
import pandas as pd
import io
from datetime import date, datetime, timedelta
from connection_pool import ConnectionPool
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()

tabela  = pd.DataFrame()

for i in range(0,365): 
    dataInicio = str(date.today() - timedelta(days=i))

    url = 

    payload={}
    headers = {
      'Authorization': 'Basic YXRsYXNmb2dvZXMtYXBpOnNyOXE1NUo4Z1FYVVQycU0='
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify = False)

    dados = (response.text)
    dados = dados.encode('utf-8')
    binaryStream = io.BytesIO(dados)
    dados = pd.read_csv(binaryStream)
    tabela = tabela.append(dados)
    
    del response
    del dados
    del binaryStream

print(tabela)