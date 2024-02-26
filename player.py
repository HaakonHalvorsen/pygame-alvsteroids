import math
import pygame


class Player(object):
    def __init__(
        self,
        length_of_gun: int,
        player_pos: pygame.Vector2,
        player_color: str,
        gun_color: str,
        player_speed: int,
        player_radius: int,
    ):
        self.length_of_gun = length_of_gun
        self.player_pos = player_pos
        self.mouse_pos = None
        self.player_color = player_color
        self.gun_color = gun_color
        self.player_speed = player_speed
        self.player_radius = player_radius

    def draw_player(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen, self.player_color, self.player_pos, self.player_radius
        )

    def _get_mouse_pos(self):
        return pygame.mouse.get_pos()

    def draw_gun(self, screen: pygame.Surface):
        # Convert the mouse position to a vector
        mouse_pos_tuple = self._get_mouse_pos()
        self.mouse_pos = pygame.Vector2(mouse_pos_tuple)

        gun_end_pos_x = (
            self.length_of_gun / math.dist(self.player_pos, self.mouse_pos)
        ) * (self.mouse_pos.x - self.player_pos.x) + self.player_pos.x
        gun_end_pos_y = (
            self.length_of_gun / math.dist(self.player_pos, self.mouse_pos)
        ) * (self.mouse_pos.y - self.player_pos.y) + self.player_pos.y
        gun_end_pos = (gun_end_pos_x, gun_end_pos_y)

        pygame.draw.line(screen, self.gun_color, self.player_pos, gun_end_pos, 5)

    def _get_keys_pressed(self):
        return pygame.key.get_pressed()

    def move_player(self, dt: int):
        keys = self._get_keys_pressed()
        if keys[pygame.K_w]:
            self.player_pos.y -= self.player_speed * dt
        if keys[pygame.K_s]:
            self.player_pos.y += self.player_speed * dt
        if keys[pygame.K_a]:
            self.player_pos.x -= self.player_speed * dt
        if keys[pygame.K_d]:
            self.player_pos.x += self.player_speed * dt
