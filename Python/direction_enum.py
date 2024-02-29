# enum for direction

from enum import Enum

class Direction(Enum):
    North = 1
    East = 2
    South = 3
    West = 4


Direction = Enum('Direction', ['North', 'East', 'South', 'West'])