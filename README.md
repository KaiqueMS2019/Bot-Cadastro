# Automação RPA Web + Desktop

Automação RPA desenvolvida em Python para execução de um fluxo integrado entre automação Web e Desktop.

O projeto realiza a geração de um comprador fictício, extração de um catálogo de produtos, persistência dos dados em CSV e cadastro dessas informações em uma aplicação desktop utilizando reconhecimento de imagem.

---

## 1. Objetivo

O projeto foi desenvolvido para atender a um fluxo de automação híbrida envolvendo:

* Automação Web
* Extração e transformação de dados
* Persistência em arquivos CSV
* Automação Desktop
* Reconhecimento de imagem
* Registro de logs
* Geração de evidências da execução

O fluxo completo é:

```text
FakeNameGenerator
        |
        v
Geração do comprador
        |
        v
buyer.csv
        |
        v
SauceDemo
        |
        v
Extração do catálogo
        |
        v
products.csv
        |
        v
Fakturama
        |
        +----> Cadastro do comprador
        |
        +----> Cadastro dos produtos
        |
        v
Evidências + Logs
```

---

## 2. Tecnologias utilizadas

* **Python 3.11**
* **Selenium**
* **BotCity Desktop**
* **CSV**
* **Pytest**
* **python-dotenv**
* **Git**

### Automação Web

A automação Web utiliza **Selenium**, responsável por:

* Acessar o FakeNameGenerator
* Gerar e extrair os dados do comprador
* Acessar o SauceDemo
* Realizar o login
* Percorrer o catálogo
* Extrair nome, descrição e preço dos produtos

### Automação Desktop

A automação Desktop utiliza **BotCity Desktop**, responsável por:

* Abrir o Fakturama
* Localizar elementos através de reconhecimento de imagem
* Preencher os campos
* Navegar entre os campos utilizando teclado
* Salvar os cadastros

---

## 3. Por que Selenium na Web e BotCity no Desktop?

O projeto utiliza cada ferramenta na parte em que ela apresenta maior aderência ao fluxo.

### Selenium

O Selenium trabalha diretamente com o DOM da página, permitindo localizar elementos através de:

* ID
* Classe
* CSS Selector
* Outros seletores disponíveis no HTML

Isso torna a extração dos dados do FakeNameGenerator e SauceDemo mais estruturada.

### BotCity Desktop

O Fakturama é uma aplicação instalada localmente.

Nesse cenário, a automação utiliza reconhecimento de imagem para localizar os elementos da interface, sem depender de coordenadas fixas da tela.

Essa abordagem permite que o fluxo seja baseado nos elementos visuais cadastrados nos assets.

---

## 4. Estrutura do projeto

```text
C:\Bot_cadastro
│
├── app
│   ├── __init__.py
│   └── main.py
│
├── domain
│   ├── __init__.py
│   ├── models.py
│   └── exceptions.py
│
├── web
│   ├── __init__.py
│   ├── identity_generator.py
│   └── extract_sauce_demo.py
│
├── desktop
│   ├── __init__.py
│   ├── fill_out_fakturama.py
│   └── assets
│       ├── New_contact.png
│       ├── first_name.png
│       ├── district.png
│       ├── save_fakturama.png
│       ├── New_product.png
│       ├── number_product.png
│       └── description_product.png
│
├── infrastructure
│   ├── __init__.py
│   ├── csv_repository.py
│   └── logger.py
│
├── data
│
├── results
│
├── tests
│
├── requirements.txt
├── config.py
├── README.md
└── .gitignore
```

---

## 5. Responsabilidade dos diretórios

### `app`

Contém o ponto de entrada da aplicação.

O arquivo `main.py` é responsável por orquestrar todo o fluxo.

```text
Geração do comprador
        ↓
Extração dos produtos
        ↓
Persistência dos dados
        ↓
Cadastro no Fakturama
        ↓
Geração das evidências
```

---

### `domain`

Contém as entidades e regras centrais do projeto.

