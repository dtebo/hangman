import random
import board
import effect
import player
import pygame

class Game:
    def __init__(self, name, status="playing"):
        self.word_list = ["python", "pizza", "cat", "dog", "computer", "programming", "hangman"]
        self.guessed_letters = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts
        self.name = name
        self.time_remaining = 120 #Number of seconds for the game
        self.status = status #Game status: playing, won, lost, quitted
        self.selected_word = random.choice(self.word_list) #The word to guess
        self.board = None
        self.effect = None

    def load_menu_audio(self, audio_file):
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file, "mp3")
        pygame.mixer.music.play(-1)  # Play the audio in a loop

    def load_game(self, screen, background):
        # Load the game
        player.score = 0
        player.name = "Player 1"  # Set the player's name

        screen.blit(background, (0, 0))

        self.board = board.Board(self.selected_word)  # Create a Board instance with the selected word
        self.board.display(screen)  # Display the board on the screen

        self.effect = effect.Effect(screen)  # Create an Effect instance
        self.effect.start(
            "Time remaining:",
            (255, 255, 255),
            (screen.get_width() // 2, 40),
            self.time_remaining,
        )