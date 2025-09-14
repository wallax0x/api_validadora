# app/routes.py
from flask import Blueprint, jsonify, request
from . import validators # Importa o novo módulo de validação
from . import services

bp = Blueprint('api', __name__, url_prefix='/api/v1')

@bp.route('/')
def health_check():
    """
    Endpoint para verificar se a API está online.
    """
    return jsonify({
        "status": "online",
        "message": "API Validadora no ar!"
    })

# --- NOVA ROTA ABAIXO ---

@bp.route('/cpf/validar', methods=['POST'])
def validar_cpf():
    """
    Recebe um CPF via JSON e valida.
    Exemplo de corpo da requisição: { "cpf": "123.456.789-00" }
    """
    # Pega os dados JSON enviados na requisição
    data = request.get_json()

    # Verifica se o JSON foi enviado e se a chave "cpf" existe
    if not data or 'cpf' not in data:
        return jsonify({
            "status": "erro",
            "motivo": "JSON inválido ou chave 'cpf' não encontrada."
        }), 400 # 400 Bad Request

    cpf_para_validar = data['cpf']

    # Chama nossa função de validação
    if validators.is_cpf_valid(cpf_para_validar):
        return jsonify({
            "status": "valido",
            "cpf": cpf_para_validar
        })
    else:
        return jsonify({
            "status": "invalido",
            "cpf": cpf_para_validar
        })


@bp.route('/cnpj/validar', methods=['POST'])
def validar_cnpj():
    data = request.get_json()
    if not data or 'cnpj' not in data:
        return jsonify({
            "status": "erro",
            "motivo": "JSON inválido ou chave 'cnpj' não encontrada."
        }), 400

    cnpj_para_validar = data['cnpj']

    if validators.is_cnpj_valid(cnpj_para_validar):
        return jsonify({"status": "valido", "cnpj": cnpj_para_validar})
    else:
        return jsonify({"status": "invalido", "cnpj": cnpj_para_validar})


@bp.route('/cep/<string:cep>', methods=['GET'])
def consultar_endereco_cep(cep):
    resultado = services.consultar_cep(cep)
    if "erro" in resultado:
        return jsonify(resultado), 404 # Not Found ou Bad Request
    return jsonify(resultado)