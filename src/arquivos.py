import csv

# leitura do arquivo, na forma de tabela
with open("alunos_star_wars.csv", "r", encoding="utf-8") as f:

    tabela_lida = [linha for linha in csv.reader(f, delimiter=",", lineterminator="\n")]

# processamento do arquivo
nome_alunos = [linha[0] for linha in tabela_lida]

aluno=input(f"Digite o nome do aluno cuja média vc quer saber.\nOpções: {nome_alunos[1:]} ")

dados_aluno = tabela_lida[nome_alunos.index(aluno)]

nota1 = float(dados_aluno[1])
nota2 = float(dados_aluno[2])

media = (nota1 + nota2)/2

print(f"\nA média do(a) aluno(a) {aluno} é: {media}")