import pygame
import game
import menu
import player
import random

class Hangman:
    def __init__(self):
        current_game = game.Game("Hangman")
        background = pygame.image.load(".\\images\\backgrounds\\menu_background.png")
        pygame.display.set_caption(current_game.name)
        pygame.init()
        screen = pygame.display.set_mode((1280,720))
        clock = pygame.time.Clock()
        show_menu = True  # Flag to control the menu display
        game_menu = menu.Menu()

        current_game.load_menu_audio(".\\audio\\menumusic.mp3")  # Load and play menu audio

        while current_game.status == "playing":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    current_game.status = "quitted"

                result = game_menu.handle_input(event) # Handle menu input

                if result == "Exit":
                    current_game.status = "quitted"
                elif result == "Start Game":
                    show_menu = False
                    current_game.status = "playing"
                    background = pygame.image.load(".\\images\\backgrounds\\game_background.png")
                    current_game.load_game(screen, background)

                if event.type == pygame.ACTIVEEVENT:
                    if event.gain:  # Window is minimized or loses focus
                        pygame.mixer.music.unpause()  # Unpause the music
                    else:  # Window is minimized or loses focus
                        pygame.mixer.music.pause()  # Pause the music

            screen.blit(background, (0, 0))

            game_menu.draw(screen, show_menu)  # Draw the menu if show_menu is True

            pygame.display.update()

            dt = clock.tick(60) / 1000

        if current_game.status == "quitted":
            pygame.mixer.music.stop()  # Stop the music when quitting

        pygame.quit() # Quit the game when the status is "quitted"

hangman_game = Hangman()