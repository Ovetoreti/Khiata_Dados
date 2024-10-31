# Com base na análise dos resultados e considerando o equilíbrio entre precisão e capacidade de generalização, o Decision Tree com o critério Gini ajustado se destaca como a melhor escolha. Este modelo apresentou:
 
# 1. Equilíbrio entre as classes: Com precisão e recall mais balanceados para as classes "Sim" e "Não".
# 2. Acurácia média: 0.65, conforme cross-validation, o que demonstra um bom nível de confiabilidade e generalização para novos dados.
# 3. Menor tendência de enviesamento: Diferente do Naive Bayes, que apresentou forte enviesamento, o Decision Tree com Gini distribuiu as previsões de forma mais uniforme.

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

from sklearn.model_selection import GridSearchCV
from sklearn import tree

# Importações para o Cross Validation
from sklearn.model_selection import KFold

# Para serializar
import pickle as pkl

df = pd.read_csv(r'python\utils\FormsKhiataTratada.csv')

# -=-=-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-

# Atributos
atributos = df.drop('Utilizaria_App_Costura', axis=1)

# Resposta
resposta = df['Utilizaria_App_Costura']

# Instanciando o labelEncoder - resposta
# Usando o labelEncoder para a resposta
label_encoder = LabelEncoder()

# Transformando os atributos de valores categóricos para valores numéricos
# Usando o ColumnTransformer() para transformar e o OrdinalEncoder() para ordenar as colunas

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

smote = SMOTE(k_neighbors = 5, random_state = 42)
X_treino_smote, y_treino_smote = smote.fit_resample(X_treino, y_treino)

# Parâmetros
parametros_gini = {
    'criterion': ['gini'],
    'splitter': ['best', 'random'],
    'max_depth': [None, 2, 4, 6, 8, 10, 12],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 5, 10],
    'max_features': [None, 'sqrt', 'log2']
}

# Criando classificador com os hyper parameters
classificador_gini_smote_cross_validation = tree.DecisionTreeClassifier(
    criterion='gini', 
    max_depth=4, 
    max_features='log2', 
    min_samples_leaf=10, 
    min_samples_split=2, 
    splitter='best'
)

# Criando objeto GridSearchCV, para o Cross Validation com os hyperparametros
gini_cross_validantion_grid = GridSearchCV(
    estimator=classificador_gini_smote_cross_validation, 
    param_grid=parametros_gini, 
    scoring='accuracy', 
    cv=KFold(n_splits=5, random_state=42, shuffle=True)
)

# Treinando o Modelo com o SMOTE
gini_cross_validantion_grid.fit(X_treino_smote, y_treino_smote)

# Serializar o pipeline de pré-processamento
with open(r'python\model\preprocessador.pkl', 'wb') as f:
    pkl.dump(preprocessador, f)
    
# Serializar o modelo
with open(r'python\model\classificador.pkl', 'wb') as f:
    pkl.dump(gini_cross_validantion_grid, f)