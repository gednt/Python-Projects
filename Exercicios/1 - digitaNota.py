nota1 = float(input("Digite a Nota 1\n"));
nota2 = float(input("Digite a Nota 2\n"));
print(nota1)
print(nota2)
notaGeral = (nota1+nota2)/2;
if notaGeral >= 6:
    print("O aluno foi aprovado" + str(notaGeral))
else:
    print("O aluno foi reprovado" + str(notaGeral))
