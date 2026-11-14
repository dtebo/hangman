class Board:
    def __init__(self, selected_word):
        self.size = len(selected_word)
        self.lines = ["_" for _ in selected_word]

    def display(self):
        print(" ".join(self.lines))