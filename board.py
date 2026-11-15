import pygame

class Board:
    def __init__(self, selected_word):
        self.size = len(selected_word)
        self.lines = ["_" for _ in selected_word]

    def display(self, screen):
        if screen is None:
            raise ValueError("A valid pygame screen is required to display the board.")

        if not pygame.get_init():
            pygame.init()

        font = pygame.font.Font(None, 96)
        blanks = " ".join(self.lines)
        text = font.render(blanks, True, (245, 245, 245))
        text_rect = text.get_rect(center=(screen.get_width() // 2 + 200, screen.get_height() // 2))

        screen.blit(text, text_rect)
