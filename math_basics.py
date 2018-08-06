""" Sammlung von Mathematikfunktionen """

import math

def ggT(a, b):
  """ Die Funktion bestimmt den größten gemeinsamen Teiler zweier 
  Zahlen a und b. Sie verwendet dazu den Euklidischen Algorithmus des 
  griechischen Mathematikers Euklid (365 - 300 v.Chr.). Beschreibung 
  des Algorithmus siehe Kreul/Ziebarth 8.Aufl., S. 47f
  """
  bigger = max(a, b)
  smaller = min(a, b)

  while True:
    # div = int(bigger / smaller)
    mod = bigger % smaller

    if mod == 1:
      return 1

    if mod == 0:
      return smaller

    bigger = smaller
    smaller = mod

  return max(a, b)
