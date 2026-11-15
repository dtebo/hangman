import pygame
import random

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

        self.particle_count = random.randint(100, 1000) # Generate random particle count

        # Particle effect attributes
        self.particles = []
        self.rx = 0
        self.ry = 0
        self.dx = 0
        self.dy = 0
        self.x = 0
        self.y = 0
        self.particle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw_particles(self, screen):
        self.particles = [
            (
                random.randrange(screen.get_width()),
                random.randrange(screen.get_height()),
                random.randint(2, 8),
            )
            for _ in range(self.particle_count)
        ]
        self._render_particles(screen)

    def _render_particles(self, screen):
        for x, y, radius in self.particles:
            pygame.draw.circle(screen, self.particle_color, (x, y), radius)

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

        if self.particles:
            self._render_particles(self.screen)

        current_time = pygame.time.get_ticks()
        remaining_seconds = max(
            0, self.duration - (current_time - self.start_time) // 1000
        )
        minutes, seconds = divmod(remaining_seconds, 60)
        countdown = f"{self.text} {minutes:02}:{seconds:02}".strip()
        text_surface = self.font.render(countdown, True, self.color)
        text_rect = text_surface.get_rect(center=self.position)
        self.screen.blit(text_surface, text_rect)