import pickle as pkl
import pandas as pd

# Carregar o preprocessador e o modelo
with open('preprocessador.pkl', 'rb') as f:
    preprocessador = pkl.load(f)

with open('classificador.pkl', 'rb') as f:
    classificador = pkl.load(f)


def predict():
    dados_formulario = "dicionário do banco de dados"
    dados_df = pd.DataFrame([dados_formulario])

    # Pré-processar os dados
    dados_preprocessados = preprocessador.transform(dados_df)

    # Fazer a previsão
    previsao = classificador.predict(dados_preprocessados)
    return previsao[0]