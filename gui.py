from tkinter import *
from hulp import split_gene_into_puzzle
from itertools import islice


class Window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Kamertje Verhuur")
#        self['bg'] = 'red'
        #self.minsize("600x400")
        self.schermhoogte = 600
        self.bad_indices = []
        self.lijst_kamer_waardes = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.lijst_lijnen = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.canvas = Canvas(self)
        self.maakCanvas()


    def maakCanvas(self):
        pixels = self.schermhoogte / 12
        font = int(pixels / 5)
        len_list = int(len(self.lijst_lijnen) / 2) + 1
        width_list = len(self.lijst_lijnen[1])
#        x = 1
#        y = 1
        # print de stippen
        for y in range(1, len_list + 1):
            for x in range(1, width_list + 1):
                self.canvas.create_oval(x * pixels - 3,
                                        y * pixels - 3,
                                        x * pixels + 3,
                                        y * pixels + 3,
                                        outline="black",
                                        fill="black")
        x = 1
        y = 1
        # Print de waardes van de gegeven kamers.
        for r in range(len(self.lijst_kamer_waardes)):
            for n in range(len(self.lijst_kamer_waardes[r])):
                my_text = self.lijst_kamer_waardes[r][n]
                if r * 9 + n in self.bad_indices:
                    self.canvas.create_text(x * pixels + pixels / 2,
                                            y * pixels + pixels / 2,
                                            font=('Arial', font),
                                            fill="red",
                                            text=my_text)
                else:
                    self.canvas.create_text(x * pixels + pixels / 2,
                                            y * pixels + pixels / 2,
                                            font=('Arial', font),
                                            fill="black",
                                            text=my_text)
                x += 1
            x = 1
            y += 1
        x = 1
        y = 1
        for i in range(len(self.lijst_lijnen)):
            if i %2 != 0:
                # print vertical lines
                for j in range(len(self.lijst_lijnen[i])):
                    if self.lijst_lijnen[i][j] == 1:
                        self.canvas.create_line(x * pixels,
                                                pixels * y,
                                                x * pixels,
                                                pixels * y + pixels,
                                                width=2,
                                                fill="black")
                    x+=1
                y+=1
            else:
                # print horizontal lines
                for j in range(len(self.lijst_lijnen[i])):
                    if self.lijst_lijnen[i][j] == 1:
                        self.canvas.create_line(x * pixels,
                                                pixels * y,
                                                x * pixels + pixels,
                                                pixels * y,
                                                width=2,
                                                fill="black")
                    x += 1
            x=1
        self.canvas.pack(fill=BOTH, expand=1)


    def setWaardes(self, kamer_waardes, lijnen, bad_indices):
        self.lijst_kamer_waardes = kamer_waardes
        self.lijst_lijnen = lijnen
        self.bad_indices = bad_indices
        self.canvas.delete("all")
        self.maakCanvas()

    def set_schermhoogte(self, schermhoogte):
        self.schermhoogte = schermhoogte
        self.canvas.delete("all")
        self.maakCanvas()

