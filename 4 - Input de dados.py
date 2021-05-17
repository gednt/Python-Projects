print("Digite um valor")
valor = input()
print(valor)

valores = [];

i=0
while i<4:
    valores.append(float(input()));
    i = i+1;

soma = 0;
for cont in range(len(valores)):
    soma += valores[cont]
    print(soma)
