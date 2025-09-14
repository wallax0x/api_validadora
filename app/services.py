# Arquivo: app/services.py
import requests

def consultar_cep(cep: str):
    try:
        # Limpa o CEP para conter apenas números
        cep_limpo = "".join(filter(str.isdigit, cep))
        if len(cep_limpo) != 8:
            return {"erro": "Formato de CEP inválido."}

        url = f"https://brasilapi.com.br/api/cep/v2/{cep_limpo}"
        response = requests.get(url, timeout=5) # Timeout de 5 segundos
        response.raise_for_status() # Lança erro para status 4xx ou 5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"erro": f"Não foi possível consultar o CEP: {e}"}