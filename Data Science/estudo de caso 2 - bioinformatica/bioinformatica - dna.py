
#bacteria
dados = open("bacteria.fasta").read()

saida = open("bacteria.html","w")

#dicionário
##vetor de contagem de par de dna
cont_pares = {}

for i in ['A','T','C','G']:
    for j in ['A','T','C','G']:
        cont_pares[i+j]=0
#tirar as quebras de linha
dados = dados.replace("\n","")
#preencher os valores
for k in range(len(dados)-1):
   cont_pares[dados[k]+dados[k+1]] += 1

print(cont_pares);

#html
i = 1;
for k in cont_pares:
    transparencia = cont_pares[k]/max(cont_pares.values())
    saida.write("<div style='width:100px; border:1px solid #111; height:100px; float:left; background-color:rgba(0,0,255,"+str(transparencia)+"')>"+k+"</div>")
    
    if i%4 == 0:
        saida.write("<div style='clear:both'></div>")

    i+=1  
saida.close()

#humano
dados = open("human.fasta").read()

saida = open("human.html","w")

#dicionário
##vetor de contagem de par de dna
cont_pares = {}

for i in ['A','T','C','G']:
    for j in ['A','T','C','G']:
        cont_pares[i+j]=0
#tirar as quebras de linha
dados = dados.replace("\n","")
#preencher os valores
for k in range(len(dados)-1):
   cont_pares[dados[k]+dados[k+1]] += 1

print(cont_pares);

#html
i = 1;
for k in cont_pares:
    transparencia = cont_pares[k]/max(cont_pares.values())
    saida.write("<div style='width:100px; border:1px solid #111; height:100px; float:left; background-color:rgba(0,0,255,"+str(transparencia)+"'; font-color:white)>"+k+"</div>")
    
    if i%4 == 0:
        saida.write("<div style='clear:both'></div>")

    i+=1  
saida.close()