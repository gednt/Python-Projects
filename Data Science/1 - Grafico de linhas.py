#exemplo de gráfico básico usando python
import matplotlib.pyplot as plt
x = [1,2,5];
y = [2,3,7];
titulo = "Gráfico de Barras"
eixox = "Eixo X"
eixoy = "Eixo Y"
#Título do Gráfico
plt.title("Meu primeiro gráfico com python")

#Labels
#Eixos
plt.xlabel(eixox)
plt.ylabel(eixoy)
#o comando plot desenha o gráfico
plt.plot(x,y);
#O Comando show mostra a janela com gráfico
plt.show();