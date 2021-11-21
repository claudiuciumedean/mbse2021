import simpy
import random
import uuid
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from components.World import World
from components.Person import Person
from CSV_Writer import CSV_Writer
from Simulation_Constants import InfectionSeverity, PersonStatus, PersonBehaviour
from Simulation_Constants import Simulation_Constants as sc

if sc.FIXED_SEED:
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
    persons = [Person(self.world, status = PersonStatus.INFECTED)]
    persons[0].x, persons[0].y = sc.WORLD_SIZE/2, sc.WORLD_SIZE/2

    for i in range(1, sc.POP_SIZE):
      if random.random() < sc.EXPLORERS_PERCENTAGE:
        person = Person(self.world, behaviour = PersonBehaviour.EXPLORER)
      else:
        person = Person(self.world)
      persons.append(person)

    self.world.persons = persons

    #self.env = simpy.rt.RealtimeEnvironment(factor = .10) #factor of 1 simulation runs a process every second, 0.5 factor 2 processes every second and so on
    self.env = simpy.Environment()
    self.env.process(self.run())
    self.env.run(until=(24//sc.TIME_STEP)*sc.DAYS_SIMULATED)
    #self.logSimulationStats()

  def run(self):
      plt.rcParams["figure.figsize"] = (5, 6)

      while True:
        #self.update_history()
        #self.plot_world()

        if self.simulation_iteration % (24//sc.TIME_STEP) == 0:
            #self.world.counter = {PersonStatus.HEALTHY: 0,
                                  #PersonStatus.INFECTED: 0,
                                  #PersonStatus.DEAD: 0,
                                  #PersonStatus.RECOVERED: 0}
            self.logSimulationStats() 

        self.world.live(self.simulation_iteration)
        self.simulation_iteration += 1

        yield self.env.timeout(1)  # timeout for a second

  def plot_world(self):
    """Plot the positions of the persons in the world, and their current status as color.
    """
    color_map = {PersonStatus.HEALTHY: 'g',
                 PersonStatus.INFECTED: 'r',
                 PersonStatus.RECOVERED: 'b',
                 PersonStatus.DEAD: 'k'}
    color_map_wearable = {InfectionSeverity.GREEN: 'g',
                          InfectionSeverity.ORANGE: 'y',
                          InfectionSeverity.RED: 'r',
                          0: 'k'}


    plt.clf()
    plt.subplot2grid((3, 1), (0, 0), rowspan=2)

    plt.gca().add_patch(Rectangle((0, 0), 100, 100, linewidth=1, edgecolor='r', facecolor='none'))
    plt.gca().add_patch(Rectangle((200, 0), 100, 100, linewidth=1, edgecolor='g', facecolor='none'))
    plt.gca().add_patch(Rectangle((400, 0), 100, 100, linewidth=1, edgecolor='y', facecolor='none'))

    plt.gca().add_patch(Rectangle((0, 200), 100, 100, linewidth=1, edgecolor='y', facecolor='none'))
    plt.gca().add_patch(Rectangle((200, 200), 100, 100, linewidth=1, edgecolor='r', facecolor='none'))
    plt.gca().add_patch(Rectangle((400, 200), 100, 100, linewidth=1, edgecolor='g', facecolor='none'))

    plt.gca().add_patch(Rectangle((0, 400), 100, 100, linewidth=1, edgecolor='r', facecolor='none'))
    plt.gca().add_patch(Rectangle((200, 400), 100, 100, linewidth=1, edgecolor='y', facecolor='none'))
    plt.gca().add_patch(Rectangle((400, 400), 100, 100, linewidth=1, edgecolor='g', facecolor='none'))


    plt.scatter([p.x for p in self.world.persons], 
                [p.y for p in self.world.persons], 30, 
                [color_map[p.status] for p in self.world.persons])
    plt.scatter([p.x for p in self.world.persons], 
                [p.y for p in self.world.persons], 10, 
                [color_map_wearable[p.wearable.user_risk_level] for p in self.world.persons])
    plt.xlim([0, sc.WORLD_SIZE])
    plt.ylim([0, sc.WORLD_SIZE])
    plt.title('Day: ' + str(self.simulation_iteration//(24//sc.TIME_STEP)) + ' - Hour: ' + str(self.simulation_iteration%(24//sc.TIME_STEP)*sc.TIME_STEP))

    #MID plot
    plt.subplot2grid((3, 1), (2, 0), rowspan=1)
    plt.plot([p[0] for p in self.history], 'g')
    plt.plot([p[1] for p in self.history], 'r')
    plt.plot([p[2] for p in self.history], 'b')
    plt.plot([p[3] for p in self.history], 'k')
    plt.xticks([i for i in range(self.simulation_iteration+1)],
               ['Day: ' + str(i//(24//sc.TIME_STEP)) if (i%(24//sc.TIME_STEP)*sc.TIME_STEP) == 0 else '' for i in range(self.simulation_iteration+1)],
              rotation='vertical')

    #Bottom plot
    #plt.subplot2grid((4, 1), (3, 0), rowspan=1)
    #plt.plot([p[1] for p in self.history], 'g')
    #plt.xticks([i for i in range(self.simulation_iteration+1)],
    #           ['Day: ' + str(i//(24//sc.TIME_STEP)) if (i%(24//sc.TIME_STEP)*sc.TIME_STEP) == 0 else '' for i in range(self.simulation_iteration+1)],
    #          rotation='vertical')
    plt.pause(0.0001)

  def update_history(self):
    self.history.append([self.world.counter[PersonStatus.HEALTHY],
                         self.world.counter[PersonStatus.INFECTED],
                         self.world.counter[PersonStatus.RECOVERED],
                         self.world.counter[PersonStatus.DEAD]])

  def logSimulationStats(self):
    day = int(self.simulation_iteration//(24//sc.TIME_STEP))
    self.csv_writer.write_row([self.world.counter[PersonStatus.HEALTHY], 
                               self.world.counter[PersonStatus.INFECTED],
                               self.world.counter[PersonStatus.RECOVERED],
                               self.world.counter[PersonStatus.DEAD],
                               day])
    
    print('Day: ', day, ' stats: ', self.world.counter)

sim_manager = Simluation_Manager()
sim_manager.start()

print('Simulation finished')
