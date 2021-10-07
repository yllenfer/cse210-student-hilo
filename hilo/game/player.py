import random


class Player:
    def __init__(self):
        self.card_number = 0

    def get_card_number(self):
        self.card_number = random.randint(1, 13)
