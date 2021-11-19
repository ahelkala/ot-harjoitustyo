import pygame

class Game:                 #first iteration of game-class. in future atleast game logic and ui will be divided to different classes
    def __init__(self):
        pygame.init()       #initialize pygame
        self.width, self.height = 640, 480  #for testing purposes, later these will be calculated with play area grid size
        self.game_screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Miinaharava")

    def game_loop(self):
        self.game_screen.fill((0,0,0))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

seppo = Game()

seppo.game_loop()