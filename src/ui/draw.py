import pygame
from database import DataBaseConnection

class Draw:
    def __init__(self, width, height, row_count, block_size, block_list):
        """Alustetaan Draw-luokka. 

        Args:
            width : pelikentän leveys.
            height: pelikentän korkeus.
            row_count: peliruutujen määrä kentän särmässä.
            block_size: peliruudun koko pikseleinä.
            block_list: lista poliobjekteista.
            start_time: pelin aloitusaika
        """
        self.font = pygame.font.SysFont("Arial", 24)
        self.block_list = block_list
        self.block_size = block_size
        self.row_count = row_count
        self.width, self.height = width, height
        self.game_screen = pygame.display.set_mode((self.width, self.height))
        self.score_base = DataBaseConnection()
        self.start_time = 0

    def draw(self, grid, won, mine_count, won_time):
        """Piirretään käyttöliittymän eri komponentit.

        Args:
            grid: peliruudukko.
            won: tieto onko pelaaja voittanut.
            mine_count: pelissä olevien miinojen määrä.
            won_time: voittoaika
        """
        self.game_screen.fill((0, 0, 0))
        self.draw_clock(won, grid, won_time)
        self.draw_mines_left(mine_count, grid)
        self.draw_blocks(grid)
        if won:
            self.draw_won(won_time)
            self.draw_score()
        if grid.mine_hit:
            self.draw_lost()
            self.draw_score()
        pygame.display.flip()

    def draw_score(self):
        """Piirretään pelikentälle viisi parasta tulosta.
        """
        if self.score_base.fail == True:
            return
        score_list = self.score_base.get_score()
        self.draw_score_backround()
        for i in range(5):
            score_text = str(score_list[i][0]) + ":  " + str(score_list[i][1])
            score_line = self.font.render(score_text, True, (255, 0, 0))
            self.game_screen.blit(score_line, (30, 140 + i*40))
    
    def draw_score_backround(self):
        """Piirretään tuloksia varten läpinäkyvä tausta ja otsikkorivi.
        """
        surface = pygame.Surface((200,240))
        surface.set_alpha(190)
        surface.fill((80,80,80))
        self.game_screen.blit(surface, (0,90))
        topic = self.font.render("Top Scores: ", True, (255, 0, 0))
        self.game_screen.blit(topic, (30, 100))


    def draw_won(self, won_time):
        """Piirretään voittoteksti voiton jälkeen.

        Args:
            won_time: voittoaika.
        """
        message = "You won, your time: " + str(won_time)
        won_string = self.font.render(message, True, (0, 255, 0))
        self.game_screen.blit(won_string, (60, 0))

    def draw_lost(self):
        """Piirretään "Game over" -teksti hävityn pelin jälkeen
        """
        message = "Game over"
        won_string = self.font.render(message, True, (0, 255, 0))
        self.game_screen.blit(won_string, (60, 0))

    def draw_mines_left(self, mine_count, grid):
        """Piirretään jäljellä olevien miinojen lukumäärä.

        Args:
            mine_count: jäljellä olevat miinat.
            grid: peliruudukko.
        """
        mines_left = str(mine_count - grid.flags)
        display_mines_left = self.font.render(mines_left, True, (255, 0, 0))
        self.game_screen.blit(display_mines_left, (self.width - 30, 33))

    def draw_clock(self, won, grid, won_time):
        """Piirretään pelikello.

        Args:
            won: tieto voitetusta pelistä
            grid: peliruudukko.
            won_time: voittoaika.
        """
        if not won and grid.mine_hit == False:
            play_time = str((pygame.time.get_ticks() - self.start_time)// 1000)
        else:
            play_time = won_time
        display_clock = self.font.render(play_time, True, (255, 0, 0))
        self.game_screen.blit(display_clock, (0, 33))

    def draw_blocks(self, grid):
        """Piirretään miinakenttä.

        Valitaan peliruudukon numeerista arvoa vastaava kuva ja piirretään se kyseiseen ruutuun.

        Args:
            grid: peliruudukko.
        """
        for i in range(self.row_count):
            for j in range(self.row_count):
                if 50 > grid.grid[i][j] > 10:
                    self.game_screen.blit(
                        self.block_list[grid.grid[i][j]-20], (j*self.block_size, i*self.block_size + 90))
                elif grid.grid[i][j] >= 50:
                    self.game_screen.blit(
                        self.block_list[9], (j*self.block_size, i*self.block_size + 90))
                else:
                    self.game_screen.blit(
                        self.block_list[11], (j*self.block_size, i*self.block_size + 90))
