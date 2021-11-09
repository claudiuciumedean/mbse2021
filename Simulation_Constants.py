class Simulation_Constants():
    WORLD_SIZE = 500
    AREA_SIZE = 200
    INITIAL_TEMPERATURE = 37.0
    INITIAL_OXYGEN = 99
    WEARABLE_DANGER_RADIUS = 5
    WEARABLE_WARNING_RADIUS = 10
    FLEE_DIST = 15
    SIGMA = 10
    POP_SIZE = 500
    DISEASE_DURATION = 14*8
    FIXED_SEED = True

    TIME_STEP = 3 #Hours
    DAYS_SIMULATED = 60


class InfectionSeverity():
    RED = 3  # high
    ORANGE = 2  # medium
    GREEN = 1  # low


class Disease_features():
    TEMP_RANGES = [(0, 37.3), (37.3, 38.2), (38.2, 39), (39, 50)]
    OXYGEN_THRESHOLD = 95
    INFECTION_RADIUS = Simulation_Constants.WEARABLE_DANGER_RADIUS
