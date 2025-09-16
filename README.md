# API Validadora de Dados Brasileiros 🇧🇷

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=yellow) ![Flask](https://img.shields.io/badge/Flask-2.2%2B-black?logo=flask) ![Status](https://img.shields.io/badge/status-concluído-green)

Uma API REST simples e robusta construída com Python e Flask para validar dados comuns do Brasil, como CPF e CNPJ, e para consultar endereços a partir de um CEP. Este projeto foi desenvolvido para demonstrar habilidades em desenvolvimento back-end, criação de APIs e integração com serviços de terceiros.

## ✨ Funcionalidades

* **Validação de CPF:** Verifica se um número de CPF é matematicamente válido, incluindo a checagem dos dígitos verificadores.
* **Validação de CNPJ:** Verifica se um número de CNPJ é válido de acordo com o algoritmo oficial.
* **Consulta de CEP:** Integra-se com a [BrasilAPI](https://brasilapi.com.br/) para retornar informações de endereço completas a partir de um CEP.

## 🛠️ Tecnologias Utilizadas

* **[Python](https://www.python.org/)**: Linguagem principal do projeto.
* **[Flask](https://flask.palletsprojects.com/)**: Micro-framework web para a criação da API.
* **[Requests](https://requests.readthedocs.io/en/latest/)**: Biblioteca para fazer chamadas HTTP para a API externa de CEP.
* **[Postman](https://www.postman.com/)**: Ferramenta utilizada para testar os endpoints da API durante o desenvolvimento.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação localmente.

**1. Clone o repositório:**
```bash
git clone https://github.com/wallax0x/api_validadora.git
cd api_validadora
```

**2. Crie e ative um ambiente virtual:**
* No Windows:
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
* No macOS/Linux:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```
*(Observação: você precisará criar o arquivo `requirements.txt` com o comando `pip freeze > requirements.txt`)*

**4. Inicie o servidor Flask:**
```bash
python run.py
```
A API estará rodando em `http://127.0.0.1:5000`.

## 📖 Endpoints da API

Aqui estão os endpoints disponíveis e como usá-los.

---

### Validação de CPF

* **Método:** `POST`
* **URL:** `/api/v1/cpf/validar`
* **Corpo (Body):**
    ```json
    {
        "cpf": "111.444.777-35"
    }
    ```
* **Resposta de Sucesso (200 OK):**
    ```json
    {
        "status": "valido",
        "cpf": "111.444.777-35"
    }
    ```

---

### Validação de CNPJ

* **Método:** `POST`
* **URL:** `/api/v1/cnpj/validar`
* **Corpo (Body):**
    ```json
    {
        "cnpj": "00.000.000/0001-91"
    }
    ```
* **Resposta de Sucesso (200 OK):**
    ```json
    {
        "status": "valido",
        "cnpj": "00.000.000/0001-91"
    }
    ```

---

### Consulta de CEP

* **Método:** `GET`
* **URL:** `/api/v1/cep/<cep>`
* **Exemplo de Uso:**
    `http://127.0.0.1:5000/api/v1/cep/01001000`
* **Resposta de Sucesso (200 OK):**
    ```json
    {
      "cep": "01001000",
      "state": "SP",
      "city": "São Paulo",
      "neighborhood": "Sé",
      "street": "Praça da Sé",
      "service": "open-cep"
    }
    ```
