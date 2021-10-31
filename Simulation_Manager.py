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
    for i in range(0, 1000):
      persons.append(Person())
    persons[random.randint(0, 49)].infected = True
    persons[random.randint(0, 49)].infected = True

    self.world = World(persons)
    #self.env = simpy.rt.RealtimeEnvironment(factor = .20) #factor of 1 simulation runs a process every second, 0.5 factor 2 processes every second and so on
    self.env = simpy.Environment()
    self.env.process(self.run())
    self.env.run(until=2)

    self.logSimulationStats()

  def run(self):
    while True:

      self.world.live()
      self.logSimulationStats()
      yield self.env.timeout(1) #timeout for a second


  def logSimulationStats(self):
    self.simulation_iteration += 1
    infectedPersons = 0
    healthyPersons = 0

    for person in self.world.persons:
      if person.infected:
        infectedPersons += 1
      else:
        healthyPersons += 1

    self.csv_writer.write_row([healthyPersons, infectedPersons, self.simulation_iteration])    

  
  def register_logs(self):
    return None

sim_manager = Simluation_Manager()
sim_manager.start()