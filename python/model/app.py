# Libs
from flask import Flask, request, jsonify
import pickle as pkl
import pandas as pd

app = Flask(__name__)

# Carregar o preprocessador e o modelo
with open('preprocessador.pkl', 'rb') as f:
    preprocessador = pkl.load(f)

with open('classificador_knn_smote.pkl', 'rb') as f:
    classificador = pkl.load(f)

# Rota para fazer previsões
@app.route('/predict', methods=['POST'])
def predict():

    dados_formulario = request.json  # Receber dados JSON do formulário
    dados_df = pd.DataFrame([dados_formulario])

    # Pré-processar as informações
    dados_preprocessados = preprocessador.transform(dados_df)

    # Fazer a previsão
    previsao = classificador.predict(dados_preprocessados)
    return jsonify({'previsao': int(previsao[0])})

if __name__ == '__main__':
    app.run(debug=True)
