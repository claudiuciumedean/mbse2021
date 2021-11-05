from enum import Enum
import uuid

import components.World as World

class AreaStates(Enum):
    RED = 3  # dangerous
    ORANGE = 2  # risk
    GREEN = 1  # safe

class Area:
    def __init__(self, start_x_pos, end_x_pos, start_y_pos, end_y_pos, infection_rate):
        self.id = str(uuid.uuid4())
        self.start_x_pos = start_x_pos
        self.end_x_pos = end_x_pos
        self.start_y_pos = start_y_pos
        self.end_y_pos = end_y_pos
        self.infection_rate = infection_rate
        self.area_states = self.compute_area_state()


    def compute_area_state(self):
        if self.infection_rate < 0.2:
            return AreaStates.GREEN

        elif 0.2 <= self.infection_rate < 0.8:

            return AreaStates.ORANGE

        elif self.infection_rate >= 0.8:
            return AreaStates.RED

    def is_in_area(self, x, y):
        return self.start_x_pos <= x <= self.end_x_pos and self.start_y_pos <= y <= self.end_y_pos


