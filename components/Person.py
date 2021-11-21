import random
import uuid

# import Simulation_Manager
from Simulation_Constants import Simulation_Constants as sc
from Simulation_Constants import PersonStatus, PersonBehaviour

from .Wearable import Wearable

if sc.FIXED_SEED:
    random.seed(0)

class Person:
    def __init__(self, world, status=PersonStatus.HEALTHY, behaviour=PersonBehaviour.RETURNER):
        self.id = str(uuid.uuid4())
        self.wearable = Wearable(self)
        self.world = world;
        self.world_size = sc.WORLD_SIZE;
        self.x = random.uniform(0, sc.WORLD_SIZE)
        self.y = random.uniform(0, sc.WORLD_SIZE)
        self.x_pre = self.x
        self.y_pre = self.y

        self.status = status
        self.behaviour = behaviour
        self.start_behaviour = self.behaviour
        self.disease_started_time = 0
        self.walk_step = {PersonBehaviour.RETURNER: sc.WALK_STEP_RETURNERS,
                          PersonBehaviour.EXPLORER: sc.WALK_STEP_EXPLORERS,
                          PersonBehaviour.FLEE: 0,
                          PersonBehaviour.FREEZE: 0}[self.behaviour]
        self.temperature = sc.INITIAL_TEMPERATURE
        self.oxygen = sc.INITIAL_OXYGEN

    def walk(self):
        if self.behaviour == PersonBehaviour.FREEZE:
            return

        elif self.behaviour == PersonBehaviour.FLEE:
            self.x = self.x_pre
            self.y = self.y_pre
            self.behaviour = self.start_behaviour
            return

        else:
            self.x_pre = self.x
            self.y_pre = self.y
         
            self.x += random.uniform(-self.walk_step, self.walk_step)
            self.y += random.uniform(-self.walk_step, self.walk_step)

            if self.x > sc.WORLD_SIZE:
                self.x = sc.WORLD_SIZE
            if self.y > sc.WORLD_SIZE:
                self.y = sc.WORLD_SIZE
            if self.x < 0:
                self.x = 0
            if self.y < 0:
                self.y = 0

    def update_disease_status(self, time: int):

      if self.status == PersonStatus.INFECTED:

        if time < self.disease_started_time + sc.DISEASE_DURATION/2:
            self.temperature = random.uniform(37.5, 38.7)
            self.oxygen = random.uniform(92, 99)

        elif time < self.disease_started_time + sc.DISEASE_DURATION:
            self.temperature = random.uniform(38.5, 40)
            self.oxygen = random.uniform(85, 99) 
                
        else:
            if self.temperature >= 39.7 and self.oxygen <= 90:
                self.status = PersonStatus.DEAD
                self.behaviour = PersonBehaviour.FREEZE
                self.temperature = 0
                self.oxygen = 0
            else:
                self.status = PersonStatus.RECOVERED
                self.temperature = sc.INITIAL_TEMPERATURE
                self.oxygen = sc.INITIAL_OXYGEN         
