import pygame
import math

from standards import LENGTH_OF_GUN
from standards import SCREEN_WIDTH
from standards import SCREEN_HEIGHT

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #, pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0

# Load background image
load_background = pygame.image.load("images/background.jpg")
background = pygame.transform.scale(load_background, (1280, 720))

# Set player position in the middle of the board
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # Exit game if window is closed or ESC is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # Set background to image
    screen.blit(background, (0, 0))
    
    # Draw a line from the player to the mouse
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos_x = mouse_pos[0]
    mouse_pos_y = mouse_pos[1]
    
    # Gun end position
    gun_end_pos_x = (LENGTH_OF_GUN / math.dist(player_pos, mouse_pos)) * (mouse_pos_x - player_pos.x) + player_pos.x
    gun_end_pos_y = (LENGTH_OF_GUN / math.dist(player_pos, mouse_pos)) * (mouse_pos_y - player_pos.y) + player_pos.y
    gun_end_pos = (gun_end_pos_x, gun_end_pos_y)

    # Draw objects on screen
    pygame.draw.line(screen, "black", player_pos, gun_end_pos, 5) # Draw the gun
    pygame.draw.circle(screen, "blue", player_pos, 20) # Draw player
    
    # Move player with WASD
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # Put the work on the screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()