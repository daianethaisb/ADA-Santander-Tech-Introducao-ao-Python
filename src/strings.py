nome = "Daiane"

#Percorre cada caractere da string com o for
for caractere in nome:
  print(caractere)

# Dá pra fazer o mesmo com o range() e o len():
for i in range(len(nome)):
  print(nome[i])

#Transformar uma string em uma lista de caracteres
nome_lista = list(nome)

#Trasnformar a lista de volta pra string
"".join(nome_lista)

#Ao multiplicar uma string por um número inteiro, a string é repetida
print("="*50)
print("OLÁ, BEM-VINDOS À ADA TECH".center(50))
print("="*50)

#Limpar espaços a mais (duplicados) do começo, meio e fim da string
string = "            eu    gosto de         estudar python   "
" ".join(string.split())

#Formatação de String
# data
dia, mes, ano = 1, 2, 2020

string_data = "{:02d}/{:02d}/{:04d}".format(dia, mes, ano)

print(string_data)

#double
preco = 1499.50

"Preço: R$ {:.2f}".format(preco)


#criando função que verifica estado civil
estado_civil = input("Digite seu estado civil (opções possíveis: S, C, D, V): ").upper()

while estado_civil not in ["S", "C", "D", "V"]:

  estado_civil = input("Resposta inválida! Digite seu estado civil (opções possíveis: S, C, D, V): ").upper()

print(f"Estado civil: {estado_civil}")