
# Täällä luodaan peliruudukko ja alustetaan se miinoilla
# sekä hoidetaan ruudukon päivitys
import random


class GameGrid:  # alustetaan peliruudukko
    def __init__(self, size, mines):
        self.size = size
        self.mine_count = mines
        self.set_mines()
        self.set_mine_neighbours()
        self.flags = 0
        self.klicked = 0
        self.mine_hit = False

    def set_mines(self):    # luodaan ruudukko ja arvotaan sille miinat
        self.grid = [[0]*self.size for _ in range(self.size)]
        i = 0
        while i < self.mine_count:
            korkeus = random.randint(0, self.size-1)
            leveys = random.randint(0, self.size-1)
            if self.grid[korkeus][leveys] == 0:
                self.grid[korkeus][leveys] = 10
                i += 1

    # lähetetään miinojen koordinaatit naapureiden laskentaan
    def set_mine_neighbours(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 10:
                    self.set_numbers(i, j)

    # hiirellä klikattu, avataan luukku ja katsotaan mitä sisällä
    # todo: miinaan osuminen, avatun ruudun tyhjien naapureiden avaaminen
    def handle_left_mouse(self, position, size):
        position_j = position[0] // size
        position_i = (position[1] - 90) // size
        if position_i < 0:
            return
        if self.grid[position_i][position_j] < 9:
            self.grid[position_i][position_j] += 20
            self.klicked += 1
        if self.grid[position_i][position_j] == 10:
            self.grid[position_i][position_j] += 20
            self.mine_hit = True

    # oikealla hiiren klikkauksella lippu päälle/ lippu pois
    def handle_right_mouse(self, position, size):
        position_j = position[0] // size
        position_i = (position[1] - 90) // size
        if self.grid[position_i][position_j] < 11:
            self.grid[position_i][position_j] += 50
            self.flags += 1
        elif self.grid[position_i][position_j] >= 50:
            self.grid[position_i][position_j] -= 50
            self.flags -= 1

    # lasketaan miinan vieressä oleville ruuduille numeroarvot
    # todo: selkiytetään koodia
    def set_numbers(self, i, j):
        if i > 0:
            if j > 0:
                if self.grid[i-1][j-1] != 10:
                    self.grid[i-1][j-1] += 1
            if j < self.size - 1:
                if self.grid[i-1][j+1] != 10:
                    self.grid[i-1][j+1] += 1

            if self.grid[i-1][j] != 10:
                self.grid[i-1][j] += 1

        if i < self.size - 1:
            if j > 0:
                if self.grid[i+1][j-1] != 10:
                    self.grid[i+1][j-1] += 1
            if j < self.size - 1:
                if self.grid[i+1][j+1] != 10:
                    self.grid[i+1][j+1] += 1

            if self.grid[i+1][j] != 10:
                self.grid[i+1][j] += 1

        if j > 0:
            if self.grid[i][j-1] != 10:
                self.grid[i][j-1] += 1
        if j < self.size - 1:
            if self.grid[i][j+1] != 10:
                self.grid[i][j+1] += 1
