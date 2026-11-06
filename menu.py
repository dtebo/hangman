
import pygame


class Menu:
    def __init__(self):
        self.options = ["Start Game", "Options", "Exit"]
        self.selected_option = 0

    def draw(self, screen, show_menu=True):
        if not show_menu:
            return

        # Draw the menu options on the screen
        for i, option in enumerate(self.options):
            color = (0, 50, 225) if i == self.selected_option else (80, 80, 80)
            pygame.font.init()
            font = pygame.font.Font(pygame.font.get_default_font(), 36)
            text = font.render(option, True, color)
            screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2 - len(self.options) * 20 + i * 40))

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.options[self.selected_option]

        pygame.event.clear()  # Clear the event queue to prevent multiple inputs from being processed

        return None