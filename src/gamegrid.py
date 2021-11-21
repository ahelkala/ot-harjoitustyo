
# Täällä luodaan peliruudukko ja alustetaan se miinoilla
#
import random

class GameGrid:
    def __init__(self, size, mines):
        self.size = size
        self.mine_count = mines
        self.set_grid()

    def set_grid(self):
        self.grid = [[0]*self.size for _ in range(self.size)]
        i = 0
        while i < self.mine_count:
            korkeus = random.randint(0, self.size-1)
            leveys = random.randint(0, self.size-1)
            if self.grid[korkeus][leveys] == 0:
                self.grid[korkeus][leveys] = 10
                i += 1
        print(self.grid)

