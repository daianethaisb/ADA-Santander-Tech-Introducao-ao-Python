def cumprimenta_parte_do_dia(nome, parte_do_dia):
  '''
  esta função recebe um nome e uma parte do dia, e imprime na tela um
  cumprimento de acordo com esses dois argumentos

  - nome (str): qualquer nome própiro;
  - parte_do_dia (str): deve ser unicamente uma das três opções: ["manhã", "tarde", "noite"]
  '''

  if parte_do_dia == "manhã":
    cumprimento = "Bom dia"
  elif parte_do_dia == "tarde":
    cumprimento = "Boa tarde"
  elif parte_do_dia == "noite":
    cumprimento = "Boa noite"
  else:
    raise ValueError(f"A parte do dia informada ({parte_do_dia}) não é válida!")

  cumprimento = f"{cumprimento}, {nome}"

  print(cumprimento)

  cumprimenta_parte_do_dia("Daiane", "tarde")


#Calculadora
def calcula_soma(n1, n2):
  return n1 + n2

def calcula_subtracao(n1, n2):
  return n1 - n2

def calcula_multiplicacao(n1, n2):
  return n1*n2

def calcula_divisao(n1, n2):
  '''
  esta função calcula o quociente entre o primeiro argumento e o segundo

  - n1 (float), numerador
  - n2 (float), denominador, deve ser != 0
  '''

  return n1/n2

def calcula_operacao(n1, n2, op):
  '''
  - n1 (float)
  - n2 (float)
  - op (str): indicando a operação a ser feita ["+", "-", "*", "/"]

  returns:

  n1 [op] n2, onde [op] é a operação correspondente à string op
  '''

  if op == "+":
    resp = calcula_soma(n1, n2)
  elif op == "-":
    resp = calcula_subtracao(n1, n2)
  elif op == "*":
    resp =  calcula_multiplicacao(n1, n2)
  elif op == "/":
    resp =  calcula_divisao(n1, n2)
  else:
    raise ValueError(f"A operação informada ({op}) não é válida!")

  return resp

calcula_operacao(2, 3, "+")