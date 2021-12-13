
# Täällä luodaan peliruudukko ja alustetaan se miinoilla
# sekä hoidetaan ruudukon päivitys
import random


class GameGrid:  
    """Luokka miinakentän luomiseen ja sen ylläpitoon syötteiden avulla.

    Attributes:
        size: Miinakentän koko.
        mine_count: Miinojen määrä.
        flags: Käyttäjän kentälle asettamien lippujen määrä.
        klicked: Käyttäjän avaamien ruutujen määrä.
        mine_hit: Onko osuttu miinaan. 
    """
    def __init__(self, size, mines):
        self.size = size
        self.mine_count = mines
        self.set_mines()
        self.set_mine_neighbours()
        self.flags = 0
        self.klicked = 0
        self.mine_hit = False

    def set_mines(self):
        """Luodaan peliruudukko ja arvotaan siihen annettu määrä miinoja.
        """
        self.grid = [[0]*self.size for _ in range(self.size)]
        i = 0
        while i < self.mine_count:
            korkeus = random.randint(0, self.size-1)
            leveys = random.randint(0, self.size-1)
            if self.grid[korkeus][leveys] == 0:
                self.grid[korkeus][leveys] = 10
                i += 1

    def set_mine_neighbours(self):
        """Lähetetään miinojen koordinaatit naapureiden laskentaan.
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 10:
                    self.set_numbers(i, j)
    
    def list_neighbours(self, i, j):
        """Lasketaan annettua koordinaattia ympäröivien ruutujen koordinaatit.

        Args:
            i: Miinakentän y-koordinaatti.
            j: Miinakentän x-koordinaatti.

        Returns:
            Lista, jonne kirjattu annetun ruudun ympärillä olevien ruutujen koordinaatit.
        """
        list = []
        for k in range(i-1, i+2):
            for l in range(j-1,j+2):
                if 0 <= k <= self.size -1 and 0 <= l <= self.size -1:
                    list.append((k,l))
        return list

    def solve_zeros(self, i, j):
        """Avataan klikatun nollan ympärillä olevat ruudut.

        Käy rekursiivisesti ympäröivät nollat läpi sekä sen jälkeen lähettää nollan ympärillä olevat
        ruudut seuraavan metodin selvitettäväksi.

        Args:
            i: Miinakentän y-koordinaatti.
            j: Miinakentän x-koordinaatti.
        """
        list = self.list_neighbours(i,j)
        for coordinates in list:
            if self.grid[coordinates[0]][coordinates[1]] == 0:
                self.grid[coordinates[0]][coordinates[1]] += 20
                self.klicked += 1                
                self.solve_zeros(coordinates[0],coordinates[1])
                self.solve_numbers(coordinates[0],coordinates[1])  
    
    def solve_numbers(self, i, j):
        """Selvittää nollan ympärillä olevien ruutujen numeroarvot.

        Args:
            i: Miinakentän y-koordinaatti.
            j: Miinakentän x-koordinaatti.
        """
        list = self.list_neighbours(i,j)
        for coordinates in list:
            if 0 < self.grid[coordinates[0]][coordinates[1]] < 10:
                self.grid[coordinates[0]][coordinates[1]] += 20
                self.klicked += 1                
                 
    # hiirellä klikattu, avataan luukku ja katsotaan mitä sisällä
    # todo: miinaan osuminen, avatun ruudun tyhjien naapureiden avaaminen
    def handle_left_mouse(self, position, size):
        """Käsittelee hiiren vasemman painikkeen klikkauksen.

        Suoritettava toiminto riippuu avatun ruudun numeerisesta arvosta.

        Args:
            position: Hiiren koordinaatit klikkaushetkellä.
            size: Yksittäisen peliruuden särmän pituus.
        """
        position_j = position[0] // size
        position_i = (position[1] - 90) // size
        if position_i < 0:
            return
        if self.grid[position_i][position_j] == 0:
            self.solve_zeros(position_i, position_j)
        if 0 < self.grid[position_i][position_j] < 9:
            self.grid[position_i][position_j] += 20
            self.klicked += 1
        if self.grid[position_i][position_j] == 10:
            self.grid[position_i][position_j] += 20
            self.mine_hit = True

    def handle_right_mouse(self, position, size):
        """Käsittelee hiiren oikean painikkeen klikkauksen.

        Peliruutuun asetetaan lippu miinan merkiksi, tai olemassa oleva lippu poistetaan.

        Args:
            position: Hiiren koordinaatit klikkaushetkellä.
            size: Yksittäisen peliruuden särmän pituus.
        """
        position_j = position[0] // size
        position_i = (position[1] - 90) // size
        if self.grid[position_i][position_j] < 11:
            self.grid[position_i][position_j] += 50
            self.flags += 1
        elif self.grid[position_i][position_j] >= 50:
            self.grid[position_i][position_j] -= 50
            self.flags -= 1

    def set_numbers(self, i, j):
        """ Asetetaan miinan ympärille olevilla ruuduille numeeriset arvot.

        Args:
            i: Miinakentän y-koordinaatti.
            j: Miinakentän x-koordinaatti.
        """
        list = self.list_neighbours(i,j)
        for neighbour in list:
            if self.grid[neighbour[0]][neighbour[1]] != 10:
                self.grid[neighbour[0]][neighbour[1]] += 1       

