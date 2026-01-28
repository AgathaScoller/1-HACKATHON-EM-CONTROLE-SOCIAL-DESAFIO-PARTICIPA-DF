# 1-HACKATHON-EM-CONTROLE-SOCIAL-DESAFIO-PARTICIPA-DF

PrivGuard AI

Detecção de Dados Pessoais em Pedidos de Acesso à Informação

Objetivo

Desenvolver um modelo de classificação de texto capaz de identificar automaticamente a presença de dados pessoais em pedidos de acesso à informação, apoiando processos de triagem e prevenção de divulgação indevida.

Descrição da Solução

A solução utiliza técnicas de Processamento de Linguagem Natural e aprendizado de máquina supervisionado para classificar textos em duas categorias:

Contém dados pessoais

Não contém dados pessoais

O sistema combina vetorização TF-IDF com variáveis auxiliares extraídas por expressões regulares, responsáveis por identificar padrões como CPF, e-mail e telefone.

Tecnologias Utilizadas

Python, pandas, numpy, scikit-learn, joblib e expressões regulares.

Base de Dados

Arquivo CSV com as colunas:

texto: conteúdo do pedido

label: 0 (sem dados pessoais) ou 1 (com dados pessoais)

Metodologia

Pré-processamento textual

Extração de padrões de dados pessoais (regex)

Vetorização TF-IDF (unigramas e bigramas)

Treinamento de Regressão Logística com balanceamento de classes

Avaliação com foco em F1-score

Treinamento

python src/train_model.py

O modelo treinado e o vetorizador são salvos na pasta models/.

Previsão

python src/predict.py "Texto do pedido"

Saída: classificação, probabilidade e indícios de padrões detectados.

Aplicação

A solução pode ser integrada a sistemas de triagem automática de pedidos públicos, auxiliando na proteção de dados pessoais e na conformidade com normas de privacidade e acesso à informação.
