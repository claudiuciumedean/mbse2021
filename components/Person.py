from enum import Enum

class Person:
  def __init__(self):
    self.id
    self.x_pos
    self.y_pos
    self.infected = False
    self.infection_severity = InfectionSeverity.GREEN

  def walk(self, x_pos, y_pos):
    return None

  def flee(self, x_pos, y_pos):
    return None

class InfectionSeverity(Enum):
  RED = 3 #high
  ORANGE = 2 #medium
  GREEN = 1 #low