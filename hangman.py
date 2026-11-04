import pygame
import game
import menu
import player
import random

class Hangman:
    def __init__(self):
        background = pygame.image.load(".\\images\\backgrounds\\menu_background.png")
        current_game = game.Game("Hangman")
        print(f"Selected word: {current_game.selected_word}")  # Debugging line to show the selected word
        pygame.display.set_caption(current_game.name)
        pygame.init()
        screen = pygame.display.set_mode((1280,720))
        clock = pygame.time.Clock()
        game_menu = menu.Menu()

        current_game.load_menu_audio(".\\audio\\menumusic.mp3")  # Load and play menu audio

        while current_game.status == "playing":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    current_game.status = "quitted"

                game_menu.handle_input(event) # Handle menu input

                if event.type == pygame.ACTIVEEVENT:
                    if event.gain:  # Window is minimized or loses focus
                        pygame.mixer.music.unpause()  # Unpause the music
                    else:  # Window is minimized or loses focus
                        pygame.mixer.music.pause()  # Pause the music

            screen.blit(background, (0, 0))

            game_menu.draw(screen)

            pygame.display.update()

            dt = clock.tick(60) / 1000

        pygame.quit()

hangman_game = Hangman()