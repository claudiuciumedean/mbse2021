import simpy
import time
import random
import uuid
import tkinter as tk

class Person:
  def __init__(self):
    self.id = uuid.uuid4()
    self.x = 0
    self.y = 0
    self.infected = False

  def walk(self):
    self.x += 1
    self.y += 1
    print("I person" + str(self.id) + " am walking on X " + str(self.x) + " and on Y " + str(self.y))

  def check_wearable(self):
    print("Checking my smarty smart watch")

class Simluation_Manager:
  def __init__(self):
    self.env = None
    self.world = None
    self.simulation_time = 0
    self.infected_persons = []
    self.healthy_persons = []
  
  def start(self):
    self.env = simpy.rt.RealtimeEnvironment(factor = 1) #factor of 1 simulation runs a process every second, 0.5 factor 2 processes every second and so on
    self.env.process(self.run())
    self.env.run(until=20)

  def run(self):
    persons = []
    for x in range(200):
      persons.append(Person())

    while True:
      for person in persons:
        person.walk()

      yield self.env.timeout(1) #timeout for a second

      for person in persons:
        person.check_wearable()

      yield self.env.timeout(1)

  def warn_persons(self, coordinates):
    return None
  
  def stop(self):
    return None
  
  def register_logs(self):
    return None

sim_manager = Simluation_Manager()
sim_manager.start()