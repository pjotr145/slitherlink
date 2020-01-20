#!/usr/bin/env python
''' Creating a population.
'''

from individual import Individual
import numpy

class Population():
    ''' Defining a population. Functions to create new generations
        should go here.
    '''
    def __init__(self,
                 gene_length,
                 all_walls,
                 all_rooms,
                 wall_index_per_room,
                 room_value_index,
                 settings):
        self.gene_length = gene_length
        self.all_walls = all_walls
        self.all_rooms = all_rooms
        self.wall_index_per_room = wall_index_per_room
        self.room_value_index = room_value_index
        self.settings = settings
        print("New population")

        self.pop = []
        for i in range(self.settings['population_size']):
            one_individual = Individual(self.gene_length,
                                        self.all_walls,
                                        self.all_rooms,
                                        self.wall_index_per_room,
                                        self.room_value_index)
            self.pop.append(one_individual)
#            print("pop: indiv-nmr: {}".format(i))


    def calc_fitnesses(self):
        for ind, gene in enumerate(self.pop):
            gene.calc_fitness()
#            print("ind: {:>3} has fitness: {}".format(ind, gene.fitness))

    def sort_pop_on_fitness(self):
        self.pop.sort(key=lambda x: x.fitness, reverse=True)
        for ind, gene in enumerate(self.pop):
            print("ind: {:>3} has fitness: {}".format(ind, gene.fitness))
