#!/usr/bin/env python

import numpy as np
import random
from room import Room

class Individual():
    ''' Class definition of a single individual.
    '''
    def __init__(self,
                 the_gene,
                 gene_length,
                 all_walls,
                 all_rooms,
                 wall_index_per_room,
                 room_value_index):
        self.gene = the_gene
        self.gene_length = gene_length
        self.walls = all_walls
        self.rooms = all_rooms
        self.wall_indexes = wall_index_per_room
        self.room_value_index = room_value_index
        self.fitness = 0

#        print("ind: rooms: {}".format(self.rooms))
#        print("ind: index: {}".format(self.room_value_index))
        # Create list of rooms for each room with a value
        self.my_rooms = []
        for i in self.room_value_index:
            new_room = Room(self.rooms[i], self.wall_indexes[i])
            self.my_rooms.append(new_room)
#        print("ind: rooms: {}".format(self.my_rooms))

    def calc_fitness(self):
        ''' Calculate the fitness of this Individual. For now
            only the walls around the rooms with values are checked.
            Later a better solution should be added.
        '''
        # TODO: add better solution for fitness calculation.
        self.fitness = 0
        for room in self.my_rooms:
            self.fitness += room.room_score(self.gene)

    def mutate_gene(self, mutation_rate):
        number_of_changes = np.random.randint(mutation_rate)
        genes_to_change = random.sample(range(len(self.gene)),
                                        number_of_changes)
        for i in genes_to_change:
            val = self.gene[i]
            if val == 0:
                self.gene[i] = 1
            else:
                self.gene[i] = 0

    def set_fixed_walls(self):
        for i in self.walls:
            self.gene[i] = 1

