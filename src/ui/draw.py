import pygame
class Draw:
    def __init__(self, width, height, row_count, block_size, block_list):
        self.font = pygame.font.SysFont("Arial", 24)
        self.block_list = block_list
        self.block_size = block_size
        self.row_count = row_count
        self.width, self.height = width, height
        self.game_screen = pygame.display.set_mode((self.width, self.height))

    # piirretään käyttöliittymä
    def draw(self, grid, won, mine_count, won_time):
        self.game_screen.fill((0, 0, 0))
        self.draw_clock(won, grid, won_time)
        self.draw_mines_left(mine_count, grid)
        if won:
            self.draw_won(won_time)
        if grid.mine_hit:
            self.draw_lost(won_time)
        self.draw_blocks(grid)
        pygame.display.flip()

    def draw_won(self, won_time):
        message = "You won, your time: " + str(won_time)
        won_string = self.font.render(message, True, (0, 255, 0))
        self.game_screen.blit(won_string, (60, 0))

    def draw_lost(self, won_time):
        message = "Game over" 
        won_string = self.font.render(message, True, (0, 255, 0))
        self.game_screen.blit(won_string, (60, 0))

    # piirretään miinalaskuri. todo: lisää tausta

    def draw_mines_left(self, mine_count, grid):
        mines_left = str(mine_count - grid.flags)
        display_mines_left = self.font.render(mines_left, True, (255, 0, 0))
        self.game_screen.blit(display_mines_left, (self.width - 30, 33))

    # piirretään pelikello. todo: lisää tausta
    def draw_clock(self, won, grid, won_time):
        if not won and grid.mine_hit == False:
            play_time = str(pygame.time.get_ticks() // 1000)
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
