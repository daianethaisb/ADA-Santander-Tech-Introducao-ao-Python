'''Uma vez criada, não é possível alterar nada de uma tupla!
Mas, então, pra que servem as tuplas?

- É um jeito de sinalizar que esses dados não deveriam ser alterados;

- É um meio de garantir que os elementos estarão em uma ordem específica;

 -O acesso a elementos de uma tupla é bem mais rápido.'''

# Outra utilidade de tuplas: fazer uma função retornar mais de um valor
def valor_valor_quadrado_valor_cubo(x):

  return x, x**2, x**3

valor_valor_quadrado_valor_cubo(2)


#Dicionarios: conjunto chave e valor.
dicionario = {"a":2, "b":6, "c":9}

cadastro_dict = {"nomes": ["José", "Maria", "Marta"],
                 "idades": [20, 30, 15],
                 "cidades" : ["SP", "RJ", "Salvador"]}

# para acessar os nomes
cadastro_dict["nomes"]

# iterando dicionários
for elemento in cadastro_dict:
  print(elemento)

for chave in cadastro_dict:
  print(cadastro_dict[chave][2])

lista_marta = []
for chave in cadastro_dict:
  lista_marta.append(cadastro_dict[chave][2])

lista_marta

for valor in cadastro_dict.values():
  print(valor[2])

[valor[2] for valor in cadastro_dict.values()]

[cadastro_dict[chave][2] for chave in cadastro_dict]

#transformando os valores em listas
list(cadastro_dict.values())

'''
Tambem é possivel visualizar os dados tabelados com a biblioteca Pandas
import pandas as pd

df = pd.DataFrame(cadastro_dict)

df'''

#Conjuntos: os dados não se repetem
# Ex: Para sabermos quais as notas únicas, basta converter a lista para um conjunto, com o construtor set()
notas = [9, 0, 6, 6, 0, 8, 2, 0, 3, 9,
         2, 3, 5, 4, 3, 9, 8, 5, 6, 2,
         7, 3, 5, 5, 9, 6, 3, 7, 3, 9,
         7, 2, 9, 5, 5, 4, 6, 6, 5, 5]

set(notas)
list(set(notas))

# Ex: Trabalhando com dois conjuntos diferentes
l1 = ["ada", "python", "dados", 2, 4]
l2 = ["web", "python", "devops", 42, 4]

pooxset(l1).intersection(set(l2)) #elementos comuns
set(l1).union(set(l2)) #união das listas (sem repetir elementos)
set(l1).difference(set(l2)) #diferença entre as listas