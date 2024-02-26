import pygame


class Board(object):
    def __init__(
        self,
        screen_width: int,
        screen_height: int,
        background_image_path: str,
        full_screen: bool = False,
        fps: int = 60,
    ):
        # Initialize pygame
        pygame.init()

        # Set variables
        self.screen = pygame.display.set_mode(
            (screen_width, screen_height), full_screen
        )
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

        # Set background to image
        load_background = pygame.image.load(background_image_path)
        self.background = pygame.transform.scale(
            load_background, (screen_width, screen_height)
        )

        self.fps = fps

    def check_exit_game(self, event):
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            self.running = False
        return self.running

    def draw_background(self):
        self.screen.blit(self.background, (0, 0))

    def put_work_on_screen(self):
        pygame.display.flip()
        self.dt = self.clock.tick(self.fps) / 1000
