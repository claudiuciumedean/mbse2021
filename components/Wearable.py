from Simulation_Constants import Simulation_Constants, InfectionSeverity, Disease_features

# import Simulation_Manager
# from .Person import Person


class Wearable:
    """Class Wearable:
        Basic instruction:
        1) Create a new object
        2) Assign it to a person
        3) Call main()
        4) Repeat from point 3
    """

    def __init__(self, person, world):
        self.person = person
        self.world = world
        self.user_risk_level = 0
        self.temperature = Simulation_Constants.INITIAL_TEMPERATURE
        self.oxygen = Simulation_Constants.INITIAL_TEMPERATURE

    def distance(self, person) -> float:
        """Returns the distance between self and the given wearable (object)"""
        return dist(self.person.x_pos, self.person.y_pos, person.x_pos, person.y_pos)

    def compute_close_persons(self, persons: list, radius: float):
        close_persons = []

        for person in persons:
            if self.distance(person) < radius and person != self.person:
                close_persons.append(person)
        
        return close_persons

    def check_temperature(self, time: int):
        """Check temperature level."""
        if self.person.infected:
            self.temperature = 39

        else:
            self.temperature = Simulation_Constants.INITIAL_TEMPERATURE

    def check_oxygen(self, time: int):
        """Check oxygen level."""
        if self.person.infected:
            self.oxygen = 92

        else:
            self.oxygen = Simulation_Constants.INITIAL_OXYGEN

    def compute_risk_level(self, persons: list):
        """Compute the user risk level"""
        risk_counter = 0

        # Points from temperature
        risk_counter += [l < self.temperature <= h for l, h in Disease_features.TEMP_RANGES].index(True)

        # Points from SpO2
        if self.oxygen < Disease_features.OXYGEN_THRESHOLD:
            risk_counter += 1

        # Points from close contacts
        max_contact_risk = 0
        for person in self.compute_close_persons(persons, Simulation_Constants.WEARABLE_DANGER_RADIUS):
            #print(person.wearable.user_risk_level)
            if person.wearable.user_risk_level > max_contact_risk:
                max_contact_risk = person.wearable.user_risk_level
        risk_counter += max_contact_risk

        #Compute risk level
        if risk_counter < 2:
            self.user_risk_level = InfectionSeverity.GREEN
        elif risk_counter < 4:
            self.user_risk_level = InfectionSeverity.ORANGE
        else:
            self.user_risk_level = InfectionSeverity.RED

    def emit_warning(self, persons: list, radius: float = 10):
        """self.person flees if there is a high risk person in the "warning" radius.
        """
        if self.user_risk_level != InfectionSeverity.GREEN:
            return

        for p in self.compute_close_persons(persons, Simulation_Constants.WEARABLE_WARNING_RADIUS):
            if p.wearable.user_risk_level == InfectionSeverity.RED:
                self.person.flee2()
                break

    def main(self, persons: list, time: int):

        #check paramters of the person
        self.check_temperature(time)
        self.check_oxygen(time)

        #compute the risk level
        self.compute_risk_level(persons)

        #emit the warning for the user (which in turn calls flee)
        self.emit_warning(persons)


# Utility functions

def dist(x1: float, y1: float, x2: float, y2: float) -> float:
    """Distance between two points."""
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
