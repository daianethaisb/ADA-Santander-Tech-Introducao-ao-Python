#Captando do usuário a quantidade de notas
num_notas = int(input("Digite o número de notas: "))

notas = []

cont = 1
while cont <= num_notas:

  # capta do usuário uma nota
  nota_atual = float(input("Digite a nota: "))

  notas.append(nota_atual)

  cont += 1

media = sum(notas)/len(notas)

print("\nA média é:", media)


#Separando números positivos e negativos de uma lista de números
lista_num = [-10, 2, -6, 4.2, -8, 3.14, -6, 0]

lista_num_pos = []
lista_num_neg = []
lista_num_neutro = []

for elemento in lista_num:
  if elemento < 0:
    lista_num_neg.append(elemento)
  elif elemento > 0:
    lista_num_pos.append(elemento)
  else:
    lista_num_neutro.append(elemento)

print(lista_num_pos)
print(lista_num_neg)
print(lista_num_neutro)


#Imprimindo se um numero da lista é par ou impar com Compreensão de Listas
lista_num = [4, 7, 13, 15, 1, 8, 16, 20, 3]
lista_par_ou_impar = ["par" if elemento % 2 == 0 else "ímpar" for elemento in lista_num]

lista_par_ou_impar


#Percorre uma sequencia de N elementos usando Range
N = 5
for _ in range(N):
  print("Olá, mundo!")

# o código acima é equivalente a
cont = 1

while cont <= N:
  print("Olá, mundo!")
  cont += 1


#Imprime apenas os elementos de indice par usando Range
for indice in range(len(lista_num)):

  if indice % 2 == 0:
    print(lista_num[indice])