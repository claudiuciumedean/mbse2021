from enum import Enum
import random
import numpy as np
from .Wearable import Wearable
from .Area import Area
import math

class Person:
    def __init__(self):
        self.id = id
        self.x_pos = np.random.rand() * self.id  # initialize with a random position
        self.y_pos = np.random.rand() * self.id
        # self.location = np.array([self.x, self.y])
        self.temperature = 37.0
        self.oxygen = 99
        self.infected = False
        self.infection_severity = InfectionSeverity.GREEN

    def walk(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_pos += np.random.rand(1000, 600)
        self.y_pos += np.random.rand(1000, 600)
        return None

    def flee(self, x_pos, y_pos, x_pos_risk, y_pos_risk):
        self.x_pos = x_pos
        self.y_pos = y_pos

        distance = math.sqrt((math.pow(x_pos - x_pos_risk, 2)+math.pow(y_pos - y_pos_risk, 2)))
        if distance <= 2:
            if x_pos-x_pos_risk < 0:
                x_pos -= np.random.rand(2, 1000)
            else:
                x_pos += np.random.rand(2, 1000)
            if y_pos-y_pos_risk < 0:
                y_pos -= np.random.rand(2, 600)
            else:
                y_pos += np.random.rand(2, 600)

        return None

    def start_disease(self, temperature, oxygen):
        if temperature >= 37.3:
            if oxygen <= 93:
                self.infection_severity = InfectionSeverity.RED
                self.infected = True
            if 93 < oxygen < 95:
                self.infection_severity = InfectionSeverity.ORANGE
                self.infected = False
            if oxygen >= 95:
                self.infection_severity = InfectionSeverity.GREEN
                self.infected = False
        if oxygen < 93:
            if temperature >= 37.3:
                self.infection_severity = InfectionSeverity.RED
                self.infected = True
            else:
                self.infected = False

        return self.infected


class InfectionSeverity(Enum):
    RED = 3  # high
    ORANGE = 2  # medium
    GREEN = 1  # low
