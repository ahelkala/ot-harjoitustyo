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
        self.font = pygame.font.SysFont("Arial", 24)
        self.won_time = "xxx"

    # ladataan pelin käyttämät kuvat listalle
    def set_block_list(self):
        for i in range(12):
            file_name = "src/assets/" + str(i) + ".png"
            self.block_list.append(pygame.transform.scale(
                pygame.image.load(file_name), (self.block_size, self.block_size)))

    def loop(self):
        self.won = False
        while True:
            self.check_events()
            self.draw()
            self.check_if_won()
            self.clock.tick(60)

    # voitettiinko?
    def check_if_won(self):
        if self.row_count ** 2 - self.grid.klicked == self.mine_count and self.grid.mine_hit == False and self.won == False:
            self.won = True
            self.won_time = str(pygame.time.get_ticks() // 1000)

    # tarkistetaan tapahtumat.
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse(event.button, event.pos)

    # lähetetään hiiren sijainti oikean tai vasemman painalluksen käsittelevälle funktiolle
    def handle_mouse(self, button, position):
        if button == 1:
            self.grid.handle_left_mouse(position, self.block_size)
        if button > 1:
            self.grid.handle_right_mouse(position, self.block_size)

    # piirretään käyttöliittymä
    # todo: tämä omaksi luokaksi?
    def draw(self):
        self.game_screen.fill((0, 0, 0))
        self.draw_clock()
        self.draw_mines_left()
        self.draw_blocks()
        pygame.display.flip()

    # piirretään miinakenttä
    def draw_blocks(self):
        for i in range(self.row_count):
            for j in range(self.row_count):
                if 50 > self.grid.grid[i][j] > 10:
                    self.game_screen.blit(
                        self.block_list[self.grid.grid[i][j]-20], (j*self.block_size, i*self.block_size + 90))
                elif self.grid.grid[i][j] >= 50:
                    self.game_screen.blit(
                        self.block_list[9], (j*self.block_size, i*self.block_size + 90))
                else:
                    self.game_screen.blit(
                        self.block_list[11], (j*self.block_size, i*self.block_size + 90))

    # piirretään pelikello. todo: lisää tausta
    def draw_clock(self):
        if not self.won and self.grid.mine_hit == False:
            play_time = str(pygame.time.get_ticks() // 1000)
        else:
            play_time = self.won_time
        display_clock = self.font.render(play_time, True, (255, 0, 0))
        self.game_screen.blit(display_clock, (0, 33))

    # piirretään miinalaskuri. todo: lisää tausta
    def draw_mines_left(self):
        mines_left = str(self.mine_count - self.grid.flags)
        display_mines_left = self.font.render(mines_left, True, (255, 0, 0))
        self.game_screen.blit(display_mines_left, (self.width - 30, 33))
