#boxplot diagrama de caixa
import matplotlib.pyplot as plt
#para gerar dados aleatórios
import random
vetor = []

for i in range(100):
    numero_aleatorio = random.randint(0,5000);
    vetor.append(numero_aleatorio);
plt.boxplot(vetor);
plt.title("BoxPlot");
plt.show();