O arquivo `models.py` define os objetos utilizados pela aplicação:

```text
Buyer
Product
```

O `Buyer` representa o comprador fictício.

O `Product` representa cada produto extraído do catálogo.

O arquivo `exceptions.py` concentra as exceções específicas da automação.

---

### `web`

Contém as automações realizadas em navegador.

#### `identity_generator.py`

Responsável por:

1. Abrir o FakeNameGenerator
2. Gerar a identidade
3. Extrair o nome
4. Extrair o sobrenome
5. Extrair o CEP
6. Criar o objeto `Buyer`

#### `extract_sauce_demo.py`

Responsável por:

1. Abrir o SauceDemo
2. Realizar login
3. Localizar o catálogo
4. Percorrer todos os produtos
5. Extrair:

   * Número
   * Nome
   * Descrição
   * Preço
6. Criar os objetos `Product`

---

### `desktop`

Contém a automação do Fakturama.

#### `fill_out_fakturama.py`

Responsável por:

* Abrir o Fakturama
* Localizar elementos através de imagens
* Cadastrar o comprador
* Cadastrar os produtos
* Salvar os registros
* Gerar screenshots de evidência

---

### `desktop/assets`

Contém as imagens utilizadas pelo BotCity para localizar os elementos da interface.

Exemplo:

```text
New_contact.png
```

Representa o botão utilizado para iniciar o cadastro de um contato.

```text
first_name.png
```

Representa o campo utilizado para localizar o primeiro nome.

As imagens são parte do projeto e devem ser versionadas no Git.

---

### `infrastructure`

Contém componentes responsáveis por infraestrutura da aplicação.

#### `csv_repository.py`

Responsável por:

* Salvar o comprador
* Salvar os produtos
* Ler o comprador
* Ler os produtos

Os arquivos CSV funcionam como uma camada simples de persistência e também como ponte entre as etapas Web e Desktop.

#### `logger.py`

Responsável pela configuração dos logs da aplicação.

Os logs são enviados para:

```text
results/automation.log
```

Também são exibidos no terminal durante a execução.

---

### `data`

Armazena os dados gerados durante a execução.

Exemplo:

```text
data/
├── buyer.csv
└── products.csv
```

Esses arquivos são gerados automaticamente e não precisam ser versionados no Git.

---

### `results`

Armazena as evidências da execução.

Exemplo:

```text
results/
├── automation.log
├── buyer.png
└── products_registeered_registered.png
```

Os arquivos são gerados durante a execução e não precisam ser versionados.

---

## 6. Modelo de dados

### Buyer

O comprador possui:

```text
first_name
last_name
cep
```

Exemplo:

```text
João
Silva
13400-000
```

### Product

Cada produto possui:

```text
number
name
description
price
```

Exemplo:

```text
1
Sauce Labs Backpack
Carry.allTheThings...
29.99
```

---

## 7. Persistência dos dados

Os dados extraídos são armazenados em CSV.

### `buyer.csv`

```csv
first_name,last_name,cep
João,Silva,13400-000
```

### `products.csv`

```csv
number,name,description,price
1,Sauce Labs Backpack,Carry.allTheThings...,29.99
2,Sauce Labs Bike Light,A red light...,9.99
```

A utilização do CSV permite separar as etapas da automação e facilita a validação dos dados antes do cadastro no Desktop.

---

## 8. Fluxo da automação

### Etapa 1 — Geração do comprador

O Selenium acessa o FakeNameGenerator.

A aplicação extrai:

```text
Nome
Sobrenome
CEP
```

Esses dados são transformados em um objeto `Buyer`.

---

### Etapa 2 — Persistência do comprador

O comprador é salvo em:

```text
data/buyer.csv
```

---

### Etapa 3 — Login no SauceDemo

O Selenium acessa:

```text
https://www.saucedemo.com/
```

E realiza o login utilizando as credenciais disponibilizadas para o ambiente de testes.

---

### Etapa 4 — Extração do catálogo

A aplicação percorre todos os produtos disponíveis.

