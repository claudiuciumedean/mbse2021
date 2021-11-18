class Simulation_Constants():
    WORLD_SIZE = 500
    POP_SIZE = 500
    EXPLORERS_PERCENTAGE = 0.3 #returners will be 1-EXPLORERS_PERCENTAGE
    WEARABLE_DANGER_RADIUS = 5
    WEARABLE_WARNING_RADIUS = 15
    WALK_STEP_RETURNERS = 10
    WALK_STEP_EXPLORERS = 50

    REBEL_PERCENTAGE = 0.5

    AREA_SIZE = 100
    INITIAL_TEMPERATURE = 37.0
    INITIAL_OXYGEN = 99
    TIME_STEP = 3 #Hours
    DISEASE_DURATION = 14*(24//TIME_STEP)
    FIXED_SEED = True
    DAYS_SIMULATED = 120
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
