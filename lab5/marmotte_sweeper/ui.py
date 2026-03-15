import os
import pygame
from lab5.marmotte_sweeper.logic import Cell, MarmotteSweeper, RealRand


class MarmotteSweeperUI:
    """
    Code responsible for instantiating MarmotteSweeper and handling
    the user interface.
    """

    def __init__(self, width: int, height: int, count_marmottes: int, cell_size: int):
        """
        width and height are the size of the game (in cells)
        count_marmottes is how many marmottes the game should have
        cell_size is the size of each cell in screen pixels
        """
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.marmotte_sweeper = MarmotteSweeper(
            width, height, count_marmottes, RealRand()
        )

        # Load images from assets/ directory
        # type1 | type2 is used to describe the union of two types. You can also
        # use the Any type to express that a type is mixed.
        self.images: dict[Cell | int, pygame.Surface] = {}
        for i in range(9):
            self.images[i] = pygame.image.load(os.path.join("assets", str(i) + ".png"))
        self.images[Cell.MARMOTTE] = pygame.image.load(
            os.path.join("assets", "marmotte.png")
        )
        self.images[Cell.FLAGGED] = pygame.image.load(
            os.path.join("assets", "flag.png")
        )
        self.images[Cell.UNREVEALED] = pygame.image.load(
            os.path.join("assets", "blank.png")
        )

        # Resize images if needed
        for k, v in self.images.items():
            self.images[k] = pygame.transform.smoothscale(
                v, (self.cell_size, self.cell_size)
            )

        # Setup pygame and create a window
        pygame.init()
        self.window = pygame.Window(
            "Marmotte Sweeper", (width * cell_size, height * cell_size)
        )

    def draw(self) -> None:
        """
        Draws every cell of the grid.
        """
        surface = self.window.get_surface()
        for x in range(self.width):
            for y in range(self.height):
                cell = self.marmotte_sweeper.cell((x, y))
                image = self.images[cell]
                # convert grid positions to pixels
                surface.blit(image, (x * self.cell_size, y * self.cell_size))
        self.window.flip()

    def start(self) -> None:
        """
        Starts the pygame event loop. Returns when the window is closed.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    # convert pixels to grid positions
                    x = x // self.cell_size
                    y = y // self.cell_size
                    self.marmotte_sweeper.flag((x, y))

            self.draw()
            pygame.Clock().tick(60)
