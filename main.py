import pygame

from player import Player
from board import Board

# Game setup
board = Board(
    screen_width=1280,
    screen_height=720,
    background_image_path="images/background.jpg",
    full_screen=False,
    fps=60,
)

player = Player(
    length_of_gun=30,
    player_pos=pygame.Vector2(
        board.screen.get_width() / 2, board.screen.get_height() / 2
    ),
    player_color="blue",
    gun_color="black",
    player_speed=300,
    player_radius=20,
)

# Game loop
while board.running:
    board.check_exit_game()
    board.draw_background()
    player.draw_gun(board.screen)
    player.draw_player(board.screen)
    player.move_player(board.dt)
    board.put_work_on_screen()
pygame.quit()
