import pygame as pg

# game options/settings
TITLE = "Sudoku Solver"
TILESIZE = 64
WIDTH = TILESIZE*9 + 3
HEIGHT = TILESIZE*9 + 3
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# font
font_name = pg.font.get_default_font()
font_size = 64

# puzzle
s_string = "438209061/206008040/001036270/000052400/080900020/320040680/000701802/792600000/005000706"

# grid layout

# GRIDWIDTH = WIDTH / TILESIZE
# GRIDHEIGHT = HEIGHT / TILESIZE