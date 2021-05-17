#scatterplot (Gráfico de Pontos)
#exemplo de gráfico básico usando python
import matplotlib.pyplot as plt
x1 = [1,3,5,7,9];
y1 = [2,3,7,1,0];

x2 = [2,4,6,8,10];
y2 = [5,1,3,7,4];

titulo = "Gráfico de Barras"
eixox = "Eixo X"
eixoy = "Eixo Y"
#Título do Gráfico
plt.title("Meu primeiro gráfico com python")

#Labels
#Eixos
plt.xlabel(eixox)
plt.ylabel(eixoy)
#o comando plot desenha o gráfico para comparação
plt.scatter(x1,y1, label = "Grupo 1");
plt.scatter(x2,y2, label = "Grupo 2", color='r');
#para ligar os pontos
plt.plot(x1,y1);
plt.plot(x2,y2);
#O Comando show mostra a janela com os gráficos
plt.legend()
plt.show();

#pesquisar atributos no site oficial da lib mathplot