Para cada produto são coletados:

```text
Número
Nome
Descrição
Preço
```

Os dados são transformados em objetos `Product`.

---

### Etapa 5 — Persistência do catálogo

O catálogo completo é salvo em:

```text
data/products.csv
```

---

### Etapa 6 — Abertura do Fakturama

O BotCity inicia a aplicação instalada localmente.

O caminho utilizado é:

```text
C:\Program Files\Fakturama2\Fakturama.exe
```

---

### Etapa 7 — Cadastro do comprador

O BotCity utiliza os assets para localizar os elementos da interface.

O fluxo realiza:

```text
Novo contato
      ↓
Nome
      ↓
Sobrenome
      ↓
CEP
      ↓
Salvar
```

---

### Etapa 8 — Cadastro dos produtos

Para cada produto armazenado em `products.csv`, o BotCity realiza o cadastro.

O fluxo é:

```text
Novo produto
      ↓
Número
      ↓
Nome
      ↓
Descrição
      ↓
Preço
      ↓
Salvar
```

O processo é repetido até que todos os produtos sejam cadastrados.

---

## 9. Reconhecimento de imagem

A automação Desktop não utiliza coordenadas fixas.

Os elementos são registrados através de imagens:

```text
New_contact
first_name
district
save_fakturama
New_product
number_product
description_product
```

O BotCity procura visualmente o elemento na tela e executa a ação quando encontrado.

Isso reduz a dependência de posições específicas da tela.

---

## 10. Logs

A execução gera um arquivo:

```text
results/automation.log
```

Os logs permitem acompanhar as principais etapas da automação.

Exemplo:

```text
2026-09-29 18:00:00 | INFO | Processo iniciado
2026-09-29 18:00:03 | INFO | Comprador gerado
2026-09-29 18:00:08 | INFO | Catálogo extraído
2026-09-29 18:00:10 | INFO | Fakturama iniciado
2026-09-29 18:00:15 | INFO | Comprador cadastrado
2026-09-29 18:00:30 | INFO | Produtos cadastrados
2026-09-29 18:00:32 | INFO | Processo finalizado
```

Os logs ajudam principalmente na identificação de falhas durante a execução.

---

## 11. Evidências

Ao final do processo são geradas evidências da execução.

Exemplo:

```text
results/
├── buyer_registered.png
└── products_registered.png
```

As screenshots permitem comprovar visualmente:

* Cadastro do comprador
* Cadastro dos produtos

---

## 12. Tratamento de recursos

Os navegadores são encerrados após suas respectivas etapas.

O fluxo utiliza `try/finally` para garantir o fechamento dos recursos mesmo quando ocorre uma exceção.

Exemplo conceitual:

```text
Abrir navegador
      ↓
Executar automação
      ↓
Extrair dados
      ↓
Fechar navegador
```

Isso evita deixar processos do navegador abertos após a execução.

---

## 13. Execução do projeto

### 13.1 Pré-requisitos

É necessário possuir:

* Python 3.11
* Google Chrome
* Fakturama instalado
* Git

O Fakturama deve estar instalado no caminho configurado no projeto.

---

### 13.2 Criar ambiente virtual

No terminal:

```bash
python -m venv .venv
```

Ativação no Windows:

```bash
.venv\Scripts\activate
```

---

### 13.3 Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 13.4 Executar

A partir da raiz do projeto:

```bash
python -m app.main
```

O `main.py` é responsável por executar todo o fluxo.

---

## 14. Dependências

O projeto utiliza:

```text
selenium
botcity-framework-core
botcity-framework-base
python-dotenv
pytest
```

As versões utilizadas podem ser encontradas no arquivo:

```text
requirements.txt
```

---

## 15. Testes

Os testes ficam no diretório:

```text
tests/
```

A execução pode ser realizada com:

```bash
pytest
```

Os testes podem validar componentes individuais sem necessariamente executar todo o fluxo Web + Desktop.

---

## 16. Configuração

Configurações específicas da aplicação ficam centralizadas no projeto.

