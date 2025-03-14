# room.py
from Room.room import Room


class Tiled_Stove(Room):
    def __int__(self, tiles, size):
        self.tiles = tiles
        self.size = size 
        