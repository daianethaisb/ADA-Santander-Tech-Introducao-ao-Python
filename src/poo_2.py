#Métodos mágicos
'''Permitem que objetos de classes personalizadas se comportem como objetos nativos do Python '''

class Horario:

  def __init__(self, hora, min, seg):

    self.h = hora
    self.m = min
    self.s = seg

  def __repr__(self):

    return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"


  def __str__(self):

    return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"
  
  # Define um método de soma de horas na nossa classe, que vai ser chamado pelo operador aritmético "+"
  def __add__(self, other):

    se = self.s + other.s
    mi = self.m + other.m
    ho = self.h + other.h

    if se >= 60:
      mi += 1
      # mi = mi + 1
      
      se -= 60
      # se = se - 60

    if mi >= 60:
      ho += 1
      mi -= 60

    if ho >= 24:
      ho -= 24

    return Horario(ho, mi, se)
  
  # Método para comparar dois horários
  def __gt__(self, other):

    if self.h > other.h:
      return True
    elif self.h == other.h and self.m > other.m:
      return True
    elif self.h == other.h and self.m == other.m and self.s > other.s:
      return True

    return False


h1 = Horario(9, 27, 42)
h2 = Horario(7, 38, 41)

h3 = h1 + h2

print(f"Entrei às {h1}\nTrabalhei por {h2}\nVou sair às {h3}")

h1 = Horario(9, 27, 42)
h2 = Horario(9, 38, 36)

h1 > h2