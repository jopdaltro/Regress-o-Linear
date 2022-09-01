import matplotlib.pyplot as plt


## base de dados a ser estudade y = variavel dependente e x = variavel independente
y = [137, 137, 137, 136, 135, 135, 133, 132, 133, 133, 128, 124, 126, 129, 126, 122, 122, 122, 119, 122 ]
x = [220, 220, 220, 220, 220, 225, 225, 225, 225, 225, 230, 230, 230, 230, 230, 235, 235, 235, 235, 235 ]

#Função que caluclua o quadrado do somatorio dos Xi para usar na equação da regressão linear
def quadrado(lista):
    soma = 0
    for i in lista:
        soma = soma + i**2
    return soma    

#Função que caluclua o somatorio de Xi*Yi para usar na equação da regressão linear
def somatorio_XiYi(lista1,lista2):
    soma = 0
    i = 0
    for numero in lista1:
         soma = soma + lista1[i]*lista2[i]
         i = i + 1
    return soma

#Função para calcular a Soma Total dos Resíduos (SQR)
def sqr (a,b):
    soma = 0
    i = 0
    for numero in a:
        soma = soma + (a[i]-b[i])**2
        i = i +1
    return soma

#Função para calcular a Soma Total dos Quadrados (STQ)
def sqt (a):
    soma = 0
    i = 0
    for numero in a:
        soma = soma + (a[i]-sum(a)/len(a))**2
        i = i+1
    return soma


######### Regrassão lienar #######

#alumas funções de somatorio ja são implmentados nos arrays no python, que faz com que a gente não precise fazer a função
#para calcular o somatorio dos Xis por exemplo. 
#sum -> retorna a soma de todos valores do vetor
#len -> retorna o tamanho de um vetor#

#Calculo do coeficiente angular de acordo com a formula da teoria.
coeficienteAngular = (sum(x)*sum(y)- len(x)*somatorio_XiYi(x,y))/((sum(x))**2 - len(x)*quadrado(x))

#Calculo do coeficiente linear de acordo com a formula da teoria.
coeficienteLinear = (somatorio_XiYi(x,y)*sum(x)- quadrado(x)*sum(y))/((sum(x))**2 - len(x)*quadrado(x))

print("A = ",coeficienteAngular)
print("B = ",coeficienteLinear)


##### criando um array pra armazenar os novos valores de Y do reauste
yArrumado = []
#Criando um nova função 'y' (Reajustado)  aparti dos coeficientes obtidos, e armazenando no array acima
for i in x:
    Y = coeficienteAngular*i + coeficienteLinear
    yArrumado.append(Y)

#printando as informações da resta e reajustes.    
print(f"Equação da reta: Y = {coeficienteAngular:.2f}X + {coeficienteLinear:.2f}")
print(f"Soma Total dos Quadrados (STQ): {sqt(y):.2f}")
print(f"Soma dos Quadrados dos Resíduos {sqr(y,yArrumado):.2f}:")
print(f"R^2 ={1-sqr(y,yArrumado)/sqt(y):.2f}")


##plotando os pontos originais em vermelho, e a regressão linear em verde pontilhado 
plt.plot(x,y,'ro')
plt.plot(x,yArrumado,'g--')
plt.show()