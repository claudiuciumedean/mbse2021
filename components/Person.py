import random
import numpy as np
import math
import uuid


from enum import Enum

import Simulation_Manager
from Simulation_Constants import Simulation_Constants
from .Area import Area
from .Wearable import Wearable

class Person:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.wearable = Wearable(self)
        self.world_size = Simulation_Constants.WORLD_SIZE
        self.x_pos = random.randint(0, Simulation_Constants.WORLD_SIZE)
        self.y_pos = random.randint(0, Simulation_Constants.WORLD_SIZE)
        self.infected = False
        self.infection_severity = InfectionSeverity.GREEN
        self.disease_started_time = 0



    def walk(self):
        if self.x_pos < Simulation_Constants.WORLD_SIZE and self.y_pos < Simulation_Constants.WORLD_SIZE and self.x_pos > 0 and self.y_pos > 0:
            self.x_pos += random.choice([-1, 1])
            self.y_pos += random.choice([-1, 1])

        elif self.x_pos == Simulation_Constants.WORLD_SIZE or self.y_pos == Simulation_Constants.WORLD_SIZE and self.x_pos > 0 and self.y_pos > 0:
            self.x_pos -= 1
            self.y_pos += 1

        elif self.x_pos < Simulation_Constants.WORLD_SIZE and self.y_pos < Simulation_Constants.WORLD_SIZE and self.x_pos == 0 and self.y_pos == 0:
            self.x_pos += 1
            self.y_pos += 1

        #print(self.id + " x-" + str(self.x_pos) + " y-" + str(self.y_pos))

    def update_disease_status(self):
        if Simulation_Manager.simulation_iteration > self.disease_started_time + Simulation_Constants.DISEASE_DURATION and self.infected == True:
            self.infected = False



        # if temperature >= Disease_features.TEMPERATURE_WARN:
        #     # temperature >= 37.3 and oxygen <= 93, this person is infected
        #     if oxygen <= Disease_features.OXYGEN_UNSAFE:
        #         self.infection_severity = InfectionSeverity.RED
        #         self.infected = True
        #     # temperature >= 37.3 and oxygen > 93, this person is at risk of infected
        #     else:
        #         self.infection_severity = InfectionSeverity.ORANGE
        #         self.infected = False
        #
        # if temperature < Disease_features.TEMPERATURE_WARN:
        #     # temperature < 37.3 and oxygen < 95, this person is at risk of infected
        #     if oxygen < Disease_features.OXYGEN_SAFE:
        #         self.infection_severity = InfectionSeverity.ORANGE
        #         self.infected = False
        #     # temperature < 37.3 and oxygen > 95, this person is not infected
        #     else:
        #         self.infection_severity = InfectionSeverity.GREEN
        #         self.infected = False
        #
        # infected_situation = [self.infection_severity, self.infected]
        #
        # return infected_situation
    
    def flee(self):   
        if self.x_pos + Simulation_Constants.FLEE_DIST < Simulation_Constants.WORLD_SIZE and self.y_pos + Simulation_Constants.FLEE_DIST  < Simulation_Constants.WORLD_SIZE and self.x_pos - Simulation_Constants.FLEE_DIST  > 0 and self.y_pos - Simulation_Constants.FLEE_DIST  > 0:
            self.x_pos += random.choice([-Simulation_Constants.FLEE_DIST , Simulation_Constants.FLEE_DIST ])
            self.y_pos += random.choice([-Simulation_Constants.FLEE_DIST , Simulation_Constants.FLEE_DIST ])

        elif self.x_pos + Simulation_Constants.FLEE_DIST >= Simulation_Constants.WORLD_SIZE or self.y_pos + Simulation_Constants.FLEE_DIST >= Simulation_Constants.WORLD_SIZE and self.x_pos - Simulation_Constants.FLEE_DIST > 0 and self.y_pos - Simulation_Constants.FLEE_DIST  > 0:
            self.x_pos += -Simulation_Constants.FLEE_DIST 
            self.y_pos += -Simulation_Constants.FLEE_DIST 

        elif self.x_pos + Simulation_Constants.FLEE_DIST < Simulation_Constants.WORLD_SIZE and self.y_pos + Simulation_Constants.FLEE_DIST < Simulation_Constants.WORLD_SIZE and self.x_pos - Simulation_Constants.FLEE_DIST <= 0 and self.y_pos - Simulation_Constants.FLEE_DIST <= 0:
            self.x_pos += Simulation_Constants.FLEE_DIST 
            self.y_pos += Simulation_Constants.FLEE_DIST 

        # distance between person X and a risk person
        #distance = math.sqrt((math.pow(x_pos - x_pos_risk, 2)+math.pow(y_pos - y_pos_risk, 2)))
        #while distance <= 2:
        #    if self.x_pos-x_pos_risk < 0:
        #        self.x_pos -= np.random.randint(2, self.length)
        #    else:
        #        self.x_pos += np.random.randint(2, self.length)
        #    if self.y_pos-y_pos_risk < 0:
        #        self.y_pos -= np.random.randint(2, self.width)
        #    else:
        #        self.y_pos += np.random.randint(2, self.width)
        #    # check if location is within boundary and rectify the over-location
        #    self.boundary_constraint(self.x_pos, self.y_pos)
        #    distance = math.sqrt((math.pow(self.x_pos - x_pos_risk, 2) + math.pow(self.y_pos - y_pos_risk, 2)))


class InfectionSeverity(Enum):
    RED = 3  # high
    ORANGE = 2  # medium
    GREEN = 1  # low


class Disease_features(Enum):
    TEMPERATURE_WARN = 37.3
    OXYGEN_UNSAFE = 93
    OXYGEN_SAFE = 95
