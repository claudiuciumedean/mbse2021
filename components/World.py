import random

from components.Area import Area
from Simulation_Constants import Simulation_Constants as sc
from Simulation_Constants import Disease_features
from Simulation_Constants import PersonStatus


if sc.FIXED_SEED:
    random.seed(0)

class World:  
    def __init__(self):
        self.frame_size_x = sc.WORLD_SIZE
        self.frame_size_y = sc.WORLD_SIZE
        self.persons = None
        self.areas = []
        self.counter = {PersonStatus.HEALTHY: 0,
                        PersonStatus.INFECTED: 0,
                        PersonStatus.DEAD: 0,
                        PersonStatus.RECOVERED: 0}
        self.create_areas()
    
    def live(self, time: int):
        self.counter = {PersonStatus.HEALTHY: 0,
                        PersonStatus.INFECTED: 0,
                        PersonStatus.DEAD: 0,
                        PersonStatus.RECOVERED: 0}

        for person in self.persons:
            self.counter[person.status] += 1 
            person.walk()

        for person in self.persons:
            for close_person in person.wearable.compute_close_persons(self.persons, Disease_features.INFECTION_RADIUS):
                self.close_persons_detected(person, close_person, time)

        for person in self.persons:
            person.update_disease_status(time)

        for person in self.persons:
            person.wearable.main(self.persons)

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
                "y": 200,
                "y_prime": 300,
                "infection_rate": 0.45
            },
            {
                "x": 200,
                "x_prime": 300,
                "y": 200,
                "y_prime": 300,
                "infection_rate": 0.9
            },
            {
                "x": 400,
                "x_prime": 500,
                "y": 200,
                "y_prime": 300,
                "infection_rate": 0.2
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

    def close_persons_detected(self, person_1, person_2, time):
        if person_1.status != PersonStatus.INFECTED and person_2.status != PersonStatus.INFECTED:
           return
        
        area_1 = self.get_in_area(person_1.x, person_1.y)
        area_2 = self.get_in_area(person_2.x, person_2.y)
        infection_prob =  area_1.infection_rate if area_1 != None and area_2 != None and area_1.id == area_2.id else 0.1

        infected = True if random.random() < infection_prob else False

        if person_1.status == PersonStatus.HEALTHY and infected:
            person_1.status = PersonStatus.INFECTED
            person_1.disease_started_time = time

        if person_2.status == PersonStatus.HEALTHY and infected:
            person_2.status = PersonStatus.INFECTED
            person_2.disease_started_time = time

