import pygame

from board import Board
from player import Player
from bullet import Bullet

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

bullets = []
while board.running:
    board.draw_background()
    player.draw_gun(board.screen)
    player.draw_player(board.screen)

    events = pygame.event.get()
    for event in events:
        board.check_exit_game(event)
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.time.delay(10)
            mouse_pos = pygame.mouse.get_pos()
            gun_end_pos = player.gun_end_pos
            bullet = Bullet(gun_end_pos, mouse_pos, 10)
            bullets.append(bullet)
    for bullet in bullets:
        bullet.move_bullet(board.screen, board.dt)

    player.move_player(board.dt)

    # Check if player shoots
    # bullet = player.shoot()
    # if bullet:
    #    bullet.move_bullet(board.screen, board.dt)

    board.put_work_on_screen()
pygame.quit()
