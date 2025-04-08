# Projetos da Faculdade
 Repositorio para projetos e exercicios da faculdade

# README - Sistema de Ouvidoria

## 📝 Descrição do Projeto

Este projeto é um sistema de ouvidoria desenvolvido em Python, que permite aos usuários cadastrar, visualizar, pesquisar e excluir manifestações (sugestões, elogios ou reclamações). O sistema está integrado a um banco de dados MySQL para armazenamento persistente das informações.

## ✨ Funcionalidades

- **Cadastro de Manifestações**: Registre novas manifestações com nota (1-5), tipo (Sugestão, Elogio, Reclamação) e descrição.
- **Listagem Completa**: Visualize todas as manifestações cadastradas.
- **Filtro por Tipo**: Liste manifestações específicas por tipo (Sugestão, Elogio ou Reclamação).
- **Pesquisa por Código**: Encontre uma manifestação específica usando seu código único.
- **Exclusão**: Remova manifestações do sistema quando necessário.
- **Estatísticas**: Veja a quantidade total de manifestações cadastradas.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **MySQL**: Banco de dados para armazenamento das manifestações.
- **Bibliotecas**:
  - `mysql.connector`: Para conexão e interação com o banco de dados MySQL.

## ⚙️ Configuração do Ambiente

1. **Pré-requisitos**:
   - Python 3.x instalado.
   - Servidor MySQL (local ou remoto).

2. **Instalação**:
   - Clone o repositório:
     ```bash
     git clone [https://github.com/Elian-BSiqueira/Projetos_Faculdade/tree/9f1acafd9a809e98e11efdcf5ec284bd9a333f3c/projetoOuvidoria]
     ```
   - Instale as dependências:
     ```bash
     pip install mysql-connector-python
     ```

3. **Configuração do Banco de Dados**:
   - Crie um banco de dados MySQL usando o Dump disponibilizado
   - 2. Usando o MySQL Workbench (Interface Gráfica)
Abra o MySQL Workbench e conecte-se ao seu servidor

No menu superior, selecione Server > Data Import

Selecione "Import from Self-Contained File"

Navegue até o arquivo dump.sql baixado

Selecione o banco de dados de destino ou crie um novo

Clique em Start Import
   - Configure as credenciais no arquivo em um novo arquivo chamado`config.py`:
     ```python
     host = "seu_host"
     user = "seu_usuario"
     password = "sua_senha"
     database = "nome_do_banco_de_dados"
     ```
   - Certifique-se de que a tabela `manifestacoes` existe no banco de dados.

