import random
from Simulation_Constants import Simulation_Constants as sc
from Simulation_Constants import InfectionSeverity, Disease_features
from Simulation_Constants import PersonStatus, PersonBehaviour

if sc.FIXED_SEED:
    random.seed(0)

class Wearable:

    def __init__(self, person):
        self.person = person
        self.user_risk_level = 0
        self.old_risk_counter = 0

    def distance(self, person) -> float:
        """Returns the distance between self and the given wearable (object)"""
        return dist(self.person.x, self.person.y, person.x, person.y)

    def compute_close_persons(self, persons: list, radius: float):
        close_persons = []

        for person in persons:
            if self.distance(person) < radius and person != self.person:
                close_persons.append(person)
        
        return close_persons

    def compute_risk_level(self, persons: list):
        """Compute the user risk level"""

        risk_counter = 0

        # Points from temperature
        risk_counter += [l < self.person.temperature <= h for l, h in Disease_features.TEMP_RANGES].index(True)

        # Points from SpO2
        if self.person.oxygen < Disease_features.OXYGEN_THRESHOLD:
            risk_counter += 1

        # Points from close contacts
        max_contact_risk = 0
        for person in self.compute_close_persons(persons, sc.WEARABLE_DANGER_RADIUS):
            #print(person.wearable.user_risk_level)
            if person.wearable.user_risk_level > max_contact_risk:
                max_contact_risk = person.wearable.user_risk_level
        risk_counter += max_contact_risk

        # Risk counter is decreased slowly in time
        if risk_counter < self.old_risk_counter:
            risk_counter = self.old_risk_counter-1
        self.old_risk_counter = risk_counter

        #Compute risk level
        if risk_counter < 2:
            self.user_risk_level = InfectionSeverity.GREEN
        elif risk_counter < 4:
            self.user_risk_level = InfectionSeverity.ORANGE
        else:
            self.user_risk_level = InfectionSeverity.RED

    def emit_warning(self, persons: list):
        """self.person flees if there is a high risk person in the "warning" radius.
        """
        if random.random() < sc.REBEL_PERCENTAGE:
            return
        if self.user_risk_level == InfectionSeverity.RED:
            self.person.walk_step = {PersonBehaviour.RETURNER: sc.WALK_STEP_RETURNERS/10,
                                     PersonBehaviour.EXPLORER: sc.WALK_STEP_EXPLORERS/2,
                                     PersonBehaviour.FLEE: 0,
                                     PersonBehaviour.FREEZE: 0}[self.person.behaviour]

        elif self.user_risk_level == InfectionSeverity.ORANGE:
            self.person.walk_step = {PersonBehaviour.RETURNER: sc.WALK_STEP_RETURNERS/5,
                                     PersonBehaviour.EXPLORER: sc.WALK_STEP_EXPLORERS,
                                     PersonBehaviour.FLEE: 0,
                                     PersonBehaviour.FREEZE: 0}[self.person.behaviour]

        else:
            self.person.walk_step = {PersonBehaviour.RETURNER: sc.WALK_STEP_RETURNERS,
                                     PersonBehaviour.EXPLORER: sc.WALK_STEP_EXPLORERS,
                                     PersonBehaviour.FLEE: 0,
                                     PersonBehaviour.FREEZE: 0}[self.person.behaviour]

            for p in self.compute_close_persons(persons, sc.WEARABLE_WARNING_RADIUS):
                if p.wearable.user_risk_level == InfectionSeverity.RED:
                    self.person.behaviour = PersonBehaviour.FLEE
                    break

    def main(self, persons: list):
        if self.person.status == PersonStatus.DEAD:
            self.user_risk_level = 0
            return

        #compute the risk level
        self.compute_risk_level(persons)

        #emit the warning for the user (which in turn calls flee)
        if sc.DEVICE_ACTIVE:
            self.emit_warning(persons)  


# Utility functions

def dist(x1: float, y1: float, x2: float, y2: float) -> float:
    """Distance between two points."""
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
