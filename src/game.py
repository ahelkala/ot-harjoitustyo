import pygame
from gamegrid import GameGrid
from ui.draw import Draw



class Game:
    def __init__(self, game_area_size: int):
        pygame.init()
        self.block_size = 30
        self.row_count = game_area_size
        self.mine_count = 60
        self.width, self.height = self.block_size * self.row_count, \
            self.block_size * self.row_count + 90
        self.game_screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Miinaharava")
        self.grid = GameGrid(self.row_count, self.mine_count)
        self.block_list = []
        self.set_block_list()
        self.font = pygame.font.SysFont("Arial", 24)
        self.won_time = "xxx"
        self.drawer = Draw(self.width, self.height,
                           self.row_count, self.block_size, self.block_list)

    def set_block_list(self):
        """Täällä ladataan pelin käyttämät kuvat listalle
        """
        for i in range(12):
            file_name = "src/assets/" + str(i) + ".png"
            self.block_list.append(pygame.transform.scale(
                pygame.image.load(file_name), (self.block_size, self.block_size)))


    def loop(self):
        """Looppi, joka on käynnissä ohjelman suorituksen loppuun asti

        Tämän kautta tarkitetaan tapahtumat, piirretään käyttöliittymä sekä pidetään kirjaa onko peli ohi
        """
        self.won = False
        self.start_time = pygame.time.get_ticks()
        while True:

            self.check_events()
            self.drawer.draw(self.grid, self.won,
                             self.mine_count, self.won_time)
            self.check_if_won()
            self.clock.tick(60)
    
    def restart(self):
        """käynnistetään peli uudelleen.
        """
        self.grid = GameGrid(self.row_count, self.mine_count)
        self.loop()

    def check_if_won(self):
        """Tarkistetaan onko peli ohi.

        Peli voi päättyä joko osumalla miinaan tai kun kaikki luukut miinoja lukuun ottamatta on avattu.
        """
        if self.row_count ** 2 - self.grid.klicked == self.mine_count and self.grid.mine_hit == False and self.won == False:
            self.won = True
            self.won_time = str(pygame.time.get_ticks() // 1000)

    def check_events(self):
        """Tarkistetaan näppäimistön ja hiiren tapahtumat.

        Jos suljetaan, ohjelman suoritus lopetataan. Välilyönnillä peli käynnistetään uudelleen ja hiiren 
        klikkaukset lähetetään edelleen tutkittavaksi.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not self.won and not self.grid.mine_hit:
                self.handle_mouse(event.button, event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.restart()

    def handle_mouse(self, button, position):
        """Lähetetään painetun hiiren napin mukaan hiiren koordinaatit niitä käsitteleville metodeille.

        Args:
            button (int): painetun hiiren napin tunniste.
            position (tuple): hiiren kursorin sijainti klikkaushetkellä.
        """
        if button == 1:
            self.grid.handle_left_mouse(position, self.block_size)
        if button > 1:
            self.grid.handle_right_mouse(position, self.block_size)
