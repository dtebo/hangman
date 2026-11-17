import pygame
import random
import math

class Effect:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 48)
        self.text = ""
        self.color = (255, 255, 255)
        self.position = (0, 0)
        self.duration = 0
        self.start_time = 0
        self.active = False

    def start(self, text, color, position, duration):
        self.text = text
        self.color = color
        self.position = position
        self.duration = duration
        self.start_time = pygame.time.get_ticks()
        self.active = True

    def update(self):
        if not self.active:
            return

        current_time = pygame.time.get_ticks()
        remaining_seconds = max(
            0, self.duration - (current_time - self.start_time) // 1000
        )
        minutes, seconds = divmod(remaining_seconds, 60)
        countdown = f"{self.text} {minutes:02}:{seconds:02}".strip()
        text_surface = self.font.render(countdown, True, self.color)
        text_rect = text_surface.get_rect(center=self.position)
        self.screen.blit(text_surface, text_rect)


class Snowflake:
    def __init__(self, screen):
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.base_x = random.randrange(self.width)
        self.x = self.base_x
        self.y = random.randrange(self.height)
        self.size = random.randint(2, 5)
        self.speed = random.uniform(1, 3)
        self.sway_amplitude = random.uniform(10, 30)
        self.sway_speed = random.uniform(0.01, 0.03)
        self.angle = random.uniform(0, math.pi * 2)

    def update(self):
        self.y += self.speed
        self.angle += self.sway_speed
        self.x = self.base_x + math.sin(self.angle) * self.sway_amplitude

        if self.y > self.height:
            self.base_x = random.randrange(self.width)
            self.y = random.randrange(-20, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (round(self.x), round(self.y)), self.size)