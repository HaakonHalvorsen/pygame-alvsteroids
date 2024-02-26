import pygame


class Bullet(object):
    def __init__(self, gun_end_pos, mouse_pos, bullet_speed):
        self.bullet_pos = pygame.Vector2(gun_end_pos)
        self.mouse_pos = pygame.Vector2(mouse_pos)
        self.bullet_speed = bullet_speed

    def move_bullet(self, screen, dt):
        screen_width = screen.get_width()
        screen_height = screen.get_height()

        # While bullet not outside of screen
        while (
            self.bullet_pos.x < 0
            or self.bullet_pos.x > screen_width
            or self.bullet_pos.y < 0
            or self.bullet_pos.y > screen_height
        ):
            # Update bullet position
            self.bullet_pos.x += self.bullet_speed * dt
            self.bullet_pos.y += self.bullet_speed * dt

            print(self.bullet_pos)

            pygame.draw.circle(
                screen, color="yellow", center=self.bullet_pos, radius=50
            )