Exemplos de configurações:

```text
Caminho do Fakturama
Diretórios de dados
Diretórios de resultados
URLs utilizadas
```

Informações sensíveis, quando existentes, devem ser armazenadas em variáveis de ambiente e não diretamente no código.

---

## 17. Git e arquivos ignorados

O projeto possui um `.gitignore` para evitar o versionamento de arquivos gerados localmente.

Principais itens ignorados:

```text
.venv/
__pycache__/
*.pyc
.idea/
.env
.pytest_cache/
data/*.csv
results/*.log
results/*.png
```

Os assets utilizados pela automação devem permanecer no repositório:

```text
desktop/assets/
```

Isso é necessário porque as imagens fazem parte da automação Desktop.

---

## 18. Arquivos que devem ser versionados

Devem fazer parte do repositório:

```text
app/
domain/
web/
desktop/
infrastructure/
tests/
desktop/assets/
requirements.txt
config.py
README.md
.gitignore
```

Não devem ser versionados:

```text
.venv/
.idea/
__pycache__/
.env
data/*.csv
results/*.log
results/*.png
```

---

## 19. Decisões técnicas

### Selenium para Web

Foi utilizado Selenium para trabalhar diretamente com os elementos HTML das aplicações Web.

### BotCity para Desktop

Foi utilizado BotCity Desktop para interação com a aplicação instalada localmente através de reconhecimento de imagem.

### CSV como persistência

O CSV foi utilizado como uma solução simples para armazenar e transportar os dados entre as etapas da automação.

### Separação por responsabilidade

O projeto foi dividido em camadas para evitar que toda a lógica ficasse concentrada em um único arquivo.

```text
Web
 ↓
Domain
 ↓
Infrastructure
 ↓
Desktop
```

O `main.py` apenas orquestra essas etapas.

---

## 20. Arquitetura

A arquitetura simplificada do projeto é:

```text
                    ┌─────────────────────┐
                    │      app/main.py    │
                    │    Orquestração     │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              v                v                v
       ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
       │     Web     │  │Infrastructure│  │   Desktop   │
       │   Selenium  │  │    CSV/Log   │  │   BotCity   │
       └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
              │                │                │
              v                v                v
       FakeNameGenerator     CSVs           Fakturama
       SauceDemo             Logs
```

---

## 21. Resultado esperado

Ao executar:

```bash
python -m app.main
```

o sistema deve:

1. Gerar um comprador fictício.
2. Salvar o comprador em `buyer.csv`.
3. Acessar o SauceDemo.
4. Realizar o login.
5. Extrair todo o catálogo.
6. Salvar os produtos em `products.csv`.
7. Abrir o Fakturama.
8. Cadastrar o comprador.
9. Cadastrar todos os produtos.
10. Gerar screenshots de evidência.
11. Registrar a execução em log.

Ao final, os dados estarão disponíveis em:

```text
data/
```

e as evidências da execução em:

```text
results/
```

---

## 22. Possíveis evoluções

A estrutura atual permite evoluir o projeto sem alterar significativamente o fluxo principal.

Possíveis melhorias:

* Implementação de testes unitários mais abrangentes
* Validação automática dos dados cadastrados
* Tratamento específico para falhas de cada etapa
* Retry automático em operações Desktop
* Configuração de caminhos através de `.env`
* Geração de relatório final da execução
* Integração com CI/CD
* Persistência em banco de dados
* Execução em ambiente de automação centralizado

---

## 23. Considerações finais

O projeto demonstra uma automação RPA híbrida, combinando diferentes estratégias de automação em um único fluxo.

A automação utiliza **Selenium para aplicações Web**, **BotCity para aplicação Desktop**, **CSV para persistência**, **reconhecimento de imagem para interação visual**, **logs para rastreabilidade** e **screenshots como evidência da execução**.

A separação das responsabilidades permite que cada etapa seja desenvolvida, testada e evoluída de forma independente, mantendo o fluxo principal centralizado no `app/main.py`.
