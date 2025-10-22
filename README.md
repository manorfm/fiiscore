# FII Score: Análise Fundamentalista de Fundos Imobiliários

O **FII Score** é uma aplicação de análise que avalia e pontua Fundos de Investimento Imobiliário (FIIs) com base em múltiplos indicadores fundamentalistas. O objetivo é fornecer uma visão clara e baseada em dados para auxiliar na tomada de decisões de investimento, com foco em segurança e desempenho a longo prazo.

## ✨ Recursos Principais

- **Análise Multifatorial Sofisticada:** O score não se baseia apenas em preço ou dividendos. Ele utiliza um modelo ponderado e normalizado que considera:
  - **Dividend Yield:** Potencial de geração de renda.
  - **P/VP (Preço / Valor Patrimonial):** Métrica de valuation.
  - **Vacância:** Saúde e ocupação dos imóveis.
  - **Liquidez Diária:** Facilidade de compra e venda das cotas.
  - **Quantidade de Ativos:** Nível de diversificação do fundo.
- **Normalização Inteligente:** Cada indicador é normalizado para uma escala de 0 a 1, garantindo que nenhuma métrica distorça a análise.
- **Sistema de Classificação:** Com base no score final, os FIIs são classificados em:
  - **Recomendado:** FIIs com ótimos indicadores.
  - **Neutro:** FIIs com indicadores medianos.
  - **Não Recomendado:** FIIs que exigem cautela.
- **API RESTful:** Todos os dados e análises podem ser consumidos via uma API FastAPI, permitindo a integração com outras ferramentas.

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python, FastAPI
- **Gerenciador de Dependências:** Poetry
- **Banco de Dados:** MongoDB
- **Testes:** Pytest, Unittest.mock

## 🚀 Como Começar

Siga os passos abaixo para configurar e executar o projeto localmente.

### 1. Pré-requisitos

- Python 3.10+
- Docker e Docker Compose
- Poetry

### 2. Clone o Repositório

```bash
git clone <URL_DO_REPOSITÓRIO>
cd fii-score
```

### 3. Suba o Banco de Dados

A aplicação utiliza um container Docker com MongoDB. Para iniciá-lo, execute:

```bash
docker-compose up -d
```
O `-d` executa o container em modo detached (em segundo plano).

### 4. Instale as Dependências

Use o Poetry para instalar todas as dependências do projeto:

```bash
poetry install --no-root
```

### 5. Inicie a Aplicação

Com o ambiente configurado, inicie o servidor FastAPI:

```bash
poetry run uvicorn app:app --reload
```
A aplicação estará disponível em `http://127.0.0.1:8000`.

## ✅ Como Executar os Testes

Para garantir a qualidade e a integridade do código, a aplicação possui uma suíte de testes completa. Para executá-la, use o comando:

```bash
poetry run pytest
```

##
Swagger
http://127.0.0.1:8000/docs
