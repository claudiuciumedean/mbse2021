class Simulation_Constants():
    TIME_STEP = 3 #Hours #Fixed
    FIXED_SEED = True #Fixed
    DAYS_SIMULATED = 150 #Fixed

    WORLD_SIZE = 500 #Fixed
    AREA_SIZE = 100 #Fixed

    POP_SIZE = 500 #Population size
    EXPLORERS_PERCENTAGE = 0.25 #returners will be 1-EXPLORERS_PERCENTAGE
    REBEL_PERCENTAGE = 0.0 #probability that a person ignore the wearable warnings

    WALK_STEP_RETURNERS = 10 #maximum movement possible at each iteration (in meters?)
    WALK_STEP_EXPLORERS = 50 #maximum movement possible at each iteration (in meters?)
    INITIAL_TEMPERATURE = 37.0 #Fixed
    INITIAL_OXYGEN = 99 #Fixed
    DISEASE_DURATION = 14*(24//TIME_STEP) #Fixed

    WEARABLE_DANGER_RADIUS = 5 #max radius at which the wearable think that a person can get infected (in meters?)
    WEARABLE_WARNING_RADIUS = 15 #max radius for communicating the warnings (in meters?)
    DEVICE_ACTIVE = True


class InfectionSeverity():
    RED = 3  # high
    ORANGE = 2  # medium
    GREEN = 1  # low


class Disease_features():
    TEMP_RANGES = [(0, 37.3), (37.3, 38.2), (38.2, 39), (39, 50)]
    OXYGEN_THRESHOLD = 95
    INFECTION_RADIUS = 5

class PersonStatus:
    HEALTHY = 0
    INFECTED = 1
    RECOVERED = 2
    DEAD = 3

class PersonBehaviour:
    RETURNER = 0
    EXPLORER = 1
    FLEE = 2
    FREEZE = 3
