import requests
import json
from requests.auth import HTTPBasicAuth
from decouple import config

# Obtenção das variáveis de ambiente do arquivo .env
CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')
REDIRECT_URI = config('REDIRECT_URI')
API_URL = config('API_URL')

# Função para obter o código de autorização
def get_authorization_code():
    url = f"{API_URL}/oauth/grant-code"

    payload = json.dumps({
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "extra_info": {
            "idCliente": 1234,
            "tipoCliente": "CD"
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_data = response.json()
    print(response_data)
    # Extrair o código da resposta
    authorization_code = response_data.get('redirect_uri').split('code=')[1]
    return authorization_code

# Função para obter o token de acesso usando o código de autorização
def get_access_token(authorization_code):
    url = f"{API_URL}/oauth/access-token"

    payload = f'grant_type=authorization_code&code={authorization_code}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'client_id': CLIENT_ID
    }

    # Autenticação Basic Auth com as credenciais fornecidas
    auth = HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

    response = requests.request("POST", url, headers=headers, data=payload, auth=auth)
    response_data = response.json()
    
    # Extrair o token de acesso da resposta
    access_token = response_data.get('access_token')
    return access_token

# Função para obter os detalhes do produto utilizando o código do formulário
def get_product_details(product_code, access_token):
    url = f"{API_URL}/instrucoes-gerais-hospitais/v1/produtos?produtos={product_code}"

    headers = {
        'client_id': CLIENT_ID,
        'access_token': access_token
    }
    
    response = requests.request("GET", url, headers=headers)
    print(response)
    product_details = response.json()
    return product_details
