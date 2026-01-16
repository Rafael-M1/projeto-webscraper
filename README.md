# Webscraper

Projeto em Python utilizando Selenium para acessar o site e extrair automaticamente tags html.

------------------------------------------------------------------------

## 📋 Requisitos

Antes de iniciar, certifique-se de ter instalado:

-   Python 3.10 ou superior
-   Google Chrome atualizado
-   Git (opcional, recomendado)

Verifique:

``` bash
python --version
```

------------------------------------------------------------------------

## 📦 Instalação

### 1️⃣ Clonar o repositório

``` bash
git clone https://github.com/Rafael-M1/projeto-webscraper.git
cd webscraper
```

------------------------------------------------------------------------

### 2️⃣ Criar ambiente virtual

``` bash
python -m venv venv
```

------------------------------------------------------------------------

### 3️⃣ Ativar ambiente virtual

#### Windows (PowerShell / CMD)

``` bash
venv\Scripts\activate
```

#### Linux / Mac

``` bash
source venv/bin/activate
```

------------------------------------------------------------------------

### 4️⃣ Instalar dependências

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

### 5️⃣ Configuração do projeto

Copie o arquivo de exemplo:

#### Linux / Mac

``` bash
cp config_example.py config.py
```

#### Windows (PowerShell / CMD)

``` powershell
copy config_example.py config.py
```

Em seguida, edite o arquivo `config.py` e configure as variáveis
necessárias.

------------------------------------------------------------------------

## ▶ Execução

Execute o projeto com o comando:

``` bash
python projeto.py
```

------------------------------------------------------------------------

## ⚙ Estrutura do Projeto

    webscraper/
    │
    ├── projeto.py
    ├── driver_factory.py
    ├── decorators.py
    ├── config.py
    ├── config_example.py
    ├── requirements.txt
    ├── .gitignore
    └── venv/

------------------------------------------------------------------------

## 🧪 Modo Debug

Caso o modo DEBUG esteja ativado no arquivo `config.py`, o sistema
exibirá:

-   Tempo de execução das funções
-   Informações adicionais de log

------------------------------------------------------------------------

## 🚀 Tecnologias Utilizadas

-   Python
-   Selenium
-   WebDriver Manager
-   Chrome WebDriver

------------------------------------------------------------------------

## 🛠 Solução de Problemas

### Chrome não abre ou erro de driver

Certifique-se que:

-   O Google Chrome está atualizado
-   O ambiente virtual está ativo
-   As dependências foram instaladas corretamente

Reinstale dependências se necessário:

``` bash
pip install --upgrade selenium webdriver-manager
```

------------------------------------------------------------------------

## 📌 Observações

-   O ChromeDriver é gerenciado automaticamente pelo WebDriver Manager.
-   Não é necessário baixar o driver manualmente.
-   O arquivo `.env` ou `config.py` não deve ser versionado.

------------------------------------------------------------------------

## 📄 Licença

Projeto para fins educacionais e automação interna.

