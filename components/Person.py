import random
import numpy as np
import math
import uuid

# import Simulation_Manager
from Simulation_Constants import Simulation_Constants
from Simulation_Constants import InfectionSeverity
from Simulation_Constants import Disease_features

# from .Area import Area
from .Wearable import Wearable

if Simulation_Constants.FIXED_SEED:
    random.seed(0)

class Person:
    def __init__(self, world):
        self.id = str(uuid.uuid4())
        self.wearable = Wearable(self, world)
        self.world_size = Simulation_Constants.WORLD_SIZE;
        self.x_pos = random.randint(0, Simulation_Constants.WORLD_SIZE)
        self.y_pos = random.randint(0, Simulation_Constants.WORLD_SIZE)
        self.x_pre_pos = self.x_pos
        self.y_pre_pos = self.y_pos
        self.infected = False
        self.recovered = False
        # self.infection_severity = InfectionSeverity.GREEN
        self.disease_started_time = 0
        self.infection_severity = InfectionSeverity.GREEN
        self.world = world;

    def walk(self):
        self.x_pre_pos = self.x_pos
        self.y_pre_pos = self.y_pos
        if self.x_pos < Simulation_Constants.WORLD_SIZE and self.y_pos < Simulation_Constants.WORLD_SIZE and self.x_pos > 0 and self.y_pos > 0:
            self.x_pos += random.choice([-1, 1])
            self.y_pos += random.choice([-1, 1])

        elif self.x_pos == Simulation_Constants.WORLD_SIZE or self.y_pos == Simulation_Constants.WORLD_SIZE and self.x_pos > 0 and self.y_pos > 0:
            self.x_pos -= 1
            self.y_pos += 1

        elif self.x_pos < Simulation_Constants.WORLD_SIZE and self.y_pos < Simulation_Constants.WORLD_SIZE and self.x_pos == 0 and self.y_pos == 0:
            self.x_pos += 1
            self.y_pos += 1

        # print(self.id + " x-" + str(self.x_pos) + " y-" + str(self.y_pos))

    def walk2(self):
        self.x_pre_pos = self.x_pos
        self.y_pre_pos = self.y_pos

        new_x_pos = self.x_pos + int(random.gauss(0, 5))
        new_y_pos = self.y_pos + int(random.gauss(0, 5))

        if new_x_pos > Simulation_Constants.WORLD_SIZE:
            new_x_pos = Simulation_Constants.WORLD_SIZE
        if new_y_pos > Simulation_Constants.WORLD_SIZE:
            new_y_pos = Simulation_Constants.WORLD_SIZE
        if new_x_pos < 0:
            new_x_pos = 0
        if new_y_pos < 0:
            new_y_pos = 0

        self.x_pos = new_x_pos
        self.y_pos = new_y_pos

    def update_disease_status(self, persons: list, time: int):
        for person in self.wearable.compute_close_persons(persons, Disease_features.INFECTION_RADIUS):
            self.world.close_persons_detected(self, person, time)

        #disease ends for self
        if time > self.disease_started_time + Simulation_Constants.DISEASE_DURATION and self.infected:
            self.infected = False
            self.recovered = True

    def flee(self):
        if self.x_pos + Simulation_Constants.FLEE_DIST < Simulation_Constants.WORLD_SIZE and self.y_pos + Simulation_Constants.FLEE_DIST < Simulation_Constants.WORLD_SIZE and self.x_pos - Simulation_Constants.FLEE_DIST > 0 and self.y_pos - Simulation_Constants.FLEE_DIST > 0:
            self.x_pos += random.choice([-Simulation_Constants.FLEE_DIST, Simulation_Constants.FLEE_DIST])
            self.y_pos += random.choice([-Simulation_Constants.FLEE_DIST, Simulation_Constants.FLEE_DIST])

        elif self.x_pos + Simulation_Constants.FLEE_DIST >= Simulation_Constants.WORLD_SIZE or self.y_pos + Simulation_Constants.FLEE_DIST >= Simulation_Constants.WORLD_SIZE and self.x_pos - Simulation_Constants.FLEE_DIST > 0 and self.y_pos - Simulation_Constants.FLEE_DIST > 0:
            self.x_pos += -Simulation_Constants.FLEE_DIST
            self.y_pos += -Simulation_Constants.FLEE_DIST

        elif self.x_pos + Simulation_Constants.FLEE_DIST < Simulation_Constants.WORLD_SIZE and self.y_pos + Simulation_Constants.FLEE_DIST < Simulation_Constants.WORLD_SIZE and self.x_pos - Simulation_Constants.FLEE_DIST <= 0 and self.y_pos - Simulation_Constants.FLEE_DIST <= 0:
            self.x_pos += Simulation_Constants.FLEE_DIST
            self.y_pos += Simulation_Constants.FLEE_DIST

    def flee2(self):
        self.x_pos = self.x_pre_pos
        self.y_pos = self.y_pre_pos
