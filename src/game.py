import pygame

class Game:                 
    def __init__(self,game_area_size: int):
        pygame.init()               #alustetaan pygame
        self.block_size = 30       #peliobjektin koko pikseleinä
        self.row_count = game_area_size          #peliobjektien määrä rivillä
        self.mine_count = 6
        self.width, self.height =  self.block_size * self.row_count, self.block_size * self.row_count + 90 #varataan pieni tili tulevalle yläpalkille
        self.game_screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Miinaharava")
        grid = GameGrid(self.row_count)     #testataan gridin luontia
        self.not_visited_block = pygame.transform.scale(pygame.image.load("assets/unexplored.png"), (self.block_size,self.block_size))

        

    def loop(self):        
        while True:
            self.check_events()
            self.draw()
            self.clock.tick(60)
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def draw(self):
        self.game_screen.fill((0,0,0))
        pygame.display.flip()
        self.game_screen.blit(self.not_visited_block, (50, 50))
        pygame.display.flip()



class GameGrid:
    def __init__(self, size):
        self.size = size
        self.set_grid()

    def set_grid(self):
        self.grid = [[0]*self.size for _ in range(self.size)]
        print(self.grid)
