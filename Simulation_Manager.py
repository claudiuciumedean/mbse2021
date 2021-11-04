import simpy
import time
import random
import uuid
import tkinter as tk

from components.World import World
from components.Person import Person
from CSV_Writer import CSV_Writer


class Simluation_Manager:
    def __init__(self):
        self.env = None
        self.world = None
        self.csv_writer = CSV_Writer(str(uuid.uuid1()))
        self.simulation_iteration = 0

    def start(self):
        persons = []
        for i in range(0, 300):
            persons.append(Person())
        persons[random.randint(0, 49)].infected = True
        persons[random.randint(0, 49)].infected = True

        self.world = World(persons)
        # self.env = simpy.rt.RealtimeEnvironment(factor = .20) #factor of 1 simulation runs a process every second, 0.5 factor 2 processes every second and so on
        self.env = simpy.Environment()
        self.env.process(self.run())
        self.env.run(until=100)

        self.logSimulationStats()

    def run(self):
        while True:
            #print('iter: ', self.simulation_iteration)
            self.logSimulationStats()
            self.world.live(self.simulation_iteration)
            yield self.env.timeout(1)  # timeout for a second

    def logSimulationStats(self):
        self.simulation_iteration += 1
        infectedPersons = 0
        healthyPersons = 0
        recoveredPersons = 0

        for person in self.world.persons:
            if person.infected:
                infectedPersons += 1
            else:
                healthyPersons += 1
            if person.recovered:
                recoveredPersons += 1

        print('iter: ', self.simulation_iteration, ', stats: ', healthyPersons, infectedPersons, recoveredPersons)
        self.csv_writer.write_row([healthyPersons, infectedPersons, recoveredPersons, self.simulation_iteration])

    def register_logs(self):
        return None


sim_manager = Simluation_Manager()
sim_manager.start()

print('Simulation finished')
