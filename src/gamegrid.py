
# Täällä luodaan peliruudukko ja alustetaan se miinoilla
#
import random


class GameGrid:  # alustetaan peliruudukko
    def __init__(self, size, mines):
        self.size = size
        self.mine_count = mines
        self.set_mines()
        self.set_mine_neighbours()
        print(self.grid)

    def set_mines(self):    # luodaan ruudukko ja arvotaan sille miinat
        self.grid = [[0]*self.size for _ in range(self.size)]
        i = 0
        while i < self.mine_count:
            korkeus = random.randint(0, self.size-1)
            leveys = random.randint(0, self.size-1)
            if self.grid[korkeus][leveys] == 0:
                self.grid[korkeus][leveys] = 10
                i += 1

    # Todo montako miinaa on ruutujen ympärillä
    def set_mine_neighbours(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 10:
                    self.set_numbers(i, j)

    def set_numbers(self, i, j):  # todo saako selkeämmäksi jotenkin?
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
