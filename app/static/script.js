// script.js

// Pega os elementos do HTML
const input = document.getElementById('dadoInput');
const select = document.getElementById('tipoSelect');
const button = document.getElementById('validarBtn');
const resultadoDiv = document.getElementById('resultado');

// Adiciona um evento de clique no botão
button.addEventListener('click', async () => {
    const tipo = select.value;
    const valor = input.value;
    
    let url = '';
    let options = {};

    // Monta a URL e as opções da requisição baseado no tipo selecionado
    if (tipo === 'cpf') {
        url = 'http://127.0.0.1:5000/api/v1/cpf/validar'; // URL da sua API Flask
        options = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cpf: valor })
        };
    } else if (tipo === 'cep') {
        url = `http://127.0.0.1:5000/api/v1/cep/${valor}`;
        options = { method: 'GET' };
    }
    // Adicionar lógica para CNPJ aqui...

    // Faz a chamada para a API
    try {
        const response = await fetch(url, options);
        const data = await response.json();

        // Exibe o resultado formatado na tela
        resultadoDiv.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        resultadoDiv.textContent = `Erro ao conectar com a API: ${error}`;
    }
});