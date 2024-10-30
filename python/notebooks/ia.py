# Importações para análise de dados
import pandas as pd

# Importações para o Pré-processamento
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer, make_column_selector

# Importação para separar o treino e teste
from sklearn.model_selection import train_test_split

# Importação para aumentar nossa base de dados, duplicamento de dados
from imblearn.over_sampling import SMOTE
from sklearn.neighbors import KNeighborsClassifier

# Importações para a Serialização
import pickle as pkl

# Importação para o Pipeline
from sklearn.pipeline import Pipeline

df = pd.read_csv(r'python\utils\FormsKhiataTratada.csv')

# Atributos
atributos = df.drop('Utilizaria_App_Costura', axis=1)

# Resposta
resposta = df['Utilizaria_App_Costura']

# Instanciando o labelEncoder - resposta
# Usando o labelEncoder para a resposta
label_encoder = LabelEncoder()

# Transformando os atributos de valores categóricos para valores numéricos
# Usando o ColumnTransformer() para transformar
# Usando o OrdinalEncoder() para ordenar as colunas

preprocessador = ColumnTransformer(transformers = [
    ('categoricas', OrdinalEncoder(), make_column_selector(dtype_include = ['object', 'bool'])),
    ],
    remainder='passthrough', # para preservar as colunas não transformadas no dataset, as colunas transformardas vão aparecer em primeiro no df
    verbose_feature_names_out = False # False para não colocar prefixo _categoricas nas colunas transformadas
)

# preprocessador para variáveis de resposta
resposta_pre = label_encoder.fit_transform(resposta) # resposta_pre variável sendo a coluna de resposta preprocessadas

# preprocessador atributos
atributos_pre = pd.DataFrame(preprocessador.fit_transform(atributos), columns = preprocessador.get_feature_names_out())

# Nome das colunas na nova ordem - O columnsTransformer ordena de acordo com as novas transformações
colunas_novas = preprocessador.get_feature_names_out()

# Capturando os nomes originais
colunas_originais = atributos.columns

# Criando o dataFrame com a mesma ordem inicial de colunas
atributos_pre = atributos_pre[colunas_originais] # atributos_pre variáveis sendo a coluna de atributos preprocessadas.

X_treino, X_teste, y_treino, y_teste = train_test_split(atributos_pre, resposta_pre, test_size = 0.20, random_state=42)

smote = SMOTE(k_neighbors=5, random_state=42)
X_treino_smote, y_treino_smote = smote.fit_resample(X_treino, y_treino)

# Criando classificador com SMOTE
classificador_knn_smote = KNeighborsClassifier(n_neighbors = 34)

# Treinando o modelo SMOTE
classificador_knn_smote.fit(X_treino_smote, y_treino_smote)

# Prevendo o Modelo com o SMOTE
previsoes_knn_smote = classificador_knn_smote.predict(X_teste)

# Serializar o pipeline de pré-processamento
with open(r'python\model\preprocessador.pkl', 'wb') as f:
    pkl.dump(preprocessador, f)
    
# Serializar o modelo
with open(r'python\model\classificador.pkl', 'wb') as f:
    pkl.dump(classificador_knn_smote, f)
