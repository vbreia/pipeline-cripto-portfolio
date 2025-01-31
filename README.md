# Pipeline de Dados - Mercado Bitcoin

## Descrição do Projeto
Pipeline de dados desenvolvido para coletar automaticamente os preços das criptomoedas Bitcoin (BTC), Ethereum (ETH) e Solana (SOL) do site mercadobitcoin.com.br através de webscraping. Os dados são processados, armazenados em formato JSON e em um banco de dados SQLite, preparando-os para futura integração com a plataforma "breia-data-cripto".

## Funcionalidades
- Webscraping automatizado do Mercado Bitcoin
- Coleta de preços de BTC, ETH e SOL
- Processamento e limpeza dos dados
- Armazenamento dual (JSON e SQLite)
- Orquestração automatizada via Airflow

## Tecnologias Utilizadas
- Python
- Apache Airflow
- SQLite
- Docker
- Beautiful Soup (webscraping)
- Pandas (processamento de dados)

## Estrutura do Projeto

pipeline-portfolio/
├── airflow/
│   └── dags/
│       └── crypto_pipeline.py
├── src/
│   ├── scrapers/
│   │   └── mercado_bitcoin.py
│   ├── processors/
│   │   └── data_transformer.py
│   └── loaders/
│       ├── json_loader.py
│       └── sqlite_loader.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── database/
│       └── crypto.db
└── docker-compose.yml

## Fluxo de Dados
1. **Extração**: Coleta automática dos preços via webscraping
2. **Transformação**: Processamento e formatação dos dados
3. **Carregamento**: 
   - Exportação para arquivos JSON
   - Armazenamento em banco SQLite
4. **Orquestração**: Gerenciamento do pipeline via Airflow

![Fluxo de Dados](./docs/fluxogram.svg)

## Próximas Etapas
- Desenvolvimento da plataforma "breia-data-cripto"
- Implementação da integração automática dos dados coletados
- Interface de visualização dos dados

