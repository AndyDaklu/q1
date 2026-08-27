# RPG HERO GAME  
class Hero:
  def __init__(self, name, hp):
    self.name = name
    self.hp = hp
  def damage(self, amount):
    self.hp -= amount

arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.damage(10)
print(f"{arthur.name}'s HP:{arthur.hp}")
print(f"{morgana.name}'s HP:{morgana.hp}")
