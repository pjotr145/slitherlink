#!/usr/bin/env python
''' Class definition of a single room with a given value.
'''

import numpy

class Room():
    ''' Defenition of a single room.
    '''
    def __init__(self, value, walls):
        self.value = value
        self.walls = walls
#        print("single room : {}".format(self.value))
#        print("room indexes: {}".format(self.walls))

    def room_score(self, list_of_walls):
        ''' Calculate the score for this room.
            room_score = 0 if nmr. walls = self.value
        '''
        score = 0
        for i in self.walls:
            score += list_of_walls[i]
        return abs(self.value - score)
