# Sistema de Estoque 📦

Este projeto consiste em um sistema de controle de estoque desenvolvido para fins acadêmicos, utilizando as tecnologias **HTML**, **Tailwind CSS**, **Flask** e **Python**. O sistema permite o gerenciamento de produtos em estoque, com funcionalidades para adicionar, editar, excluir e visualizar produtos.

## Tecnologias Utilizadas 🛠️

- **HTML**: Estruturação das páginas da aplicação.
- **Tailwind CSS**: Framework CSS para estilização rápida e responsiva.
- **Flask**: Framework Python para desenvolvimento web.
- **Python**: Linguagem utilizada para lógica de programação e manipulação de dados.
- **POO (Programação Orientada a Objetos)**: Estruturação do código utilizando conceitos de classes e objetos.

## Funcionalidades Principais ⚙️

- **Cadastro de Produtos** 📝: Permite adicionar novos produtos ao estoque, com nome, descrição, quantidade e preço.
- **Edição de Produtos** ✏️: Permite editar as informações dos produtos existentes.
- **Exclusão de Produtos** 🗑️: Permite remover produtos do estoque.
- **Listagem de Produtos** 📋: Exibe todos os produtos registrados no estoque com a opção de visualização detalhada.

## Como Rodar o Projeto 🚀

### Pré-requisitos 📋

1. Python 3.x instalado na sua máquina.
2. Gerenciador de pacotes `pip` instalado.

### Instalação 🛠️

1. Clone o repositório:

```bash
git clone https://github.com/Projeto_POO_Sistema_de_Estoque.git
cd sistema-estoque
pip install -r requirements.txt
pip install flask
python app.py



sistema-estoque/ 📂
│
├── app.py                 # Arquivo principal da aplicação Flask
├── requirements.txt       # Dependências do projeto
├── static/                # Arquivos estáticos (CSS, JS, imagens)
│   └── styles.css         # Estilos personalizados
├── templates/             # Arquivos HTML da aplicação
│   ├── index.html         # Página principal (listagem de produtos)
│   ├── add_product.html   # Página de cadastro de produtos
│   └── edit_product.html  # Página de edição de produtos
└── models/                # Lógica de classes e manipulação de dados
    └── product.py         # Classe que representa um produto

