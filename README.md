# 📋 Sistema de Gerenciamento de Reclamações

Aplicação de linha de comando em **Python** para registrar e gerenciar reclamações, com um menu interativo e operações de CRUD (criar, listar, pesquisar, atualizar e remover).

## ✨ Funcionalidades

- 📄 Listar todas as reclamações registradas
- ➕ Adicionar uma nova reclamação
- 🔍 Pesquisar uma reclamação pelo código
- ✏️ Atualizar uma reclamação existente
- 🗑️ Remover uma reclamação pelo código
- 🔢 Exibir a quantidade total de reclamações cadastradas

## 🗂️ Estrutura do projeto

```
projeto-ouvidoria-python/
├── backend.py    # Funções que manipulam a lista de reclamações
└── frontend.py   # Menu interativo e execução do programa
```

- **`backend.py`**: contém a lógica do sistema (`listar_reclamacoes`, `adicionar_reclamacao`, `pesquisar_reclamacao`, `atualizar_reclamacao`, `remover_reclamacao` e `obter_quantidade_reclamacoes`).
- **`frontend.py`**: importa o backend e exibe o menu para o usuário interagir pelo terminal.

## 🚀 Como executar

**Pré-requisito:** [Python 3](https://www.python.org/downloads/) instalado.

1. Clone o repositório:
   ```bash
   git clone https://github.com/mariana-developer/NOME-DO-REPOSITORIO.git
   ```
2. Entre na pasta do projeto:
   ```bash
   cd NOME-DO-REPOSITORIO
   ```
3. Execute o programa:
   ```bash
   python frontend.py
   ```

## 🖥️ Exemplo de uso

```
------------ Menu ------------
1) Listar reclamações registradas,
2) Adicionar uma nova reclamação,
3) Pesquisar uma reclamação pelo código,
4) Atualizar uma reclamação existente,
5) Remover uma reclamação pelo código,
6) Mostrar a quantidade de reclamações cadastradas,
7) Sair.
Digite a sua opção:
```

> ⚠️ As reclamações ficam guardadas apenas em memória: ao encerrar o programa, os dados são perdidos.

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 👩‍💻 Integrantes do grupo

- Nicole de Lucena Macedo
- Mariana Araujo Azevedo
- Rayanne Varelo Alves Caldas
- Clara Lourdes Cunha Marques

## 🎓 Contexto

Projeto acadêmico desenvolvido no curso de Sistemas de Informação da **UNIFACISA**.