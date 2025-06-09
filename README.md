# Automobil 🚗

## Instalação

Tenha o **poetry** instalado localmente.

Para instruções de instalação, visite: [Documentação Oficial do Poetry](https://python-poetry.org/docs/#installation)

Siga os passos abaixo:

1.  **Configure as Variáveis de Ambiente:**
    *   O agente utiliza a API do Gemini (atualmente testado com Gemini Flash 2.0).
    *   Na pasta raiz do projeto (`automobil/`), crie um arquivo chamado `.env`.
    *   Adicione o seguinte conteúdo, substituindo `sua_chave_aqui` pela sua chave API:
    *   Declare a varíável também no terminal
      ```bash
      export GEMINI_API_KEY=
      ```

    ```env
    DATABASE_URL=sqlite:///database.db
    GEMINI_API_KEY=sua_chave_aqui
    ```

2.  **Clone o Repositório e Acesse a Pasta:**

    ```bash
    git clone https://github.com/ricardotenv/automobil.git
    cd automobil
    ```

3.  **Instale as Dependências:**
    Com o Poetry instalado e dentro da pasta do projeto, execute:

    ```bash
    poetry shell
    poetry install
    ```

4.  **Popule o Banco de Dados:**
    Este comando cria as tabelas e insere dados iniciais, se necessário.

    ```bash
    poetry run populate
    ```
    > **Nota:** Se o arquivo de banco de dados `database.db` já existir com dados, este comando não o sobrescreverá. Para gerar novos dados do zero, apague o arquivo `database.db` antes de executar este passo.

5.  **Inicie a Aplicação CLI:**

    ```bash
    poetry run python chat.py
    ```
    A aplicação gerenciará automaticamente o **MCP Server** e a conexão do cliente.

---

## Resumo rápido

Para quem já clonou o projeto e precisa apenas rodar:

1. **Configurar:** Crie o arquivo `.env` com sua `GEMINI_API_KEY`.
   ```env
   DATABASE_URL=sqlite:///database.db
   GEMINI_API_KEY=sua_chave_aqui
   ```
2. **Instalar:** `poetry install`
3. **Popular:** `poetry run populate`
4. **Executar:** `poetry run python chat.py`
