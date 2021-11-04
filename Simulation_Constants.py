from enum import Enum


class Simulation_Constants():
    WORLD_SIZE = 500
    AREA_SIZE = 200
    INITIAL_TEMPERATURE = 37.0
    INITIAL_OXYGEN = 99
    WEARABLE_DANGER_RADIUS = 10
    WEARABLE_WARNING_RADIUS = 15
    FLEE_DIST = 15
    DISEASE_DURATION = 14*24
    FIXED_SEED = True


class InfectionSeverity():
    RED = 3  # high
    ORANGE = 2  # medium
    GREEN = 1  # low


class Disease_features():
    TEMP_RANGES = [(0, 37.3), (37.3, 38.2), (38.2, 39), (39, 50)]
    OXYGEN_THRESHOLD = 95
    INFECTION_RADIUS = Simulation_Constants.WEARABLE_DANGER_RADIUS
