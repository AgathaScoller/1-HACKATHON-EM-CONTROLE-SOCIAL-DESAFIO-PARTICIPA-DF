# 1-HACKATHON-EM-CONTROLE-SOCIAL-DESAFIO-PARTICIPA-DF

PrivGuard AI

Detecção Automática de Dados Pessoais em Pedidos de Acesso à Informação

1. Objetivo

Este projeto apresenta uma solução de classificação automática de textos com o objetivo de identificar a presença de dados pessoais em pedidos de acesso à informação. A ferramenta foi desenvolvida para apoiar processos de triagem e reduzir o risco de divulgação indevida de informações pessoais em solicitações classificadas como públicas.

2. Descrição da Solução

A solução utiliza técnicas de Processamento de Linguagem Natural (PLN) combinadas com aprendizado de máquina supervisionado. O sistema analisa o conteúdo textual dos pedidos e classifica cada entrada em uma das seguintes categorias:

Contém dados pessoais

Não contém dados pessoais

Além do modelo de classificação, a solução inclui um módulo de detecção de padrões por meio de expressões regulares, responsável por identificar indícios explícitos de dados pessoais, como números de CPF, endereços de e-mail e telefones. Essas informações são utilizadas como variáveis auxiliares no processo de classificação.

3. Estrutura do Projeto

privguard-ai/
│
├── data/
│ └── exemplo_dados.csv
│
├── src/
│ ├── preprocessing.py
│ ├── regex_features.py
│ ├── train_model.py
│ └── predict.py
│
├── models/
│ ├── model.pkl
│ └── vectorizer.pkl
│
└── requirements.txt

4. Tecnologias Utilizadas

Python 3.10 ou superior

pandas

numpy

scikit-learn

joblib

Expressões regulares (regex)

5. Instalação do Ambiente

Clone o repositório e configure o ambiente virtual:

git clone https://github.com/seu-usuario/privguard-ai

cd privguard-ai

python -m venv venv

Ativação do ambiente:

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

Instalação das dependências:

pip install -r requirements.txt

6. Base de Dados

A base de dados deve estar no formato CSV contendo, no mínimo, as seguintes colunas:

texto: conteúdo do pedido de acesso à informação

label: classe associada ao texto

0 = não contém dados pessoais

1 = contém dados pessoais

Exemplo:

texto,label
"Solicito informações sobre gastos da secretaria",0
"Meu CPF é 123.456.789-00 e quero saber sobre um processo",1

7. Metodologia

O processamento da informação ocorre nas seguintes etapas:

Pré-processamento de texto
Normalização do texto para padronização da entrada.

Extração de indícios por padrões
Identificação de padrões associados a dados pessoais (CPF, e-mail e telefone) por meio de expressões regulares. Esses indícios são convertidos em variáveis numéricas.

Vetorização textual
Conversão do texto em representação numérica utilizando TF-IDF com unigramas e bigramas.

Classificação supervisionada
Treinamento de modelo de Regressão Logística com balanceamento de classes para lidar com possíveis desbalanceamentos entre as categorias.

Avaliação
O desempenho é avaliado por métricas de classificação, com ênfase no F1-score.

8. Treinamento do Modelo

Execute o script de treinamento:

python src/train_model.py

O script realiza:

Leitura da base de dados

Pré-processamento textual

Extração de variáveis baseadas em padrões

Vetorização TF-IDF

Treinamento do modelo

Avaliação de desempenho

Salvamento do modelo e do vetorizador na pasta models/

9. Execução de Previsões

Após o treinamento, é possível classificar novos textos utilizando:

python src/predict.py "Texto do pedido de acesso à informação"

A saída contém:

Classificação final

Probabilidade associada

Indícios de padrões detectados

10. Formato de Entrada e Saída

Entrada:
Texto livre contendo um pedido de acesso à informação.

Saída:
Estrutura contendo:

Classificacao: indica presença ou ausência de dados pessoais

Confianca: probabilidade da predição

Indicios_regex: padrões de dados pessoais detectados

11. Uso de Inteligência Artificial

A solução utiliza técnicas de aprendizado de máquina supervisionado para classificação de texto, implementadas por meio da biblioteca scikit-learn. O modelo foi treinado a partir de dados rotulados para identificar padrões associados à presença de dados pessoais em textos administrativos.

12. Aplicação

A ferramenta pode ser integrada a fluxos de triagem automatizada de pedidos de acesso à informação, contribuindo para a proteção de dados pessoais, conformidade com a legislação vigente e fortalecimento das práticas de governança da informação no setor público.
