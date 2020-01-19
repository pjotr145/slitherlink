#!/usr/bin/env python
''' Creating a population.
'''

from individual import Individual
import numpy

class Population():
    ''' Defining a population. Functions to create new generations
        should go here.
    '''
    def __init__(self, all_walls, all_rooms, wall_index_per_room,
                 room_value_index, settings):
        self.all_walls = all_walls
        self.all_rooms = all_rooms
        self.wall_index_per_room = wall_index_per_room
        self.room_value_index = room_value_index
        self.settings = settings
        print("New population")

        self.pop = []
        for i in range(self.settings['population_size']):
            one_individual = Individual(all_walls,
                                        all_rooms,
                                        wall_index_per_room,
                                        room_value_index)
            self.pop.append(one_individual)
            print("pop: indiv-nmr: {}".format(i))
