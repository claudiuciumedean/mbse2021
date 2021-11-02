import random

from components.Area import Area
from Simulation_Constants import Simulation_Constants

class World:  
    def __init__(self):
        self.frame_size_x = Simulation_Constants.WORLD_SIZE
        self.frame_size_y = Simulation_Constants.WORLD_SIZE
        self.persons = None
        self.areas = []

        self.create_areas()
    
    def person_active(self):
        for person in self.persons:
            person.walk()
            person.wearable.compute_close_persons(self.persons)

    def create_areas(self):
        areas = [
            {
                "x": 0,
                "x_prime": 100,
                "y": 0,
                "y_prime": 100,
                "infection_rate": 0.8 
            },
            {
                "x": 200,
                "x_prime": 300,
                "y": 0,
                "y_prime": 100,
                "infection_rate": 0.1
            },
            {
                "x": 400,
                "x_prime": 500,
                "y": 0,
                "y_prime": 100,
                "infection_rate": 0.5
            },
            {
                "x": 0,
                "x_prime": 100,
                "y": 400,
                "y_prime": 500,
                "infection_rate": 0.9
            },
            {
                "x": 200,
                "x_prime": 300,
                "y": 400,
                "y_prime": 500,
                "infection_rate": 0.4
            },
            {
                "x": 400,
                "x_prime": 500,
                "y": 400,
                "y_prime": 500,
                "infection_rate": 0.15
            }
        ]

        for area in areas:
            self.areas.append(
                Area(
                    area["x"],
                    area["x_prime"],
                    area["y"],
                    area["y_prime"],
                    area["infection_rate"]
                )
            )

    def get_in_area(self, x, y):
        for area in self.areas:
            if area.is_in_area(x, y):
                return area

        return None

    def close_persons_detected(self, person_1, person_2):
        if not person_1.infected and (not person_2.infected):
           return
        
        area_1 = self.get_in_area(person_1.x_pos, person_1.y_pos)
        area_2 = self.get_in_area(person_2.x_pos, person_2.y_pos)

        if area_1 != None and area_2 != None and area_1.id == area_2.id:
            infected = random.random() < area_1.infection_rate == 0 if False else True

            if not person_1.infected:
                person_1.infected = infected

            if not person_2.infected:
                person_1.infected = infected

        else:
            infected = random.random() < 0.1 == 0 if False else True

            if not person_1.infected:
                person_1.infected = infected

            if not person_2.infected:
                person_1.infected = infected



