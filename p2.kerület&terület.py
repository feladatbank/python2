'''
Készíts egy programot, amelyben van egy Negyzet nevű osztály. Attribútuma legyen az oldal hossza. Rendelkezzen továbbá a kerület és terület számításra is egy-egy metódussal!
'''

class Negyzet:
  def __init__(self, oldalhossza):
    self.oldalhossza = oldalhossza

  def terulet(self):
    return self.oldalhossza ** 2

  def kerulet(self):
    return self.oldalhossza * 4

negyzet1 = Negyzet(10)

print(f"A négyzet területe: {negyzet1.terulet()} cm")

print(f"A négyzet kerülete: {negyzet1.kerulet()} cm")
