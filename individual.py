#!/usr/bin/env python

import numpy as np
from room import Room

class Individual():
    ''' Class definition of a single individual.
    '''
    def __init__(self,
                 gene_length,
                 all_walls,
                 all_rooms,
                 wall_index_per_room,
                 room_value_index):
        self.gene_length = gene_length
        self.walls = all_walls
        self.rooms = all_rooms
        self.wall_indexes = wall_index_per_room
        self.room_value_index = room_value_index
        self.fitness = 0

        self.gene = np.random.randint(2, size=self.gene_length)
        # TODO: Make sure the walls given bij the puzzle are set to 1.
        for i in all_walls:
            self.gene[i] = 1
#        print("Ind gene: {}".format(self.gene))

        self.my_rooms = []
#        print("ind: rooms: {}".format(self.rooms))
#        print("ind: index: {}".format(self.room_value_index))
        for i in self.room_value_index:
            new_room = Room(self.rooms[i], self.wall_indexes[i])
            self.my_rooms.append(new_room)
#        print("ind: rooms: {}".format(self.my_rooms))

    def calc_fitness(self):
        self.fitness = 0
        for room in self.my_rooms:
            self.fitness += room.room_score(self.gene)
