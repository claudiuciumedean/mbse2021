from .Person import Person, InfectionSeverity

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

    def __init__(self):
        self.person = None

        self.user_risk_level = InfectionSeverity.GREEN

        self.temperature = None
        self.oxygen = None

    def assign_user(self, person):
        """Assign the wearable to the given person
        """
        self.person = person

    def distance(self, wearable) -> float:
        """Return the distance between self and the given wearable (object)
        """
        return dist(self.person.x_pos, self.person.y_pos,
                    wearable.person.x_pos, wearable.person.y_pos)

    def get_close_users(self, wearables: list, radious: float):
        """Yields all the people inside the given radious.
        """
        for w in wearables:
            if self.distance(w) < radious:
                yield w

    def check_temperature(self):
        """Check temperature level.
        """
        self.temperature = self.person.temperature

    def check_oxygen(self):
        """Check oxygen level.
        """
        self.oxygen = self.person.oxygen

    def compute_risk_level(self, wearables: list, radious: float = 2):
        """Compute the user risk level
        """
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


#Utility functions

def dist(x1: float, y1: float, x2: float, y2: float) -> float:
    """Distance between two points.
    """
    return ((x2-x1)**2 + (y2-y1)**2)**0.5


if __name__ == "__main__":
    print("Some test:")
    #TODO
