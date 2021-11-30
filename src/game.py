import pygame
from gamegrid import GameGrid


class Game:
    def __init__(self, game_area_size: int):
        # alustetaan pygame
        pygame.init()
        # peliobjektin koko pikseleinä
        self.block_size = 30
        # peliobjektien määrä rivillä
        self.row_count = game_area_size
        self.mine_count = 6
        # varataan pieni tili tulevalle yläpalkille
        self.width, self.height = self.block_size * self.row_count, \
            self.block_size * self.row_count + 90
        self.game_screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Miinaharava")
        self.grid = GameGrid(self.row_count, self.mine_count)
        # tehdään lista kuville ja täytetään se
        self.block_list = []
        self.set_block_list()

    def set_block_list(self):
        for i in range(12):
            file_name = "src/assets/" + str(i) + ".png"
            self.block_list.append(pygame.transform.scale(
                pygame.image.load(file_name), (self.block_size, self.block_size)))

    def loop(self):
        while True:
            self.check_events()
            self.draw()
            self.clock.tick(60)

    # tarkistetaan tapahtumat. ToDo hiiren oikea sekä vasen painallus.
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def draw(self):
        self.game_screen.fill((0, 0, 0))
        for i in range(self.row_count):
            for j in range(self.row_count):
                self.game_screen.blit(
                    self.block_list[self.grid.grid[i][j]], (i*self.block_size, j*self.block_size + 90))
        pygame.display.flip()
