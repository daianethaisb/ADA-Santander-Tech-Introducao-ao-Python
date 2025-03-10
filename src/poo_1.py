class Pessoa:

  def __init__(self, name, age, res):

    # inicializar os atributos da classe, que terão valores definidos na instanciação
    # como argumentos do método construtor
    self.nome = name
    self.idade = age
    self.residencia = res
    
    # inicializar alguns atributos cujos valores são fixados
    self.num_filhos = 0
    self.profissao = None
    self.salario = 0

  # definindo outros métodos da classe
  def fala(self, mensagem):
    print(f"{self.nome} diz: '{mensagem}'")

  def consegue_emprego(self, prof, valor_salario):
    self.profissao = prof
    self.salario = valor_salario

  def aumenta_salario(self, porcentagem):
    '''
    porcentagem: float entre 0 e 1, indicando o percentual de aumento de salario
    '''
    self.salario = self.salario*(1 + porcentagem)