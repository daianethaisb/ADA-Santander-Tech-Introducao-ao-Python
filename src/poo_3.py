#Herança e Polimorfismo
class Animal:
  def __init__(self, nome):
    self.nome = nome

  def fala(self):
    print(f"{self.nome} faz barulho!")

a1 = Animal("grilo")

a1.fala()

class Cachorro(Animal):
    
  def fala(self):
    print(f"{self.nome} late!")

c1 = Cachorro("léo")

c1.fala()

class Gato(Animal):
    
  def fala(self):
    print(f"{self.nome} mia!")

g1 = Gato("fred")

g1.fala()

'''Imagine agora que queremos herdar um método parcialmente, com a possibilidade de alterá-lo.

(Isso é importante, pois se apenas copiássemos o método original, qualquer alteração nele teria de ser feita em todos os locais onde ele é copiado...)

Para isso, usamos o método super()'''

class Cachorro(Animal):

  def __init__(self, nome, raca, cor_do_pelo):

    super().__init__(nome)

    self.raca = raca
    self.cor_do_pelo = cor_do_pelo

    
  def fala(self):

    super().fala()

    print(f"Mas, por ser um cachorro, {self.nome} late!")

c2 = Cachorro("léo", "poodle", "branco")

c2.fala()

'''Mais especificamente, objetos de uma classe filha podem também ser tratados como se pertencessem à classe mãe.

O método isinstance recebe 2 parâmetros: um objeto e uma classe.

Ele retorna True caso o objeto pertenca à classe, e False caso não pertença.

Isso é útil porque uma função que seja feita para lidar com Animal será capaz de lidar com qualquer classe herdeira 
de Animal com a mesma facilidade.'''

g2 = Gato("fred")
c2 = Cachorro("leo", "poodle", "branco")

isinstance(g2, Gato) #True
isinstance(c2, Cachorro) #True
isinstance(g2, Animal) #True
isinstance(c2, Animal) #True

isinstance(g2, Cachorro) #False
isinstance(c2, Gato) #False