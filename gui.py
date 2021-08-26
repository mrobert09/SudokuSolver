from guisettings import *
from solver import *

class Game:
    """
    Gui class called "Game" using the PyGame library. Within it it calls the Sudoku solver.
    """

    def __init__(self):
        """
        Initialization of PyGame class.
        """
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(font_name, font_size)
        self.solver = SudokuSolver(s_string)
        self.frame_count = 0
        self.running = True

    def new(self):
        """
        Code within normally used to reset game, though not used in this program.
        :return:
        """
        self.run()

    def run(self):
        """
        Main game loop.
        :return:
        """
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        """
        Game Loop - Events. Checks for any interaction by user. Only interaction is closing the window.
        :return:
        """
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        """
        Game Loop - Update. Updates the data on each frame.
        :return:
        """
        self.frame_count += 1
        if self.frame_count >= 10:
            self.solver.slow_solve()

    def draw_grid(self):
        """
        Draws the Sudoku grid to the screen.
        :return:
        """
        for iteration, x in enumerate(range(0, WIDTH, TILESIZE)):
            if iteration % 3 == 0:
                pg.draw.line(self.screen, BLACK, (x, 0), (x, HEIGHT), 4)
            else:
                pg.draw.line(self.screen, BLACK, (x, 0), (x, HEIGHT))
        for iteration, y in enumerate(range(0, HEIGHT, TILESIZE)):
            if iteration %  3 == 0:
                pg.draw.line(self.screen, BLACK, (0, y), (WIDTH, y), 4)
            else:
                pg.draw.line(self.screen, BLACK, (0, y), (WIDTH, y))

    def write_numbers(self):
        """
        Draws all the numbers onto the screen before the flip. Uses the Sudoku solver's last known list to write numbers.
        :return:
        """
        for y_iter, row in enumerate(self.solver.get_list()):
            for x_iter, num in enumerate(row):
                if num != 0:
                    text = self.font.render(str(num), True, BLACK)
                    text_rect = text.get_rect()
                    text_rect.center = (32 + x_iter * TILESIZE, 35 + y_iter * TILESIZE)
                    self.screen.blit(text, text_rect)
                else:
                    pass

    def draw(self):
        """
        Game Loop - Draw
        :return:
        """
        self.screen.fill(WHITE)
        self.draw_grid()
        self.write_numbers()

        # always do last after drawing everything
        pg.display.flip()

def main():
    g = Game()
    while g.running:
        g.new()

if __name__ == '__main__':
    main()
