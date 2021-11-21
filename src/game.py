import pygame

class Game:                 
    def __init__(self):
        pygame.init()               #alustetaan pygame
        self.block_size = 30       #peliobjektin koko pikseleinä
        self.row_count = 9          #peliobjektien määrä rivillä
        self.mine_count = 6
        self.width, self.height =  self.block_size * self.row_count, self.block_size * self.row_count + 90 #varataan pieni tili tulevalle yläpalkille
        self.game_screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Miinaharava")
        grid = GameGrid(self.row_count)     #testataan gridin luontia

        

    def game_loop(self):
        self.game_screen.fill((0,0,0))
        pygame.display.flip()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()


class GameGrid:
    def __init__(self, size):
        self.size = size
        self.set_grid()

    def set_grid(self):
        self.grid = [[0]*self.size for _ in range(self.size)]
        print(self.grid)

mine = Game()

mine.game_loop()