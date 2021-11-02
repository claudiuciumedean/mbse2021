from enum import Enum


class Simulation_Constants():
    WORLD_SIZE = 500
    AREA_SIZE = 200
    INITIAL_TEMPERATURE = 37.0
    INITIAL_OXYGEN = 99
    WEARABLE_COMMUNICATION_RADIUS = 20
    FLEE_DIST = 15
    DISEASE_DURATION = 14


class InfectionSeverity(Enum):
    RED = 3  # high
    ORANGE = 2  # medium
    GREEN = 1  # low


class Disease_features(Enum):
    TEMPERATURE_WARN = 37.3
    OXYGEN_UNSAFE = 93
    OXYGEN_SAFE = 95
