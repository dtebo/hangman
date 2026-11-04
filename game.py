import random
import menu
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

    def load_menu_audio(self, audio_file):
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file, "mp3")
        pygame.mixer.music.play(-1)  # Play the audio in a loop