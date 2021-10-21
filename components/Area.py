from enum import Enum

class Area:
  def __init__(self):
    self.start_x_pos
    self.end_x_pos
    self.start_y_pos
    self.end_Y_pos
    self.infection_rate
    self.infection_persons_count

  def increase_infection_rate(self):
    return None
  
  def decrease_infection_rate(self):
    return None




class AreaStates(Enum):
  RED = 3  # dangerous
  ORANGE = 2  # risk
  GREEN = 1  # safe