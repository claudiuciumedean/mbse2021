from enum import Enum
import random
import numpy as np
from .Wearable import Wearable
from .Area import Area
import math

class Person:
    def __init__(self):
        self.id = id
        # initialize with a random position
        self.width = 600    # an initial ones, which is should be calculated from World.py
        self.length = 1000
        self.x_pos = np.random.rand() * self.length  # length = World.size_y_prime - World.size_y
        self.y_pos = np.random.rand() * self.width  # width = World.size_x_prime - World.size_x
        self.temperature = 37.0
        self.oxygen = 99
        self.infected = False
        self.infection_severity = InfectionSeverity.GREEN

    def boundary_constraint(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

        # boundaries of left and right edges (x axis)
        if self.x_pos < 0:
            self.x_pos = self.x_pos + np.random.rand() * self.length
        elif self.x_pos > self.length:
            self.x_pos = self.x_pos - np.random.rand() * self.length

        # boundaries of up and down edges (y axis)
        if self.y_pos < 0:
            self.y_pos = self.y_pos + np.random.rand() * self.width
        elif self.y_pos > self.width:
            self.y_pos = self.y_pos - np.random.rand() * self.width

        return None

    def walk(self):
        self.x_pos += np.random.rand() * self.length
        self.y_pos += np.random.rand() * self.width
        self.boundary_constraint(self.x_pos, self.y_pos)
        return None

    def flee(self, x_pos, y_pos, x_pos_risk, y_pos_risk):
        self.x_pos = x_pos
        self.y_pos = y_pos

        # distance between person X and a risk person
        distance = math.sqrt((math.pow(x_pos - x_pos_risk, 2)+math.pow(y_pos - y_pos_risk, 2)))
        while distance <= 2:
            if self.x_pos-x_pos_risk < 0:
                self.x_pos -= np.random.randint(2, self.length)
            else:
                self.x_pos += np.random.randint(2, self.length)
            if self.y_pos-y_pos_risk < 0:
                self.y_pos -= np.random.randint(2, self.width)
            else:
                self.y_pos += np.random.randint(2, self.width)
            # check if location is within boundary and rectify the over-location
            self.boundary_constraint(self.x_pos, self.y_pos)
            distance = math.sqrt((math.pow(self.x_pos - x_pos_risk, 2) + math.pow(self.y_pos - y_pos_risk, 2)))

        return None

    def start_disease(self, temperature, oxygen):
        if temperature >= Disease_features.TEMPERATURE_WARN:
            # temperature >= 37.3 and oxygen <= 93, this person is infected
            if oxygen <= Disease_features.OXYGEN_UNSAFE:
                self.infection_severity = InfectionSeverity.RED
                self.infected = True
            # temperature >= 37.3 and oxygen > 93, this person is at risk of infected
            else:
                self.infection_severity = InfectionSeverity.ORANGE
                self.infected = False

        if temperature < Disease_features.TEMPERATURE_WARN:
            # temperature < 37.3 and oxygen < 95, this person is at risk of infected
            if oxygen < Disease_features.OXYGEN_SAFE:
                self.infection_severity = InfectionSeverity.ORANGE
                self.infected = False
            # temperature < 37.3 and oxygen > 95, this person is not infected
            else:
                self.infection_severity = InfectionSeverity.GREEN
                self.infected = False

        infected_situation = [self.infection_severity, self.infected]

        return infected_situation


class InfectionSeverity(Enum):
    RED = 3  # high
    ORANGE = 2  # medium
    GREEN = 1  # low


class Disease_features(Enum):
    TEMPERATURE_WARN = 37.3
    OXYGEN_UNSAFE = 93
    OXYGEN_SAFE = 95
