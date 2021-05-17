#crescimento População Brasileira 1980-2016
import matplotlib.pyplot as plt
dados = open("dados.csv").readlines()
x_anos = []
y_populacao=[]

for i in range(len(dados)):
    if i !=0:
        linha = dados[i].split(";")
        x_anos.append(int(linha[0]))
        y_populacao.append(int(linha[1]))
print(y_populacao)
plt.bar(x_anos,y_populacao,color="#e4e4e4")
plt.plot(x_anos,y_populacao,color="k",linestyle="--")

plt.title("Crescimento da População Brasileira de 1980 até 2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.00")
#plt.show()

#salvar a imagem
plt.savefig("populacao_brasileira.png",dpi=300)
plt.savefig("populacao_brasileira.pdf")
