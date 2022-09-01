import pandas as pd

arquivo = pd.read_csv('C:\\Users\\thelo\\Analise de Dados\\Projetos\\DADOS\\iris.csv')

arquivo ['Species'] = arquivo['Species'].replace('Iris-setosa',0)
arquivo ['Species'] = arquivo['Species'].replace('Iris-versicolor',1)
arquivo ['Species'] = arquivo['Species'].replace('Iris-virginica',2)

y = arquivo['Species']
x = arquivo.drop('Species', axis=1)

from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste = train_test_split(x,y, test_size = 0.3)

from sklearn.ensemble import ExtraTreesClassifier
#criando modelos
modelo = ExtraTreesClassifier()
modelo.fit(x_treino,y_treino)

#imPRIMir resultados
resultado = modelo.score(x_teste,y_teste)
print("acuracia", resultado)

y_teste [0:5]
x_teste[0:5]