import simpy
import time
import random
import uuid
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from components.World import World
from components.Person import Person
from CSV_Writer import CSV_Writer
from Simulation_Constants import Simulation_Constants as SC


if SC.FIXED_SEED:
    random.seed(0)

class Simluation_Manager:
  def __init__(self):
    self.env = None
    self.world = None
    self.csv_writer = CSV_Writer(str(uuid.uuid1()))
    self.simulation_iteration = 0
    self.history = []
  
  def start(self):
    self.world = World()
    persons = []

    for i in range(0, SC.POP_SIZE):
      if i%2==0 and SC.POP_RATIO == 1:
        person = Person(self.world, True)
      else:
        person = Person(self.world, False)
      persons.append(person)

    persons[0].infected = True
    self.world.persons = persons

    #self.env = simpy.rt.RealtimeEnvironment(factor = .10) #factor of 1 simulation runs a process every second, 0.5 factor 2 processes every second and so on
    self.env = simpy.Environment()
    self.env.process(self.run())
    self.env.run(until=(24//SC.TIME_STEP)*SC.DAYS_SIMULATED)
    self.logSimulationStats()

  def run(self):
      plt.rcParams["figure.figsize"] = (5, 6)
      while True:
        self.update_history()
        self.plot_world()
        if self.simulation_iteration % (24//SC.TIME_STEP) == 0:
            self.logSimulationStats() 
        self.world.daily_infected_counter = 0
        self.world.live(self.simulation_iteration)

        self.simulation_iteration += 1
        yield self.env.timeout(1)  # timeout for a second

  def plot_world(self):
    """Plot the positions of the persons in the world, and their current status as color.
    """
    plt.clf()
    plt.subplot2grid((4, 1), (0, 0), rowspan=2)

    plt.gca().add_patch(Rectangle((0, 0), 100, 100, linewidth=1, edgecolor='r', facecolor='none'))
    plt.gca().add_patch(Rectangle((200, 0), 100, 100, linewidth=1, edgecolor='g', facecolor='none'))
    plt.gca().add_patch(Rectangle((400, 0), 100, 100, linewidth=1, edgecolor='y', facecolor='none'))

    plt.gca().add_patch(Rectangle((0, 200), 100, 100, linewidth=1, edgecolor='y', facecolor='none'))
    plt.gca().add_patch(Rectangle((200, 200), 100, 100, linewidth=1, edgecolor='r', facecolor='none'))
    plt.gca().add_patch(Rectangle((400, 200), 100, 100, linewidth=1, edgecolor='g', facecolor='none'))

    plt.gca().add_patch(Rectangle((0, 400), 100, 100, linewidth=1, edgecolor='r', facecolor='none'))
    plt.gca().add_patch(Rectangle((200, 400), 100, 100, linewidth=1, edgecolor='y', facecolor='none'))
    plt.gca().add_patch(Rectangle((400, 400), 100, 100, linewidth=1, edgecolor='g', facecolor='none'))


    plt.scatter([p.x_pos for p in self.world.persons], 
                [p.y_pos for p in self.world.persons], 4, 
                [{(True, False): 'r', 
                  (False, False): 'g', 
                  (False, True): 'b'}[(p.infected, p.recovered)] for p in self.world.persons])
    plt.xlim([0, SC.WORLD_SIZE])
    plt.ylim([0, SC.WORLD_SIZE])
    plt.title('Day: ' + str(self.simulation_iteration//(24//SC.TIME_STEP)) + ' - Hour: ' + str(self.simulation_iteration%(24//SC.TIME_STEP)*SC.TIME_STEP))

    #MID plot
    plt.subplot2grid((4, 1), (2, 0), rowspan=1)
    plt.plot([p[0] for p in self.history], 'r')
    plt.plot([p[1] for p in self.history], 'g')
    plt.plot([p[2] for p in self.history], 'b')
    plt.plot([p[3] for p in self.history], 'k')
    plt.xticks([i for i in range(self.simulation_iteration+1)],
               ['Day: ' + str(i//(24//SC.TIME_STEP)) if (i%(24//SC.TIME_STEP)*SC.TIME_STEP) == 0 else '' for i in range(self.simulation_iteration+1)],
              rotation='vertical')

    #Bottom plot
    plt.subplot2grid((4, 1), (3, 0), rowspan=1)
    plt.plot([p[4] for p in self.history], 'r')
    plt.xticks([i for i in range(self.simulation_iteration+1)],
               ['Day: ' + str(i//(24//SC.TIME_STEP)) if (i%(24//SC.TIME_STEP)*SC.TIME_STEP) == 0 else '' for i in range(self.simulation_iteration+1)],
              rotation='vertical')
    plt.pause(0.0001)

  def update_history(self):
    infectedPersons = 0
    healthyPersons = 0
    recoveredPersons = 0
    deadPersons = 0

    for person in self.world.persons:
      if person.infected:
        infectedPersons += 1
      else:
        healthyPersons += 1

      if person.recovered:
        recoveredPersons += 1

      if person.dead:
          deadPersons += 1

    #self.history.append([infectedPersons, healthyPersons, recoveredPersons])
    self.history.append([infectedPersons, healthyPersons, recoveredPersons, deadPersons, self.world.daily_infected_counter])

  def logSimulationStats(self):
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

    day = int(self.simulation_iteration//(24//SC.TIME_STEP))
    self.csv_writer.write_row([healthyPersons, infectedPersons, recoveredPersons, day])
    
    print('Day: ', day, ' stats: ', healthyPersons, infectedPersons, recoveredPersons)

sim_manager = Simluation_Manager()
sim_manager.start()

print('Simulation finished')
