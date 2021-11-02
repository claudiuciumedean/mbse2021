from Simulation_Constants import Simulation_Constants

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
        self.user_risk_level = None
        self.temperature = Simulation_Constants.INITIAL_TEMPERATURE
        self.oxygen = Simulation_Constants.INITIAL_TEMPERATURE

    def distance(self, wearable) -> float:
        """Return the distance between self and the given wearable (object)"""
        return dist(self.person.x_pos, self.person.y_pos, wearable.person.x_pos, wearable.person.y_pos)

    def get_close_persons(self, persons: list):
        """Yields all the people inside a given circle."""
        close_persons = []
        
        for person in persons:
            if in_circle(self.person.x_pos, self.person.y_pos, Simulation_Constants.WEARABLE_COMMUNICATION_RADIUS, person.x_pos, person.y_pos):
                close_persons.append(person)
                
                if person.infected and not self.person.infected:
                    self.person.infected = True
                elif (not person.infected) and self.person.infected:
                    person.infected = True
                    person.deases_started = simulation_time

                #print(f"{self.person.id} ({self.person.x_pos}, {self.person.y_pos}) and {person.id} ({person.x_pos}, {person.y_pos}) are in the same radius")
        
        return close_persons

    def check_temperature(self):
        """Check temperature level."""
        person.update_desease_status()

        if person.infected:
            self.temperature = 39
        else:
            self.temperature = Simulation_Constants.INITIAL_TEMPERATURE

    def check_oxygen(self):
        """Check oxygen level."""
        person.update_desease_status()

        if person.infected:
            self.temperature = 92
        else:
            self.temperature = Simulation_Constants.INITIAL_OXYGEN

    def compute_risk_level(self, wearables: list, radious: float = 2):
        """Compute the user risk level"""
        risk_counter = 0

        #Points from temperature
        ranges = [(0, 37.3), (37.3, 38.2), (38.2, 39), (39, 50)]
        risk_counter += [l < self.temperature <= h for l, h in ranges].index(True)

        #Points from SpO2
        if self.oxygen < 95:
            risk_counter += 1

        #Points from close contacts
        max_contact_risk = 0
        for wearable in self.get_close_users(wearables, radious):
            if wearable.user_risk_level > max_contact_risk:
                max_contact_risk = wearable.user_risk_level
        risk_counter += max_contact_risk

        #Compute risk level
        if risk_counter < 2:
            self.user_risk_level = InfectionSeverity.GREEN
        elif risk_counter < 4:
            self.user_risk_level = InfectionSeverity.ORANGE
        else:
            self.user_risk_level = InfectionSeverity.RED

    def emit_warning(self, wearables: list, radious: float = 10) -> bool:
        """Return True if there is an high risk user inside the given radious,
           False otherwise.
        """
        for w in self.get_close_users(wearables, radious):
            if w.user_risk_level == InfectionSeverity.RED:
                return True
        return False

    def main(self):
        #list of all the persons inside a circle <- get_close_persons()
        #computerisklevel()
        #update infected()
        #emit warning() -> flee



        pass


#Utility functions

def dist(x1: float, y1: float, x2: float, y2: float) -> float:
    """Distance between two points."""
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def in_circle(center_x, center_y, radius, x, y):
    """Checks if two given points are inside a circle between two points."""
    square_dist = (center_x - x) ** 2 + (center_y - y) ** 2
    return square_dist <= radius ** 2