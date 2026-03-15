import pygame


def main() -> None:
    pygame.init()
    window = pygame.Window()
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            print(event)
        window.get_surface().fill(pygame.Color("white"))
        pygame.draw.rect(
            window.get_surface(),
            pygame.Color("blue"),
            (10, 10, 50, 20))
        window.flip()
        clock.tick(60)


main()
