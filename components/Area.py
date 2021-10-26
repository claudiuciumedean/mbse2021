from enum import Enum

import components.World as World


class Area:
    def __init__(self):
        self.AreaStates = 0
        self.start_x_pos = 0
        self.end_x_pos = 0
        self.start_y_pos = 0
        self.end_Y_pos = 0
        self.infection_rate = 0
        self.infection_persons_num = 0
        self.person_num = 0
        self.area_states = AreaStates.GREEN

    # a person come into this area
    def add_person_num(self):
        self.person_num += 1
        self.change_infection_rate(self)

    # a person leave this area
    def decrease_person_num(self):
        if self.person_num != 0:
            self.person_num -= 1
            self.change_infection_rate(self)

    # an infected person come into the area
    def add_infection_person_num(self):
        self.person_num += 1
        self.infection_persons_num += 1
        self.change_infection_rate(self)

    # when a person come into the area,then the infection_rate change
    # we suppose that if rate over 0.8 is dangerous and less than 0.2 is safe
    def change_infection_rate(self):
        if self.person_Num != 0:
            rate = self.infection_persons_rate
            self.infection_rate = self.infection_persons_count / self.person_Num
            if rate < 0.2 <= self.infection_rate or rate < 0.8 <= self.infection_rate:
                self.area_state_change(self)
            if rate >= 0.2 > self.infection_rate or rate >= 0.8 > self.infection_rate:
                self.area_state_change(self)

    def area_state_change(self):
        if self.infection_rate < 0.2:
            self.area_states = AreaStates.GREEN
        if 0.2 <= self.infection_rate < 0.8:
            self.area_states = AreaStates.ORANGE
        if self.area_states >= 0.8:
            self.area_states = AreaStates.RED
        World.changeColor(self)


class AreaStates(Enum):
    RED = 3  # dangerous
    ORANGE = 2  # risk
    GREEN = 1  # safe
