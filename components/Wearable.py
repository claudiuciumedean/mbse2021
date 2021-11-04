from Simulation_Constants import Simulation_Constants
from Simulation_Constants import InfectionSeverity


# import Simulation_Manager
# from .Person import Person


class Wearable:
    """Class Wearable:
        Basic instruction:
        1) Create a new object
        2) Assign it to a person
        3) Call check_temperature(), check_oxygen()
        4) Call compute_risk_level() to update the user risk level
        5) Call emit_warning() to check for nearby high risk people
        6) Repeat from point 3
    """

    def __init__(self, person):
        self.person = person
        self.user_risk_level = 0
        self.temperature = Simulation_Constants.INITIAL_TEMPERATURE
        self.oxygen = Simulation_Constants.INITIAL_TEMPERATURE

    def distance(self, person) -> float:
        """Return the distance between self and the given wearable (object)"""
        return dist(self.person.x_pos, self.person.y_pos, person.x_pos, person.y_pos)

    def get_close_persons(self, persons: list, radious: float = Simulation_Constants.WEARABLE_COMMUNICATION_RADIUS):
        """Yields all the people inside a given circle."""
        close_persons = []

        for person in persons:
            if self.distance(person) < radious and person != self.person:
                close_persons.append(person)

                # print(f"{self.person.id} ({self.person.x_pos}, {self.person.y_pos}) and {person.id} ({person.x_pos}, {person.y_pos}) are in the same radius")

        return close_persons

    def update_infected(self, person, time):
        if person.infected and not self.person.infected and not self.person.recovered:
            self.person.infected = True
            self.person.disease_started_time = time
        elif (not person.infected) and (not person.recovered) and self.person.infected:
            person.infected = True
            person.disease_started_time = time

    def check_temperature(self, time: int):
        """Check temperature level."""
        self.person.update_disease_status(time)

        if self.person.infected:
            self.temperature = 39
        else:
            self.temperature = Simulation_Constants.INITIAL_TEMPERATURE

    def check_oxygen(self, time: int):
        """Check oxygen level."""
        self.person.update_disease_status(time)

        if self.person.infected:
            self.oxygen = 92
        else:
            self.oxygen = Simulation_Constants.INITIAL_OXYGEN

    def compute_risk_level(self, persons: list):
        """Compute the user risk level"""
        risk_counter = 0

        # Points from temperature
        ranges = [(0, 37.3), (37.3, 38.2), (38.2, 39), (39, 50)]
        risk_counter += [l < self.temperature <= h for l, h in ranges].index(True)

        # Points from SpO2
        if self.oxygen < 95:
            risk_counter += 1

        # Points from close contacts
        max_contact_risk = 0
        for person in persons:
            #print(person.wearable.user_risk_level)
            if person.wearable.user_risk_level > max_contact_risk:
                max_contact_risk = person.wearable.user_risk_level
        risk_counter += max_contact_risk

        #Compute risk level
        if risk_counter < 2:
            self.user_risk_level = InfectionSeverity.GREEN.value
        elif risk_counter < 4:
            self.user_risk_level = InfectionSeverity.ORANGE.value
        else:
            self.user_risk_level = InfectionSeverity.RED.value

    def emit_warning(self, persons: list, radious: float = 10):
        """Return True if there is an high risk user inside the given radious,
           False otherwise.
        """
        for p in self.get_close_persons(persons, 2*Simulation_Constants.WEARABLE_COMMUNICATION_RADIUS):
            if p.wearable.user_risk_level == InfectionSeverity.RED.value:
                self.person.flee()
                break

    def main(self, persons: list, time: int):
        close_persons = self.get_close_persons(persons)

        self.check_temperature(time)
        self.check_oxygen(time)

        self.compute_risk_level(close_persons)

        for person in close_persons:
            self.update_infected(person, time)

        self.emit_warning(persons)


# Utility functions

def dist(x1: float, y1: float, x2: float, y2: float) -> float:
    """Distance between two points."""
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def in_circle(center_x, center_y, radius, x, y):
    """Checks if two given points are inside a circle between two points."""
    square_dist = (center_x - x) ** 2 + (center_y - y) ** 2
    return square_dist <= radius ** 2
