# 💻 Data Stack Moderna E-commerce

Este projeto implementa uma Data Stack Moderna completa, no contexto para um e-commerce, focando na geração de dados sintéticos, orquestração de pipelines, modelagem de dados usando dbt (data build tool), e entrega automatizada de relatórios críticos.

## 🎯 **Objetivo**

O objetivo principal é calcular e monitorar a taxa de churn (rotatividade de clientes) do e-commerce e enviar um relatório por meio de uma API para apoiar decisões estratégicas de retenção de clientes.

## 🛠️ **Tecnologias Utilizadas (Stack)**
A arquitetura do projeto é construída com as seguintes ferramentas:

| Categoria | Tecnologia & Versão | Finalidade |
| :--- | :--- | :--- |
| **Linguagem** | Python 3.11.9 | Geração de dados (Faker) e scripts auxiliares. |
| **Orquestração** | Apache Airflow (via Astro CLI) | Gerenciamento, agendamento e monitoramento de pipelines (DAGs). |
| **Ambiente** | Docker Desktop | Padronização e isolamento do ambiente de desenvolvimento/produção. |
| **Modelagem** | dbt-core 1.9.0 | Transformação e modelagem de dados. |
| **Conexão dbt** | dbt-postgres 1.9.0 | Adaptador para conexão com o banco de dados PostgreSQL. |
| **Banco de Dados** | PostgreSQL (Postgres) | Data Warehouse para o armazenamento dos dados e modelos. |
| **Gerenciamento de Pacotes** | `uv` | Gerenciamento eficiente de dependências e bibliotecas Python. |
| **Visualização/Acesso ao DB** | DBeaver | Ferramenta para visualização e gerenciamento do banco de dados PostgreSQL. |
| **Relatórios** | Telegram API | Envio automatizado do relatório final de churn. |

## 📐 **Arquitetura do Projeto**
A arquitetura segue um fluxo de trabalho claro e modular, dividida em três etapas principais de modelagem de dados (Seeds, Staging e Marts), utilizando dbt para as transformações e Airflow (orquestrado via Astro CLI) para o agendamento e controle do pipeline.

1. **Geração de Dados:**

    - Utilizamos a biblioteca Faker em Python para gerar dados sintéticos simulando transações e clientes de um e-commerce.

    - Os dados gerados são exportados para arquivos CSV.

1. **Ingestão e Modelagem (dbt):**

   - Os arquivos CSV são carregados e transformados em um Data Warehouse PostgreSQL através do dbt.

   - Seeds: É a primeira camada. As tabelas são carregadas exatamente como estão nos CSVs originais.

   - Staging: Aplica transformações e tratamentos iniciais e a lógica para marcar se os clientes estão ativos ou em churn.

   - Marts: Camada final, responsável pela criação do datamart (tabelas Fato e Dimensão) otimizado para relatórios.

2. **Orquestração (Airflow/Astro CLI):**

   - O Apache Airflow é o responsável por orquestrar os pipelines (DAGs) e monitorar sua execução.

   - O Airflow garante que as tarefas sejam executadas em uma sequência e horário específico agendado.

3. **Entrega do Relatório:**

   - Após a conclusão da modelagem (Marts), um relatório da taxa de churn do e-commerce é gerado e enviado automaticamente por meio da API do Telegram.
  
## 🤖 **Geração e Envio de Relatório (API - Python)**
Na pasta scripts do repositório se encontra o código.

- **Propósito:** Automatizar a geração de um relatório de performance semanal e seu envio imediato para um canal de comunicação.

- **Ação:** O script lê os dados de pedidos e produtos (do diretório de seeds do dbt), calcula métricas importantes como total de pedidos, cancelamentos e a taxa de cancelamento, além de identificar o produto mais caro.

- **Entrega:** Após o cálculo, ele formata as métricas em uma mensagem e a envia para o Telegram utilizando credenciais de API seguras, notificando a equipe sobre os resultados da semana.

## 🚀 **Considerações Finais**
Esta implementação estabeleceu uma base robusta de Data Engineering focada na entrega de valor de negócio.

**Valor Chave do Projeto**
-  **Modelo Prático:**
   -  Demonstra a construção de uma Data Stack Moderna completa (Geração -> Airflow -> dbt -> Postgres) para um cenário de e-commerce real.

- **Decisão Ágil:**
  - O cálculo e envio automatizado da taxa de churn via Telegram API permite que as equipes de negócio respondam rapidamente aos dados críticos de retenção.

- **Qualidade de Dados:**
  - A modelagem em camadas (Seeds, Staging, Marts) com dbt garante que os dados finais estejam limpos e prontos para análise.

## 🌎 Agradecimentos
Agradeço imensamente a todos que visitarem este repositório! Espero que este projeto sirva de recurso valioso para seus estudos e futuras implementações de Engenharia de Dados. Sinta-se à vontade para explorar, sugerir melhorias ou entrar em contato.