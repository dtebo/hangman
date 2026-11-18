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

class Particle:
     def __init__(self, screen):
          self.screen = screen
          self.x = 40
          self.y = 250
          self.angle = 0
          self.size = random.randint(1, 8)
          self.particle_color = (0, 255, 125)

     def draw(self, screen):
        pygame.draw.circle(screen, self.particle_color, (round(self.x), round(self.y)), self.size)

     def update(self):
         self.t = pygame.time.get_ticks() / 8 % 400
         self.x = self.t
         self.y = math.sin(self.t/50.0) * 100 + 200
         self.y = int(self.y)